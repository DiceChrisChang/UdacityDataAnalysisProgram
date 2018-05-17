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
    global df
    # start install csv_files(three) as seperate as city
    CITY_DATA = {'chicago':'chicago.csv',
             'newyorkcity':'new_york_city.csv',
             'washington':'washington.csv'}
    # CITY_DATA is dict so use items() to traverse/遍历 to get keys & values
    for (key,values) in CITY_DATA.items():
        if key==city:
            df = pd.read_csv(values)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['start_month'] = df['Start Time'].dt.month
    df['start_hour'] = df['Start Time'].dt.hour
    df['start_weekday'] = df['Start Time'].dt.weekday
    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'augest', 'september', 'october', 'november', 'december']
    weeks = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    # weekday start from 0 to 6 as the indexs don't need to add 1
    if month == 'all' and weekday == 'all':
        # this is the kind of not filter at all
        return df
    elif month != None and weekday != None:
        start_month = months.index(month) + 1
        start_weekday = weeks.index(weekday)
        df = df[df['start_month'] == start_month]
        df = df[df['start_weekday'] == start_weekday]
        return df
    elif month != None and weekday == None:
        start_month = months.index(month) + 1
        df = df[df['start_month'] == start_month]
        return df
    elif month == None and weekday != None:
        start_weekday = weeks.index(weekday)
        df = df[df['start_weekday'] == start_weekday]
        # print(data)
        return df
    else:
        # JUST IN CASE
        df = None
        return df
    # in order to anlysis data

def data_analysis(data,two_choosen_parts):
    if two_choosen_parts == 'start station':
        two_choosen_parts = 'Start Station'
    elif two_choosen_parts == 'end station':
        two_choosen_parts = 'End Station'
    else:
        print('Your enter is not percise, try add a blank between two words !')
    mode_name = data[two_choosen_parts].value_counts().first_valid_index()
    mode_count = data[two_choosen_parts].value_counts().iloc[0,]
    return mode_name,mode_count

def trip_dutation(data):
    trip_dutation_sum = ['sum',data['Trip Duration'].sum()]
    trip_dutation_mean =['mean',data['Trip Duration'].mean()]
    return trip_dutation_sum,trip_dutation_mean

def user_analysis(data,three_parts_user):
    if three_parts_user == 'user type' :
        three_parts_user = 'User Type'
        total_type_analysis = data[three_parts_user].value_counts()
        return total_type_analysis
    elif three_parts_user == 'gender' :
        three_parts_user = 'Gender'
        total_type_analysis = data[three_parts_user].value_counts()
        return total_type_analysis
    elif three_parts_user  == 'birth year':
        three_parts_user = 'Birth Year'
        year_min = ['min',data[three_parts_user].min()]
        year_max = ['max',data[three_parts_user].max()]
        year_mode = ['mode',data[three_parts_user].value_counts().first_valid_index()]
        return year_min,year_max,year_mode

def famous(city):
    '''
    Without filters, first show the hotest month,hour,weekday in this city that user choosen
    '''
    global data
    data = filter_data(city,'all','all')
    start_month =['hotest month',data['start_month'].mode()[0]]
    start_hour = ['hotest hour',data['start_hour'].mode()[0]]
    start_weekday = ['hotest weekday',data['start_weekday'].mode()[0]]
    print(start_month)
    print(start_weekday)
    print(start_hour)

def filters():
    '''
    get values from input and use filter_data to filter return a data seperate datetime
    '''
    global data
    # try:
    city = input('\nWhich city do you want to walk through ? Chicago, NewYorkCity, Washington \n')
    city = city.lower()
    print('I am going to show you the most famous month, weekday and hour in this city.')
    famous (city)
    three_choices = input('\nWould you like to filter datas from months,weekdays,not at all or both, m for months, w for weekdays, n for not ar all, b for both, \n')
    # make input check more comfortable
    three_choices = three_choices.lower()
    if three_choices == 'b':
        month = input('\nWhich month January,February,March,April,May,June,July,Augest,September,October,November,December ? \n')
        weekday = input('\nWhich weekday Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday \n')
        weekday = weekday.lower()
        month = month.lower()
    elif three_choices == 'w':
        weekday = input('\nWhich weekday Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday \n')
        weekday = weekday.lower()
        month = None
    elif three_choices == 'm':
        month = input('\nWhich month January,February,March,April,May,June,July,Augest,September,October,November,December ? \n')
        month = month.lower()
        weekday = None
    elif three_choices == 'n':
        month = weekday = 'all'
    data = filter_data(city,month,weekday)
    # except:
    #     print('There is something wrong in your input, plesase try again! ')
    #     filters()
    # else:
    if data.empty or data is None:
        print('This kind of date that you choosen is empty, please try again')
        filters()


    return data,city

def analysis_station(data):
    try:
        choose = input('\nWoule you like to watch data by start/end station or combine both, you can enter s for one or enter b for both? \n')
        choose = choose.lower()
        if choose == 's':
            two_choosen_parts = input('\ninput Start Station or End Station to find out the hotest\n')
            two_choosen_parts = two_choosen_parts.lower()
            data_analysis(data,two_choosen_parts)
        elif choose == 'b':
            #### find the most popular trip from start station to end station ####
            combine_station_data = ['the hostest trip',data.groupby(['Start Station','End Station']).size() \
            .reset_index(name='count').sort_values(by = ['count'], ascending = False).iloc[0,]]
    except:
        print('There is something wrong in your input, plesase try again! ')
        analysis_station(data)
    else:
        if choose == 's':
            print(data_analysis(data,two_choosen_parts))
        elif choose == 'b':
            print(combine_station_data)

def personal_info(data,city):
        if city == 'washington':
            print('I am going to show you the calculate user type of Washington city by bike ')
            print(user_analysis(data,'user type'))
        else:
            three_parts_user = input('\nWhich kind of data do you want from User Type, Gender, Birth Year ? \n')
            three_parts_user = three_parts_user.lower()
            print(user_analysis(data,three_parts_user))
            retry = input('\nDo you want to see other kinds of info ? Yes or No \n')
            if retry.lower() == "yes" :
                personal_info(data,city)
            else:
                return

########################### main ##############################
global data
def main ():
    while True:
        data,city = filters()

        analysis_station(data)

        print('I am going to show you the calculate time of whole trip by bike ')
        print(trip_dutation(data))
        # data = filter_data('Chicago','March','Monday')

        personal_info(data,city)

        restart = input('\nWould you like to restar ? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
