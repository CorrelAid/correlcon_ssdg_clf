import modal
from codecarbon import OfflineEmissionsTracker
import os
from geopy.geocoders import Nominatim
import country_converter as coco
from correlcon_ssdg_clf.modal_region_names import regions_dict
import polars as pl
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from correlcon_ssdg_clf.helpers import multilabel_train_test_split
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, f1_score
import string

image = modal.Image.debian_slim().poetry_install_from_file("pyproject.toml").apt_install("iproute2").run_commands("python -m nltk.downloader punkt stopwords punkt_tab") 

app = modal.App(name="correlcon_ssdg_clf")

@app.function(
        image=image,
        timeout=50000,
        # only on team/enterprise plan
        # https://modal.com/docs/guide/region-selection
        # region="europe-west4"
)
def train_model(df):
    cloud_provider = os.getenv("MODAL_CLOUD_PROVIDER").replace("CLOUD_PROVIDER_","").lower()
    cloud_region = os.getenv("MODAL_REGION")

    print(f"cloud provider= {cloud_provider}, cloud region= {cloud_region}")
    
    if cloud_provider != "gcp":
        if cloud_region == "us-phoenix-1":
            modal_region = "Phoenix"
        else:
            modal_region = regions_dict[cloud_region][4:]
    
        cloud_provider = None
        cloud_region = None

        geolocator = Nominatim(user_agent = "correlcon")

        location = geolocator.geocode({"city": modal_region}, exactly_one=False, featuretype="city")
        location = location[0].raw["display_name"].split(", ")[-1]

        code = coco.convert(names = [location], to = 'iso3').upper()
        print(f"🌎 Code runs in {code} 🌎")

    else:
        print(f"🌎 This code runs on {cloud_provider} in {cloud_region}, which codecarbon has data for 🌎")
        code = None

    # code is run in docker container so probably bad estimate
    with OfflineEmissionsTracker(cloud_provider=cloud_provider, cloud_region=cloud_region, country_iso_code=code) as tracker:
        X_train_raw, X_test_raw, y_train, y_test = multilabel_train_test_split(
        df.select(pl.col("text")),
        df.select(pl.col("^SDG.*$")),
        stratify=df.select(pl.col("^SDG.*$")),
        test_size=0.2,
        train_size=0.8,
        random_state=21,
    )
        nltk_stopwords = stopwords.words('english')
        stemmer = PorterStemmer()
        def tokenizer(text):
            text = text.translate(str.maketrans('', '', string.punctuation))
            return  [stemmer.stem(word) for word in text.split() if word not in nltk_stopwords and word.isascii()]
        
        vectorizer = TfidfVectorizer(stop_words=None, preprocessor=None, tokenizer=tokenizer, ngram_range=(1,3), max_features=50000)

        print("Fitting tfidf..")
        vectorizer.fit(X_train_raw["text"].to_list())
        print("Extracting tf-idf vectors for Training data..")
        X_train = vectorizer.transform(X_train_raw["text"].to_list())
        print("Extracting tf-idf vectors for testing data..")
        X_test = vectorizer.transform(X_test_raw["text"].to_list())

        clf = BinaryRelevance(

        classifier = LogisticRegression(),
        require_dense = [True, True]
        )

        print("fitting logistic regression..")
        clf.fit(X_train, y_train)

        print("predicting.")
        y_pred = clf.predict(X_test)

        print("classification report")    
        print(classification_report(y_test,y_pred)) 

        print("f1 score") 
        print(f1_score(y_test,y_pred, average="macro")) 

    cc_data = pl.read_csv("/root/emissions.csv")
     
    # ['timestamp', 'project_name', 'run_id', 'experiment_id', 'duration', 'emissions', 'emissions_rate', 'cpu_power', 'gpu_power', 'ram_power', 'cpu_energy', 'gpu_energy', 'ram_energy', 'energy_consumed', 'country_name', 'country_iso_code', 'region', 'cloud_provider', 'cloud_region', 'os', 'python_version', 'codecarbon_version', 'cpu_count', 'cpu_model', 'gpu_count', 'gpu_model', 'longitude', 'latitude', 'ram_total_size', 'tracking_mode', 'on_cloud', 'pue']
    l_water = 0.12 #kWh https://www.co2online.de/energie-sparen/strom-sparen/strom-sparen-stromspartipps/wasserkocher/

    l_water_b = cc_data.tail(1).select(["energy_consumed"]).item(-1,-1)/l_water

    print(f"⚡ {l_water_b:.10f} litres of water could have been boiled.. ⚡")

@app.local_entrypoint()
def main():
    df = pl.read_csv("data/sdg_knowledge_hub.csv")
    train_model.remote(df)