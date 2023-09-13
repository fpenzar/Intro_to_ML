# REPORT 1

Noa Margeta (232470), Eva Kaštelan (232469), Filip Penzar (232452)\
Group 127

---

## Description of the Dataset

This dataset contains a wide range of information about countries worldwide.
It covers every country globally and its attributes serve as basic categories describing each country. Categories include demographic statistics, healthcare metrics, economic indicators, education statistics, environmental data, and others. The global-wide inclusion of all countries allows for a wide perspective that can be used for in-depth analyses and cross-country comparisons.

The dataset can be obtained at [kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023).

### Previous Data Analysis Projects

This [data analysis](https://www.kaggle.com/code/amgedelshiekh/continent-level-eda#1.-GDP) does an exploratory data analysis utilizing statistical graphics and other data visualization methods. Its analysis is divided into 3 overarching categories hoping to look closer into GDP, Good place to live in, and Gasoline prices. The first subsection of the work considers several different relations that the author hypothesizes to be relevant to the GDP attribute. (GDP - Population, GDP - Fertility rate, Industrialization - Agriculture, GDP - Taxes, GDP - Army). The subsection begins by noting a linear relationship between population and GDP. Contrary to expectations, it finds no correlation between fertility rates and GDP in Europe, while other continents show a negative correlation. The subsection also highlights a strong 92% correlation between GDP and CO2 emissions, emphasizing that economic growth often leads to increased pollution. This correlation extends to the percentage of urban population and CO2 emissions, indicating the environmental challenges posed by urbanization. Regarding land use, there's no significant correlation between GDP and the percentage of agricultural land, except for Oceania, where a reversal relationship exists, and South America, where a positive correlation is observed.
The role of taxes in nation-building is discussed, with negative correlations between tax revenue and GDP in Asia, North America, and South America, but a positive correlation in Oceania. No clear correlation is found in Europe and Africa. Lastly, the exponential relationship with the Army suggests that economic growth often leads to increased defense spending. In the second subsection relations, which are assumed to bring about a better life, are being analyzed. The analysis compares the minimum wage, post-tax minimum wage, higher education enrollment, out-of-pocket health expenditure, and other attributes to the countries' GDP. In it positive correlations are shown between post-tax minimum wage and GDP per population, minimum wage and GDP, higher education enrollment and individual GDP, as well as healthcare and GDP. Conversely, negative correlations are observed between taxation and minimum wage, suggesting that in some countries with high tax rates, the minimum wage is lower. Additionally, there is a strong negative correlation between life expectancy and fertility rates, implying that as one rises, the other declines. Primary education does not have a specified correlation in the text. The final subsection explores the attributes tax money, minimum wage, and CPI in relation to the Gasoline prices in the country. What the further analysis shows is a strong positive correlation between Tax revenue and minimum wage factors and Gasoline Prices, outside Africa. The opposite is ascertained for the consumer price index.

### Project Goals

This project focuses on the manipulation, examination, description, and visualization of the data in order to provide a solid starting point for the upcoming project, in which the focus will be on classification and regression models.

#### Classification
Classification models are used to categorize data into predefined classes or categories.
For the classification problem, the goal will be to create such a model that can predict the continent a country is on (`Continent` the chosen class label attribute), based on several other features. 
The attributes will include:

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

Regression models are used to predict a continuous numeric value based on input features. 
For the regression problem, the goal will be to predict the value of `Gross Tertiary Education Enrollment`. Attributes used for the prediction will include:

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

Since the original dataset does not come with the attribute that describes the continent a country is on, the attribute needed to be added. This was done with a [python library](https://pypi.org/project/pycountry-convert/).
Attributes with a high percentage of null values across the dataset were excluded so as not to introduce bias in the models. 

## Detailed Explanation of the Data Attributes

A basic description of the relevant attributes is shown in the following table:

| Attribute | Details |   | Attribute type   |
|:---|:---|:---:|:---:|
| Abbreviation | Abbreviation or code representing the country |discrete|nominal|
| Agricultural Land | Percentage of land area used for agricultural purposes (%) |continuous|ratio|
| Birth rate|  Number of births per 1,000 population per year |continuous|ratio|
| Continent| Continent name of country |discrete|nominal|
| CPI | Consumer Price Index, a measure of inflation and purchasing power |continuous|ratio|
|Fertility Rate | Average number of children born to a woman during her lifetime | continuous | ration|
|Forested Area |Percentage of land area covered by forests (%) | continuous | ratio |
| Density| Population density measured in persons per square kilometer (P/Km2) |continuous|ratio|
| GDP | Gross Domestic Product, the total value of goods and services produced in the country |continuous|ratio|
| Gasoline price| Price of gasoline per liter in local currency  |continuous|ratio|
| Gross Primary Education Enrollment |Gross enrollment ratio for primary education (%) |continuous|ratio|
| Gross Tertiary Education Enrollment| Gross enrollment ratio for tertiary education (%) |continuous|ratio|
| Infant Mortality| Number of deaths per 1,000 live births before reaching one year of age |continuous|ratio|
| Life Expectancy |Average number of years a newborn is expected to live.  |continuous|ratio|
| Maternal mortality ratio | Number of maternal deaths per 100,000 live births |continuous|ratio|
| Physicians per thousand people| Number of physicians per thousand people  |continuous|ratio|
| Population | Total population of the country |continuous|ratio|
| Unemployment rate| Percentage of the labor force that is unemployed |continuous|ratio|
| Urban population | Percentage of the population living in urban areas |continuous|ratio|

