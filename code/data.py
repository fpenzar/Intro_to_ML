#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pycountry_convert as pc

def get_continent(country_code):
    try:
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
attributeNames = np.asarray(df.columns[cols])

# We can determine the number of data objects and number of attributes using 
# the shape of X
N, M = X.shape

# DATA cleanup

# We will remove row 133, "Palestinian National Authority",
# because all of the relevant attributes are NaN

X = np.delete(X, 133, axis=0)

# Adding continents as a new attribute

continents = np.array([get_continent(country_code) for country_code in X[:,2]])
continents = continents.reshape(-1, 1)

# Add the values(continents) as a new column to the original matrix
X = np.hstack((X, continents))

# Update attributeNames
attributeNames = np.append(attributeNames, "Continent")

# Because some countries do not have a country code 
# or because the country code in the dataset and in the pycountry_convert module are not equal
# we will add them by hand
X[39,35] = "Africa"
X[56,35] = "Africa"
X[73,35] = "Europe"
X[81,35] = "Europe"
X[119,35] = "Africa"
X[128,35] = "Europe"
X[173,35] = "Asia"
