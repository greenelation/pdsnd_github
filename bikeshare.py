
# Import Neccessary Packages
from datetime import datetime
import pandas as pd
import numpy as np
import statistics as st

# Read the csv files
Chicago_bikeshare = pd.read_csv("chicago.csv")
NYC_bikeshare = pd.read_csv("new_york_city.csv")
Washington_bikeshare = pd.read_csv("washington.csv")


# Converting the object type to datetime datatype
Chicago_bikeshare['Start Time'] = pd.to_datetime(Chicago_bikeshare['Start Time'])
NYC_bikeshare['Start Time'] = pd.to_datetime(NYC_bikeshare['Start Time'])
Washington_bikeshare['Start Time'] = pd.to_datetime(Washington_bikeshare['Start Time'])
Chicago_bikeshare['End Time'] = pd.to_datetime(Chicago_bikeshare['End Time'])
NYC_bikeshare['End Time'] = pd.to_datetime(NYC_bikeshare['End Time'])
Washington_bikeshare['End Time'] = pd.to_datetime(Washington_bikeshare['End Time'])



# Declaring Initial ad empty variables
FilteredCity = "";
Option = "";
DfObj = pd.DataFrame()

# Function to get the City Option
def get_City(Chicago_bikeshare,NYC_bikeshare,Washington_bikeshare):
    FilteredCity = input('\nWould you like to see the data for Chicago, NYC or Washington? \n')
    if (FilteredCity.lower() == "chicago"):
        DfObj = Chicago_bikeshare
        get_Option(DfObj)
    elif (FilteredCity.lower() == "nyc"):
        DfObj = NYC_bikeshare
        get_Option(DfObj)
    elif (FilteredCity.lower() == "washington"):
        DfObj = Washington_bikeshare
        get_Option(DfObj)
    else :
        print ("Invalid Option. Please enter the correct option")
        get_City(Chicago_bikeshare,NYC_bikeshare,Washington_bikeshare)

# Fuction to get the option day of month
def get_Option(DfObj):
    Option = input('\nWould you like to filter the data by month, day, both or nofilter?\n')
    if (Option.lower() == "day"):
        filter_By_day(DfObj,False)
    elif (Option.lower() == "month"):
        filter_By_Month(DfObj)
    elif (Option.lower() == "nofilter"):
        print_Result(DfObj)
    elif (Option.lower() == "both"):
        filter_By_day(DfObj,True)
    else :
        print ("Invalid Option. Please enter the correct option")
        get_Option(DfObj)
        
# Function to filter by day        
def filter_By_day(DfObj,ShowBoth):
    DayOption = input('\nChoose a day to filter. Which day Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ?\n')
    DayOption = DayOption.lower()
    if (DayOption == "monday" or DayOption == "tuesday" or
        DayOption == "wednesday" or DayOption == "thursday" or
        DayOption == "friday" or DayOption == "saturday" or
        DayOption == "sunday" ):
        Result = DfObj[DfObj['Start Time'].dt.strftime('%A') == DayOption.capitalize()]
        if (ShowBoth == False):
            print_Result(Result)
        else :
            filter_By_Month(Result)
    else :
        print ("Invalid Option. Please enter the correct option")
        filter_By_day(DfObj,ShowBoth)
    
# Function to filter by month     
def filter_By_Month(DfObj):
    MonthOption = input('\nChoose a month to filter.  Which month - January, February, March, April, May, or June? ?\n')
    MonthOption = MonthOption.lower()
    if (MonthOption == "january" or MonthOption == "february" or
        MonthOption == "march" or MonthOption == "april" or
        MonthOption == "may" or MonthOption == "june"):
        Result2 = DfObj[DfObj['Start Time'].dt.strftime('%B') == MonthOption.capitalize()]
        print_Result(Result2)
    else :
        print ("Invalid Option. Please enter the correct option")
        filter_By_Month(DfObj)
        
# Function to print the result
def print_Result(FilteredResult):
    print ("Most Common Month of Travel")
    print ("Most Common Month of Travel in filtered dataset is ",st.mode(FilteredResult['Start Time'].dt.strftime('%B')))
    print ("Most Common Day of Week")
    print ("Most Common Day of Week of Travel in filtered dataset  is ",st.mode(FilteredResult['Start Time'].dt.strftime('%A')))
    print ("Most Common Hour of the Day")
    print ("Most Common Hour of the Day of Travel in filtered dataset is at ",st.mode(FilteredResult['Start Time'].dt.hour))
    print ("Popular Stations and Trips")
    print ("The Most Common Start Station in filtered dataset is ",st.mode(FilteredResult['Start Station']))
    print ("The Most Common End Station in filtered dataset is ",st.mode(FilteredResult['End Station']))
    Chicago_trip_series = FilteredResult["Start Station"].astype(str) + " to " + FilteredResult["End Station"].astype(str)
    Chicago_most_popular_trip = Chicago_trip_series.describe()["top"]
    Chicago_most_popular_trip_count = Chicago_trip_series.describe()["freq"]
    print(Chicago_most_popular_trip)
    print(Chicago_most_popular_trip_count)
    print("The Most frequent Combination in filtered dataset is ",Chicago_most_popular_trip,"and the nummber of times is ",Chicago_most_popular_trip_count)
    print("Trip Duration")
    print ("The total Trip Duration of filtered dataset is ",sum(FilteredResult['Trip Duration'])/3600," hours")
    print ("The average mins of each trip in filtered dataset is " ,st.mean(FilteredResult['Trip Duration'])/60, " minutes")
    #re_Run(FilteredResult)
    print_Five(FilteredResult,0)

# Function to rerun the program
def re_Run(FilteredResult):
    rerun = input('\nWould you like to rerun. Press Y for Yes or N or No\n') 
    rerun = rerun.lower()
    if (rerun == "y"):
        get_City(Chicago_bikeshare,NYC_bikeshare,Washington_bikeshare)
    elif (rerun == "n"):
        print ("Thanks for running the program")
    else :
        print ("Invalid Option. Please enter Y or N")
        re_Run(FilteredResult)



# Print Five Records
def print_Five(FilteredResult,i):
    while (i < len(FilteredResult)):
        print (FilteredResult.iloc[i:i+5,1:len(FilteredResult.columns)])
        i = i + 5
        break
    PrintAgain = input('\nWould you like to print another five records. Press Y to print next five records or any other key to exit this loop\n') 
    PrintAgain = PrintAgain.lower()
    if (PrintAgain == "y"):
        print_Five(FilteredResult,i)
    else :
        print ("Thanks for printing records")
        re_Run(FilteredResult)
   
        
        
    
# Calling the get City function
get_City(Chicago_bikeshare,NYC_bikeshare,Washington_bikeshare)        
    
    
    
