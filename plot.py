import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

HB = pd.read_csv('Hour_Borough.csv')
HB = HB.fillna(0)
HB.set_index(HB['Borough'])
# Imports from the csv file and sets up database

num_bor = len(HB)
HB['TotalPass'] = HB.sum(axis=1,numeric_only=True)
# Sums the total number of passengers for each borough

for j in range(6):
    name_str='Frac'+str(4*j)+'-'+str(4*(j+1))
    in_sum = 0
    for k in range(4):
          in_sum +=  HB[:][str(4*j)]
    HB[name_str] = in_sum/HB['TotalPass']
# Finds the fraction of total passengers in each 4 hour spell as a fraction of the total

bar_tot = plt.figure(figsize=(10, 6))
plt.bar(range(num_bor),HB['TotalPass'], color = '#2b8cbe')
plt.yscale('log')
for i in range(num_bor):
        plt.text(i, max(np.exp(np.log(HB['TotalPass'][i])*0.63),75), '{:.2e}'.format(HB['TotalPass'][i]), ha = 'center',color='white')

tick_list = HB['Borough']
tick_list[tick_list=='EWR'] = 'Newark Airport'
plt.xticks(range(num_bor),tick_list,size=10)
plt.ylabel('Journeys',size=12)
plt.xlabel('Borough of Origin',size=12,loc='center')
plt.title('Uber Journeys by Borough',size=16)
bar_tot.savefig('Journeys_Borough.pdf')
plt.clf()
# Creates log bar chart of journeys from each borough

col_ext = HB.columns[(HB.columns.str.match(r'[Frac][0-9]*'))]

text_pie = ['00:00-04:00','04:00-08:00','08:00-12:00','12:00-16:00','16:00-20:00','20:00-24:00']
pie_hours = plt.figure(figsize=(15, 10))
for j in range(6):
    plt.subplot(3,2,j+1)
    plt.title(HB.loc[j]['Borough'])
    HB.loc[j][col_ext].plot(kind='pie',labels=text_pie,fontsize=8,colormap='viridis', autopct='%1.0f%%')
    plt.ylabel('')
plt.suptitle('Taxi Pickup Hour by Borough')
plt.savefig('PickupTime_Borough.pdf')

# Creates subplots with the distribution of each pickup time for different locations