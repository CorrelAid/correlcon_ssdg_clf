# Sustainable Sustainable Development Goal Text Classification

Originating from the need to classify CorrelAid projects by the Sustainable Developmen Goals (SDGs) they advance, this coding session aims to explore methods for doing this while also exploring how to assess ressource usage of the different methods. In the wake of increased usage of LLMs, such as ChatGPT, ressource consumption is rising fast. For machine learning tasks such as text classification, specialised, less ressource intensive models often achieve better performance than large general models. The goal of this session is to explore ways to find a balance between performance and ressource usage for the specific task of multi label text classification. The Session will begin with an introduction to the task at hand, followed by an introduction into how to measure ressource usage of excecuting code. Afterwards, several methods will be introduec, ranked by their ressource usage. 

## Task Definition
Multi Label Text Classification

## Project Setup

1. Install Poetry
    
    Follow [these](https://python-poetry.org/docs) instructions.

2. Clone Repo

3. `poetry install`

## Render Presentation

1. [Install Pandoc](https://pandoc.org/installing.html)

2. `pandoc -t revealjs -s -o documents/presentation/slides.html documents/presentation/slides.md -V revealjs-url=https://unpkg.com/reveal.js/ --include-in-header=documents/presentation/slides.css`

