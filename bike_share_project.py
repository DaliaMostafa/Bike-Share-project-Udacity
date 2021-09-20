import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month = "all of them"
    day = "all of them"
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Nice to do business with you :), please choose and inter the city you want to explore; chicago  new york city  washington :').lower()
    while city not in ['chicago','new york city','washington']:
        print('This is an invalid input please try again !!')
        city= input('Hello, please choose and inter the city you want to explore; chicago  new york city  washington :').title()

    filter1= input('Do you want to filter your data, please enter Y or N: ').upper()
    while filter1 not in ['Y','N']:
        print('This is an invalid input please try again !!')
        filter1= input('Do you want to filter your data, please enter Y or N: ').upper()

    if filter1=="Y":
        filter2 = input("Please, choose from the following options, (Month, Day, or Both): ").lower()
        if filter2=="both":
            month= input('please enter the month you are intrested to explore (available months from january to june): ').lower()
            while month not in ['january','february','march','april','may','june']:
                print('This is an invalid input please try again !!')
                month= input('please enter the month you are intrested to explore (available months from january to june): ').lower()

            day= input('please enter the day you are intrested to explore; saturday, sunday, monday, tuesday,wednesday, thursday, friday: ').lower()
            while day not in ['saturday', 'sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday']:
                print('This is an invalid input please try again !!')
                day= input('please enter the day you are intrested to explore; saturday, sunday, monday, tuesday,wednesday, thursday, friday: ').lower()
        if filter2=="month":
            month= input('please enter the month you are intrested to explore (available months from january to june): ').lower()
            while month not in ['january','february','march','april','may','june']:
                print('This is an invalid input please try again !!')
                month= input('please enter the month you are intrested to explore (available months from january to june): ').lower()
        if filter2 == "day":
            day= input('please enter the day you are intrested to explore; saturday, sunday, monday, tuesday,wednesday, thursday, friday: ').lower()
            while day not in ['saturday', 'sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday']:
                print('This is an invalid input please try again !!')
                day= input('please enter the day you are intrested to explore; saturday, sunday, monday, tuesday,wednesday, thursday, friday: ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all of them':

        df = df[df['month'] == month.title()]
        print(df['month'])
    if day != 'all of them':
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month= df['month'].mode()[0]

    print('The most common month is: {}'.format(common_month))

    # TO DO: display the most common day of week

    common_day= df['day'].mode()[0]
    print('The most common day is: {}'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]
    print('The most common hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('the most common start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('the most common end station is: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "-->" + df['End Station']
    common_combination=df['combination'].mode()[0]
    print('the most common combination are: {}'.format(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('The total trip duration: {}'.format(total_time))

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('The mean travel time: {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('We have 2 types of users: {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender'in df.columns:
        user_gender = df['Gender'].value_counts()
        print('Both male and female use our service: {}'.format(user_gender))
    else:
        print("Sorry, No Data Regarding Gender Is Available")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year= df['Birth Year'].min()
        latest_birth_year=df['Birth Year'].max()
        common_birth_year= df['Birth Year'].mode()[0]
        print("The earliest birth year is: {} \n The latest birth year is: {} \n The most common birth year is:{}" .format(earliest_birth_year, latest_birth_year, common_birth_year))
    else:
        print("Sorry, No Data Regarding Birth Year Is Available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    raw_data= input('would you like to go through our raw_data, please answer Y or N: ').upper()
    i= 0
    df = pd.read_csv(CITY_DATA[city])
    while raw_data== "Y":
        print(df[i:i+5])
        i+=5
        raw_data= input('would you like to go through our raw_data, please answer Y or N: ').upper()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
