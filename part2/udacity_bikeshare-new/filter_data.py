
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# how to use seaborn
from matplotlib.figure import Figure
# for the plot visualization


def filter_data(city,month,weekday):
    '''function to get data from csv files devided by city
       return
       data: the file of city from csv
    '''
    # start install csv_files(three) as seperate as city
    CITY_DATA = {'Chicago':'chicago.csv',
             'NewYorkCity':'new_york_city.csv',
             'Washington':'washington.csv'}
    # CITY_DATA is dict so use items() to traverse/遍历 to get keys & values
    for (key,values) in CITY_DATA.items():
        if key==city:
            data = pd.read_csv(values)
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    data['start_month'] = data['Start Time'].dt.month
    data['start_hour'] = data['Start Time'].dt.hour
    data['start_weekday'] = data['Start Time'].dt.weekday
    if month != None:
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July','Augest','September','October ','November','December']
        start_month = months.index(month) + 1
        data = data[data['start_month'] == start_month]
    if weekday != None:
        weeks = ['Sunday','Monday','Tuesday','Wednesday ','Thursday ','Friday ','Saturday']
        # weekday start from 0 to 6 as the indexs don't need to add 1
        start_weekday = weeks.index(weekday)
        data = data[data['start_weekday'] == start_weekday]
    # in order to anlysis data
    return data


def data_analysis(data,two_choosen_parts):
    mode_name = data[two_choosen_parts].value_counts().first_valid_index()
    mode_count = data[two_choosen_parts].value_counts().iloc[0,]
    return mode_name,mode_count
def trip_dutation(data):
    trip_dutation_sum = data['Trip Duration'].sum()
    trip_dutation_mean = data['Trip Duration'].mean()
    return trip_dutation_sum,trip_dutation_mean
def user_analysis(data,three_parts_user):
    if three_parts_user == 'User Type'or three_parts_user == 'Gender':
        total_type_analysis = data[three_parts_user].value_counts()
        return total_type_analysis
    elif three_parts_user == 'Birth Year':
        year_min = data[three_parts_user].min()
        year_max = data[three_parts_user].max()
        year_mode = data[three_parts_user].value_counts().first_valid_index()
        return year_min,year_max,year_mode

########################### main ##############################
# data = filter_data('Chicago', 'March', 'Monday')
# print (data)
# thwo_choosen_parts = ['Start Station','End Station']
# data_analysis(data,'End Station')
# trip_dutation(data)
# three_parts_user = ['User Type','Gender','Birth Year']
# user_analysis(data,'User Type')
# seems like some city file don't have the user type

def main ():
    while True:
        city = input('\nWhich city do you want to walk through ? Chicago, NewYorkCity, Washington \n')
        month = input('\nWhich month,January,February,March,Apri,May,June,July,Augest,September,October,November,December ? \n')
        weeday = input('\nWhich weekday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday \n')
        print(filter_data(city,month,weekday))



        restart = input('\nWould you like to restar ? Enter yes or no.\n')

if __name__ == "__main__":
    main()
