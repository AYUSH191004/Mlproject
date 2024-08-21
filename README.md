# Diamond Price Prediction

This repository contains the code and resources used for building a machine learning model to predict diamond prices based on various features such as carat, cut, clarity, and color.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Training](#model-training)
- [Results](#results)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Diamond pricing is a complex task influenced by several factors including carat, cut, clarity, and color. This project aims to predict the price of diamonds using machine learning techniques.

## Dataset
The dataset used in this project contains features related to diamond characteristics:
- **Carat**: Weight of the diamond.
- **Cut**: Quality of the cut, categorized into 5 levels (Fair, Good, Very Good, Ideal, Premium).
- **Clarity**: Internal purity of the diamond, categorized into 8 levels (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF).
- **Color**: Rated from D to J, with D being the most colorless and J being the most yellow.
- **Price**: Target variable representing the price of the diamond.

The dataset is publicly available and can be accessed [here](https://raw.githubusercontent.com/sunnysavita10/Gemstone-Price-Prediction-End-to-End/main/NOTES/data/gemstone.csv).

## Exploratory Data Analysis (EDA)
The EDA process involves:
- **Data Cleaning**: Handling missing values and duplicates.
- **Categorical Data Exploration**: Analyzing distributions of categorical variables like cut, color, and clarity.
- **Numerical Data Exploration**: Analyzing distributions of numerical variables like carat and price.
- **Correlation Analysis**: Investigating correlations between features.

Detailed analysis can be found in the `EDA.ipynb` notebook.

## Model Training
The model training process includes:
- **Data Preprocessing**: Imputation, encoding, and scaling of features.
- **Model Selection**: Various regression models are trained, including Linear Regression, Lasso, Ridge, and Decision Trees.
- **Model Evaluation**: Models are evaluated based on performance metrics like RMSE and R².

Detailed code for model training is available in the `model_training.ipynb` notebook.

## Results
The best-performing model in this project was the DECISION TREE REGRESSOR with an R² score of 99.99979369604115.

# git commands 
''' git init -> to commit and connect it 
''  conda create -p (name of enviroment)  python=3.8 (model) -y -> in order to create a virtual enviromnet 
''''  source activate (source path) ->  to activate the enviroment 

:::  .gitignore ->  includes files that should be ignore 
 ''' git init
'' git add
'' git commit -m "message"
'' git branch -M origin

''' git remote add origin <repo url>  ->  add repo to origin of repo
''' git remote -v   ->  file in remote repo
'''  git push -u origin main  ->   push the files to the branch specifyed
