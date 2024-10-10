---
author: Jonas Stettner (CorrelAid)
title: Sustainable Sustainable Development Goal Text Classification 
date: October 13, 2024
---
## Agenda for the next 90 minutes

1. Talk (~15 minutes)
    - Reflecting on the current development in AI usage and its consequences
    - What does this mean for Data4Good?
    
2. Tutorial (~30 minutes) 
    - Multi Label Text Classification with Binary Relevance with TF-IDF and Logistic Regression
    - Introduction to modal (severless code execution) and codecarbon (measuring carbon emission) 

3. Coding Session (~45 minutes) 
    - Learning the introduced methods with example tasks
    - Freestyle exploration

## Intro 

- Emergent AI energy crisis $^{1}$, causing cloud providers to utilize fault-prone nuclear reactors $^{2}$

- The physical reality of the cloud and AI: 
    - 🔌 Global power consumption of data centres to range between **620 - 1050 TWh** in 2026. Comparison: Europe consumed **3.674 TWh** in 2022 $^{3}$
    - 🏭 ICT sector currently responsible for a similar percentage of global carbon emission as aviation: **~2%** $^{4}$
    - 🌊 AI may be accountable for more than the total annual water withdrawal of **4 – 6** Denmark or **half** of the United Kingdom in 2027 $^{5}$

- Trusting in innovation: Increased efficiency can lead to increased overall resource consumption (Jevons Paradoxon or Rebound Effects)

 <hr/>
 <ol>
  <li class="smaller">Crawford, K. (2024). Generative AI’s environmental costs are soaring — and mostly secret. Nature, 626, 693–693. doi: [10.1038/d41586-024-00478-x](https://www.nature.com/articles/d41586-024-00478-x)</li>
  <li class="smaller">Luscombe, R. (2024). Three Mile Island nuclear reactor to restart to power Microsoft AI operations. [The Guardian](https://www.theguardian.com/environment/2024/sep/20/three-mile-island-nuclear-plant-reopen-microsoft)</li>
  <li class="smaller">IEA (2024), Electricity 2024, IEA, Paris https://www.iea.org/reports/electricity-2024</li>
  <li class="smaller"> Aouf, R. S. (2024). AI's "eye-watering" use of resources could be a hurdle to achieving climate goals, argue experts. [Dezeen](https://www.dezeen.com/2023/08/09/ai-resources-climate-environment-energy-aitopia/)</li>
   <li class="smaller"> Li, P., Yang, J., Islam, M. A., & Ren, S. (2023). Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models. arXiv, 2304.03271. doi: [10.48550/arXiv.2304.03271](    
   https://doi.org/10.48550/arXiv.2304.03271)</li>
  </ol>
 
---

## Brief digression on AI hype

- The method being hyped to solve all of the worlds problems and currently mostly being understood as AI is **Deep Learning** (large neural models)

- Deep Learning can only solve pattern matching problems (learning data distributions) with lots of available data $^{1}$

- Potential Performance Improvement Barriers
    - Data Availability $^{2}$ and Model Collapse $^{3}$
    - Neural Scaling Laws: Diminishing Marginal Returns $^{4}$

- Don't trust the hype but also dont trust the anti-hype hype

 <hr/>
 <ol>
    <li class="smaller">Stevens, H. (2024, October 10). In a new manifesto, OpenAI’s Sam Altman envisions an AI utopia – and reveals glaring blind spots. Retrieved from https://theconversation.com/in-a-new-manifesto-openais-sam-altman-envisions-an-ai-utopia-and-reveals-glaring-blind-spots-239841</li>
    <li class="smaller">Villalobos, P., Ho, A., Sevilla, J., Besiroglu, T., Heim, L., & Hobbhahn, M. (2022). Will we run out of data? Limits of LLM scaling based on human-generated data. arXiv, 2211.04325 doi: [10.48550/arXiv.2211.04325](https://arxiv.org/abs/2211.04325)</li>
    <li class="smaller">Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. Nature, 631, 755–759. doi: [10.1038/s41586-024-07566-y](https://www.nature.com/articles/s41586-024-07566-y)</li>
    <li class="smaller">Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., ...Amodei, D. (2020). Scaling Laws for Neural Language Models. arXiv, 2001.08361. doi: [10.48550/arXiv.2001.08361](https://arxiv.org/abs/2001.08361)</li>
</ol>

---

## Hypothesis

- Large neural models (not including neural models recently defined as being small) are inefficient with regard to performance and resource consumption for a range of tasks

- Alternatives can achieve **better** performance with **less** ressources or achieve a better balance

- Examples:
    - Search
    - Web Scraping (parsing)

- NLP: Specialized Small Language Models vs. Generalized Large Language Models

- Small gains in performance lead to an unproportional resource consumption increase (more computational requirements, different model)

---

## The Sustainable Development Goals

- The 17 Sustainable Development Goals are part of an agenda that the UN is working towards

- Defines a desirable future for society and environment

- The UN additionally introduced a range of indicators to measure progress, 

- E.g. Climate Action (SDG 13) 
    - "*Take urgent action to combat climate change and its impacts*" $^{1}$
    - Indicator 13.2.2: Total greenhouse gas emissions per year $^{2}$

 <hr/>
 <ol>
  <li class="smaller">THE 17 GOALS | Sustainable Development. (2024, October 02). Retrieved from https://sdgs.un.org/goals</li>
  <li class="smaller">SDG Indicator 13.2.2 - Total greenhouse gas emissions per year - German Indicators For The UN Sustainable Development Goals. (2024, October 04). Retrieved from https://sdg-indikatoren.de/en/13-2-2 </li>
  </ol>

## Ethical Reasoning

- As Data4Good practioners, following a **utilitarian logic**, we should be aware that we can have impact on one challenge with the help of methods that worsen a different problem

- Advancing SDG "Zero Hunger" at the cost of SDG "Climate Action" has the potential to make an approach overall **unsustainable** 

- Some challenges of this simple utalitarian logic: 
    - Some aspects of human experience can't be quantified
    - Irreversible extinction of a species can be a understood as a qualitative loss transcending biodiversity loss
    - Uncertain tipping points and complex dynamics 

- ➡️ First step is to make visible and quantify a methods consequences

---

## Today's (Meta) Task

- Origin Story: Classifying past CorrelAid projects by the SDG they advance

- Multi Label Text Classification (vs. binary and multi-class)

- Chosen Dataset: "SDG Knowledge Hub Dataset of SDG-labeled News Articles" 
 
-  ➡️ Exploring tools to measure power consumption and carbon emissions of running classification code

<hr/>
 <ol>
    <li class="smaller">SDG Knowledge Hub Dataset of SDG-labeled News Articles. (2023, January 10). doi: [10.5281/zenodo.7523032](https://zenodo.org/records/7523032)</li>
</ol>

---

## Tutorial Introduction

- Presentation will continue in a Jupyter Notebook 
    - How to "quantify" text
    - Binary Relevance with TF-IDF and Logistic Regression 

- Afterwards we will work through a script for code deployment
    - Running code with modal
    - Measuring Power Consumption and Carbon Emissions with the `codecarbon` package

- If you want to, you can follow along on your own machine with the repo at: https://github.com/CorrelAid/correlcon_ssdg_clf 

---

## Coding Session Setup

- Follow the Project Setup steps in this workshops repo: https://github.com/CorrelAid/correlcon_ssdg_clf 

- **What you can do now**:
    - Ask questions or discuss the topic with me or in groups in while others start coding
    - Work on the tasks described in (ordered by difficulty)
    - Freestyle coding 💃

---




