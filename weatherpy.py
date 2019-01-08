# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:50:05 2018
@author: Deepali
%matplotlib inline
"""


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key
import api_keys

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

#**********************
#Generate Cities List
#**********************

# List for holding lat_lngs and cities# List  
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)

#**********************
#Perform API Calls
#**********************


#**********************
#Convert Raw Data to DataFrame
#**********************

#**********************
#Plotting the Data
#**********************

#Latitude vs. Temperature Plot
#Latitude vs. Humidity Plot
#Latitude vs. Cloudiness Plot
#Latitude vs. Wind Speed Plot
