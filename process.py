import numpy as np
import pandas as pd
from datetime import datetime

JanJune = pd.read_csv('uber-tlc-foil-response-master/uber-trip-data/uber-janjune-15.csv')
# Import the data from Jan to June
tzl = pd.read_csv('uber-tlc-foil-response-master/uber-trip-data/taxi-zone-lookup.csv')
# Import the location data
JanJune.rename(columns={'locationID':'LocationID'},inplace=True)
JJ_merge=pd.merge(JanJune, tzl, on='LocationID',how='left')
# Merge the location data with the ride data to get location names

JJ_merge['PickupDate'] = pd.to_datetime(JJ_merge.Pickup_date) #,'%Y-%m-%d %H:%M:%S')
JJ_merge['PickupHour'] = JJ_merge['PickupDate'].apply(lambda x: x.hour)
# Extracts the pickup hour

hour_borough = JJ_merge.groupby(['Borough','PickupHour']).Zone.count().reset_index()
hour_borough.rename(columns={'Zone':'Count'},inplace=True)
hb_pivot = hour_borough.pivot(columns = 'PickupHour', index='Borough', values = 'Count')
# Groups by borough and pickup hour and pivots the table

hb_pivot.to_csv('Hour_Borough.csv')
 
