import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS= ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november']
DAYS =  ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Which city do you want to explore? chicago, new york, washington\n')
            if city.lower() in CITY_DATA:
                break
            else:
                print('Enter valid city name..\n')
        except ValueError:
            
            print("Provide a string value...\n")
            continue

    #get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Which month do you want to explore? all, january, february, ... , etc\n')
            if month.lower() in MONTHS or month == 'all':
                break
            else:
                print('Enter valid month name..\n')
        except ValueError:
            
            print("Provide a string value...\n")
            continue


    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Which day do you want to explore? all, saturday, sunday, ... , etc\n')
            if day.lower() in DAYS or day == 'all':
                break
            else:
                print('Enter valid day name..\n')
        except ValueError:
            
            print("Provide a string value...\n")
            continue

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df = pd.read_csv(CITY_DATA[city])
  

    #Converting time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = MONTHS.index(month) + 1

        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #display the most common month
    print('\nCalculating The Most Common Month to Travel...\n')
    common_month = df['month'].mode()[0]
    print('Most Common Month : {}  Counts {}'.format(MONTHS[common_month-1].title(),df['month'].value_counts()[common_month]))

    #display the most common day of week
    print('\nCalculating The Most Common Day to Travel...\n')
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day : {}   Counts {}'.format(common_day,df['day_of_week'].value_counts()[common_day]))
    
    #display the most common start hour
    print('\nCalculating The Most Common Start Hour to Travel...\n')
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour : {}   Counts {}'.format(common_hour,df['hour'].value_counts()[common_hour]))
    
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('******************************')
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nCalculating The Most Common Start Station to Travel...\n')    
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station : {}   Counts : {}'.format(common_start_station,df['Start Station'].value_counts()[common_start_station]))
    
    #display most commonly used end station
    print('\nCalculating The Most Common End Station to Travel...\n')    
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station : {}   Counts : {}'.format(common_end_station,df['End Station'].value_counts()[common_end_station]))

    #display most frequent combination of start station and end station trip
    print('\nCalculating The Most Common Start & End Station to Travel...\n')  
    station_combination = df['Start Station'] + ' TO ' + df['End Station']
    common_stations = station_combination.mode()[0]
    print('Most Common Start & End Station : {}   Counts : {}'.format(common_stations,station_combination.value_counts()[common_stations]))    

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('******************************')
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    print('\nCalculating The Total Travel Time...\n') 
    total_duration = df['Trip Duration'].sum()
    total_days = total_duration /86400 
    total_hours = (total_duration/3600)%24
    total_minutes = (total_hours % 1)*60
    remained_seconds = (total_minutes%1)*60
    print('Total Travel Time : \n{} Days,\n{} Hours,\n{} Minutes,\n{} Seconds '.format(int(total_days),int(total_hours),int(total_minutes),round(remained_seconds)))
     

    #display mean travel time
    print('\nCalculating The Average Travel Time...\n')    
    avg_duration = df['Trip Duration'].mean()
    print('Average Travel Time : {} '.format(avg_duration))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('******************************')
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print('\nCalculating Counts of User Types...\n')    
    user_types = df['User Type'].value_counts()
    print('User Types Count : \n{}'.format(user_types))    

    #Display counts of gender
    print('\nCalculating Counts of Gender...\n')
    if 'Gender' in df:      
        gender_count = df['Gender'].value_counts()
        print('Gender Count : \n{}'.format(gender_count))    
    else:
        print('No Available Gender Data for This City\n')

    #Display earliest, most recent, and most common year of birth
    print('\nCalculating earliest, most recent, and most common year of birth...\n')   
    if 'Birth Year' in df: 
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('Earliest Year : {}, \nMost Recent Year : {}, \nMost Common Year {} '.format(earliest_year,recent_year,common_year))  
    else:
        print('No Available Birth Year Data for This City\n')

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('******************************')
    print('-'*40)

def raw_data(df):
    """Asks the user if he wants to view raw data 5 rows at a time
    """
    
    start_index = 0
    end_index = 5

    while True:
        try:
            response = input('\nDo you want to keep seeing 5 rows of raw data? Enter yes or no.\n')
            if response.lower() == 'yes' and start_index <= len(df):
                print(df.iloc[start_index:end_index])
                start_index+=5
                end_index+=5       
            elif response.lower() == 'no' or start_index > len(df):
                print('\nNo Problem, good luck! :)\n')
                break
            else:
                print('Enter a valid string\n')

        except ValueError:
            print("Provide a string value...\n")
            continue
                
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
