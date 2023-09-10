# REPORT 1

Noa Margeta (232470), Eva Kaštelan (232469), Filip Penzar (232452)\
Group 127

---

## Description of the Dataset

This dataset contains a wide range of information about countries worldwide.
It covers every country globally and its attributes serve as basic categories describing each country. Categories include demographic statistics, healthcare metrics, economic indicators, education statistics, environmental data, and other. The global-wide inclusion of all countries allows for a wide perspective which can be used for in-depth analyses and cross-country comparisons.

The dataset can be obtained at [kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023).

### Previous Data Analysis Projects

In this [data analysis](https://www.kaggle.com/code/amgedelshiekh/continent-level-eda#1.-GDP), a number of different relations are considered. Some examples:
* GDP - Population
* GDP - Fertility rate
* Industrialization - Agriculture
* GDP - Taxes
* GDP - Army

### Project Goals

This project focuses on the manipulation and examination of the data in order to provide a solid starting point for the upcoming project, in which the focus will be on classification and regression models.

#### Classification

For the classification problem, the goal will be to create a model that can predict the continent a country is on (`Continent` variable), based on a number of other variables. The variables will include:
* GDP
* Life Expectancy
* Physicians per thousand people
* Gross Primary Education Enrollment
* Gross Tertiary Education Enrollment
* Infant Mortality
* CPI
* Agricultural Land
* Density
* Birth rate
* Forested area
* Gasoline price
* Maternal mortality ratio
* Unemployment rate
* Urban population
* Population
* Physicians per thousand people

#### Regression

For the regression problem, the goal will be to predict the value `Gross Tertiary Education Enrollment`. Variables used for the prediction will enclude:
* GDP
* Life Expectancy
* Continent
* Physicians per thousand people
* Gross Primary Education Enrollment
* Gross Tertiary Education Enrollment
* Infant Mortality
* CPI
* Agricultural Land
* Density
* Birth rate
* Gasoline price
* Maternal mortality ratio
* Unemployment rate
* Urban population
* Population
* Physicians per thousand people

#### Data Transformation

Since the original dataset does not come with the attribute that descrbes the continent a country is on, the attribute needed to be added. This was done with a [python library](https://pypi.org/project/pycountry-convert/).
Attribute with high percentage of null values across the dataset were excluded so as not to introduce bias in the models. 

## Detailed Explanation of the Data Attributes

