import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('uber-tlc-foil-response-master/uber-trip-data/uber-janjune-15.csv')
tzl = pd.read_csv('uber-tlc-foil-response-master/uber-trip-data/taxi-zone-lookup.csv')
df.rename(columns={'locationID':'LocationID'},inplace=True)
test=pd.merge(df, tzl, on='LocationID',how='left')
# # print(tzl['LocationID'])
test['BookHour'] = pd.Series(np.zeros(len(test)))
for i in range(0,len(test)):
    test.BookHour[i] = datetime.strptime(test.Pickup_date[i],'%Y-%m-%d %H:%M:%S').hour
# print(test)
hour_borough = test.groupby(['Borough','BookHour']).Zone.count().reset_index()
hour_borough.rename(columns={'Zone':'Count'},inplace=True)
hb_pivot = hour_borough.pivot(columns = 'BookHour', index='Borough', values = 'Count')
hb_pivot.to_csv('Hour_Borough.csv')

# print(df.groupby('Affiliated_base_num'))
