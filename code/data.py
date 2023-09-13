#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pycountry_convert as pc

def get_continent(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except Exception as e:
        return "Country not found"

# Load the dataset using the Pandas library
filename = '../data/dataset.csv'
df = pd.read_csv(filename)

# Pandas returns a dataframe, (df) which could be used for handling the data.
# We will however convert the dataframe to numpy arrays for this course as 
# is also described in the table in the exercise
raw_data = df.values  

# We start by making the data matrix X by indexing into data.
cols = range(0, 35) 
X = raw_data[:, cols]

# We can extract the attribute names that came from the header of the csv
attribute_names_raw = np.asarray(df.columns[cols])

# DATA cleanup

# attributes we want to delete (see the report on why we remove each of them)
attributes_to_remove = ["Armed Forces size", "Abbreviation", "Land Area(Km2)", "Calling Code", "Capital/Major City", "CPI Change (%)", "Co2-Emissions", "Currency-Code", "Largest city", 
                        "Minimum wage", "Official language", "Out of pocket health expenditure", "Population: Labor force participation (%)", "Tax revenue (%)", 
                        "Total tax rate", "Latitude", "Longitude"]

# get the indices of the columns to remove
indices = np.where(np.isin(attribute_names_raw, attributes_to_remove))

# remove the columns from the dataset
filtered_data = np.delete(X, indices, axis=1)
attribute_names = np.delete(attribute_names_raw, indices)

# index of the country
country_index = np.where(np.isin(attribute_names, ["Country"]))

p = 0
# get a list of countries that have more than p percent null values
def calculate_nan_perc_per_row(row):
    nan_count = sum(np.isnan(x) if isinstance(x, (float, np.floating)) else False for x in row)
    return nan_count / len(row)

nan_percentages = [calculate_nan_perc_per_row(row) for row in filtered_data]
indices_with_multiple_nans = np.where(np.array(nan_percentages) > p)[0]

# get the country names of the deleted countries
deleted_countries = filtered_data[indices_with_multiple_nans, country_index][0]
print(deleted_countries)

# Remove the countries with too many null attributes
X = np.delete(filtered_data, indices_with_multiple_nans, axis=0)

# Adding continents as a new attribute

continents = np.array([get_continent(country_name) for country_name in X[:,0]])
continents = continents.reshape(-1, 1)

# Add the values(continents) as a new column to the original matrix
X = np.hstack((X, continents))

# Update attributeNames
attribute_names = np.append(attribute_names, "Continent")

# convert the attributes to numerical values
def convert_to_numerical(value):
    if isinstance(value, str):
        value = value.replace('%', '').replace('$', '').replace(",", "")
        try:
            return float(value)
        except ValueError:
            return value
    else:
        return value

X = np.vectorize(convert_to_numerical)(X)

# Because some countries do not have a country code 
# or because the country code in the dataset and in the pycountry_convert module are not equal
# we will add them by hand
X[9][18] = "North America"
X[51][18] = "Africa"
X[67][18] = "Europe"
X[142][18] = "Asia"
attribute_names[1] = "Density (P/Km2)"
attribute_names[9] = "Gross primary education(%)"
attribute_names[10] = "Gross tertiary education(%)"
# We can determine the number of data objects and number of attributes using 
# the shape of X
N, M = X.shape
