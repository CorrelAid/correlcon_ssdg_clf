# CorrelCon 2024 Workshop: Sustainable Sustainable Development Goal Text Classification

As the use of generative AI such as ChatGPT increases, so does the associated global resource consumption, to the point where Big Tech is reportedly considering operating fault-prone nuclear reactors. However, for many tasks, alternative, less resource-intensive approaches often achieve similar or even better performance than large general-purpose language models. Born out of the need to classify CorrelAid projects according to the Sustainable Development Goals (SDGs) they advance, this coding session aims to strike a balance between performance and resource consumption of multi label text classification methods.

We will start with a reflection on the current developments in AI usage and their consequences, including the ethical implications for Data4Good. A tutorial on multi-label text classification using binary relevance with TF-IDF and Logistic Regression follows. We will also introduce Modal for serverless code execution and the codecarbon package for measuring carbon emissions. The session will conclude with a coding session where participants can practice the introduced methods through predefined tasks or engage in freestyle exploration.

## Project Setup

1. Install Poetry
    
    Follow [these](https://python-poetry.org/docs) instructions.

2. Fork or clone this Repo

3. `poetry install`

4. Create an account on [modal.com](https://modal.com/signup)

5. Run `poetry run modal setup`

## Render Presentation

1. [Install Pandoc](https://pandoc.org/installing.html)

2. `pandoc -t revealjs -s -o documents/presentation/slides.html documents/presentation/slides.md -V revealjs-url=https://unpkg.com/reveal.js/ --include-in-header=documents/presentation/slides.css`

