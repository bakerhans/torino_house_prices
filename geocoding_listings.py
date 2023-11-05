from geopy.geocoders import Nominatim
import time
from random import randint
import geocoder
import logging

# Need to configure logging. But first need to understand how it works and how to use it properly


user = randint(1000,9999)
geolocator = Nominatim( user_agent= f"Torino-listings-{user}") # probaby don't need this if i'm using geocoder.py?

# Initialize empty longitude and latitude columns
th_no_missing_price['Longitude'] = np.NaN
th_no_missing_price['Latitude'] = np.NaN

# Loop through addresses in dataframe to geocode each listing
for address in th_no_missing_price['Address description']:
    location = geolocator.geocode(address)
    
    if location is None: continue
    
    # Extract the longitude and latitude of current address
    th_no_missing_price['Longitude'][address] = location.longitude
    th_no_missing_price['Latitude'][address] = location.latitude
    
    # Maintain at least 1 second per request as per Nomatim policy, and random interval to avoid time-out
    time.sleep(randint(1,10))
    
    
    