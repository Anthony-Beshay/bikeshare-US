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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input('Enter a city to filter by: ').strip().lower()
        if city in CITY_DATA.keys():
            break
        elif city not in CITY_DATA.keys():
            print('Enter a valid city!')

        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input('Enter a month to filter by: ').strip().lower()
        if month in months:
            break
        elif month not in months:
            print('Enter a valid month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input('Enter a day to filter by: ').strip().lower()
        if day in days:
            break
        elif day not in days:
            print('Enter a valid day!')

        

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
    
    df = pd.read_csv(CITY_DATA.get(city))
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hours'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   
    most_month = df['month'].value_counts().index[0]
    month_count = df['month'].value_counts()[0]
    try:
        df['month'].value_counts().index[1]
        print('Most Common Month: {}, with count: {}'.format(most_month, month_count))
        
    except IndexError:
        pass
        
    # TO DO: display the most common day of week
    
    most_day = df['day_of_week'].value_counts().index[0]
    day_count = df['day_of_week'].value_counts()[0]
    try:
        df['day_of_week'].value_counts().index[1]
        print('Most Common Day of Week: {}, with count: {}'.format(most_day, day_count)) 
        
    except IndexError:
        pass 
    # TO DO: display the most common start hour
    most_hour = df['hours'].value_counts().index[0]
    hour_count = df['hours'].value_counts().iloc[0]
    print('Most Common Start hour: {}, with hour count: {}'.format(most_hour, hour_count))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].value_counts().index[0]
    start_count = df['Start Station'].value_counts()[0]
    # TO DO: display most commonly used end station
    most_end = df['End Station'].value_counts().index[0]
    end_count = df['End Station'].value_counts()[0]
    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'].astype(str) +' - '+ df['End Station']
    most_start_end = df['start_end'].value_counts().index[0]
    start_end_count = df['start_end'].value_counts()[0]
    
    print('Most Commonly Used Start Station: {}, with count: {}'.format(most_start, start_count)) 
    print('Most Commonly Used End Station: {}, with count: {}'.format(most_end, end_count))
    print('Most Frequent Combination of Start and End Station Trip: {}, with count: {}'.format(most_start_end, start_end_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    count_t_travel = df['Trip Duration'].count()

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()

    print('Total Travel Time: {}, with count: {}'.format(total_travel, count_t_travel))
    print('Mean Travel Time: {}'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('Subscriber count is {}'.format(user_types['Subscriber']))
    print('Customer count is {}'.format(user_types['Customer']))
    # TO DO: Display counts of gender
    
    try:
        user_gender = df['Gender'].value_counts()
        print('Male count: {}'.format(user_gender['Male']))
        print('Female count: {}'.format(user_gender['Female']))
    except:
        print('NO available information about gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        most_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth: {}'.format(earliest_birth)) 
        print('Most Recent year of birth: {}'.format(recent_birth))
        print('Most Common year of birth: {}'.format(most_birth))

    except:
        print('NO available information about year of birth')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ display the first 5 rows of raw data until the user says no"""
    
    print('\nDisplaying User Data...\n')
    start_time = time.time()
    
    # TO DO: ask the user if they want to see individual data
    view_data = input('Do you want to see 5 rows of individual data? Respond by yes/no.\n')
    start_loc = 0
    
    # TO DO: create a loop that prints the first 5 rows of data, and breaks whenever the answer is no
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5, :])
        view_data = input('Do you want to see more 5 rows of individual data? Respond by yes/no.\n')
        if view_data == 'yes':
            start_loc += 5
        elif view_data == 'no':
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
