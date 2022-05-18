import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "D:\Data Analytics\Professional Track\Project\chicago.csv",
               'new york city': "D:\Data Analytics\Professional Track\Project/new_york_city.csv" ,
              'washington': "D:\Data Analytics\Professional Track\Project\washington.csv"}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
            city = str(input('Enter the city please (chicago ,new york city, washington) : ')).lower().strip()
            if city in CITY_DATA :
                break
            else :
                 print('Please enter correct city ,choose one from these (chicago ,new york city, washington).')     
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
            month = str(input('Enter the month or all please :(all, january, february, ... , june) : ')).lower().strip()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month in months or month == 'all':
                break
            else :
                print('Please enter the correct month or all  :(all, january, february, ... , june).')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
            day = str(input('Enter the day or all please : (all, monday, tuesday, ... sunday) : '))
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            if day in days or day == 'all' :
                break
            else :
                print('Please enter the correct day or all :(all, monday, tuesday, ... sunday)')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is: ',common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour: ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']   #creat new column contains date of start and end station columns
    common_combination = df['combination'].mode()[0]
    print('The most common station of each start and end station is: ',common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total drive time = {} hour'.format(total_travel_time/3600))

    # TO DO: display mean travel time
    avg_of_travel_time = df['Trip Duration'].mean()
    print('The mean of travel time = ',avg_of_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()[0]
    print('The count of user types : ',count_of_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df :
        count_of_gender = df['Gender'].value_counts()[0]
        print('The count of gender : ',count_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :
        earliest_year= df['Birth Year'].min()
        print('Earliest year of birth : ',earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('The most recent year of birth : ',most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth : ',most_common_year)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def diplay_data(df) :
    answer = str(input('I can display the first 5 rows of data, Do you want that ? (yes,no): ')).strip().lower()
    counter = 0
    while True :
        if answer == 'yes' :
            print(df[counter:counter+5])
            counter+=5 
            answer = str(input('Would you like the next 5 rows ?'))
        else :
                break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        diplay_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
