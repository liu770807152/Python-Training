"""
Template for the COMP1730/6730 project assignment, S2 2021.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/


The assignment is due 25/10/2021 at 9:00 am, Canberra time

Collaborators: <,,>
"""
import os
import csv
from collections import Counter

def analyse(path_to_files):
    '''
        Question 1
        Finding the CSV file with the most recent date, 
        find out the exact timestamp of the last record being updated.
        And from this most recent file, report the total number of cases and deaths worldwide
    '''
    #Create a function to get the data table
    def getfiletable(file):
        with open('./covid-data/%s' % file) as csvfile:
            reader = csv.reader(csvfile)
            table = [ row for row in reader ]
        return table
    
    #Get the CSV file and sort it in descending order
    files = []
    dirs = os.listdir(path_to_files)
    for file in dirs:
        filetype = os.path.splitext(file)[1]
        if filetype == ".csv":
            files.append(file)
        else:
            continue
    files.sort(reverse=True)
    
    #Open the most recent file
    table = getfiletable(files[0])
    
    #Get update date
    last_update_list = [ table[i][4] for i in range(1,len(table)) ]
    last_update = max(last_update_list)
    
    #Get the number of cases and deaths worldwide
    confirmed_list = [ int(table[i][7]) for i in range(1,len(table)) ]
    deaths_list = [ int(table[i][8]) for i in range(1,len(table)) ]
    #Calculate sum
    total_worldwide_cases = sum(confirmed_list)
    total_worldwide_deaths = sum(deaths_list)
    
    print('Analysing data from folder ... \n')
    print('Question 1:',
          '\nMost recent data is in file `%s`' % files[0],
          '\nLast updated at %s' % last_update,
          '\nTotal worldwide cases: %d, Total worldwide deaths: %d' % (total_worldwide_cases, total_worldwide_deaths))
    
    
    '''
        Question 2
        For every country in the world, calculate the total number of confirmed cases 
        and deaths in that country from the most recent CSV file, then sort the countries 
        in descending order of number of cases and print top 10. For every country, 
        compute the number of new cases during the one day immediately before the last update.
    '''
    #Get the country list, and calculate the number of duplicate countries
    country_list = [ table[i][3] for i in range(1,len(table)) ] 
    count = Counter(country_list)
    
    #Get the number of cases and deaths during the one day immediately before the last update. 
    pre_table = getfiletable(files[1])
    pre_confirmed_list = [ int(pre_table[i][7]) for i in range(1,len(pre_table)) ]
    pre_deaths_list = [ int(pre_table[i][8]) for i in range(1,len(pre_table)) ]
    
    rank = []
    for key in count:
        country_cases_deaths_new_active = []
        cases = 0 #total cases
        deaths = 0 #total deaths
        pre_cases = 0 #total cases before the last update
        pre_deaths = 0 #total deaths before the last update
        
        #Add country name to list
        country_cases_deaths_new_active.append(key)
        
        #Calculate the total number of cases and deaths in each country
        for i in range(count[key]):
            cases += confirmed_list[country_list.index(key) + i]
            deaths += deaths_list[country_list.index(key) + i]
            pre_cases += pre_confirmed_list[country_list.index(key) + i]
            pre_deaths += pre_deaths_list[country_list.index(key) + i]
            
        country_cases_deaths_new_active.append(cases)
        country_cases_deaths_new_active.append(deaths)
        country_cases_deaths_new_active.append(cases - pre_cases)
        '''
        2(c)
        Let’s use simple maths we would like to calculate real cases 
        on a day given the deaths at that day. To calculate true active cases, 
        the calculation needs to be very country-specific 
        and also requires enough cases to become statistically correct.
        For people to die, there must have been deaths/(fatality rate) people.
        Since deaths happen after a few days of contracting disease, 
        the cases grew at the doubling rate.So the active cases on a day given the deaths 
        on that day are "deaths*(daysToDie/InfectionRateDays)/fatality_rate".
        Here, the average number of days required to die, and the number of days 
        required to infect the next person, we use the WHO’s worldwide median.
        This equation can only be a simple estimate of actives. 
        Due to different medical conditions, different countries are very different. 
        Developed countries often have more medical resources, 
        which can make critically ill patients survive longer, 
        even in different regions of the same country.
        There is a big difference. We refer to many research reports. 
        It is very difficult to accurately estimate active cases, and as the virus mutates, 
        many data will change. We compared our estimation results with official data, 
        and other countries except US basically meet the scope of our estimation.
        
        Referencing:
            https://towardsdatascience.com/calculating-live-covid-19-cases-from-deaths-e70e5df45f60

        '''
        #caluate fatality rate
        fatality_rate = deaths / cases
        #caluate active range
        if fatality_rate == 0:
            lower_bound = 0
            higher_bound = 0
        else:
            higher_bound = int(((deaths - pre_deaths) * 2** (22/5)) / fatality_rate)
            lower_bound = int(((deaths - pre_deaths) * 2** (20/5)) / fatality_rate)
            
        
        country_cases_deaths_new_active.append(lower_bound)
        country_cases_deaths_new_active.append(higher_bound)
        
        #Add the data of each country to the rank
        rank.append(country_cases_deaths_new_active)
    
    #Sort by total cases in descending order
    rank.sort(key = lambda x:x[1], reverse=True)
    
    print('\nQuestion 2:')
    for i in range(0,10):
        print('%s - total cases: %d deaths: %d new: %d active: %d - %d' 
              % (rank[i][0], rank[i][1], rank[i][2], rank[i][3], rank[i][4], rank[i][5]))
    
    
    '''
        Question 3
        Caluate the worldwide number of new daily cases and new daily deaths for each 
        of the days that you can find from the data files, except for the oldest day.
        Summarise the number of new cases and deaths on a weekly.
    '''
    print('\nQuestion 3:')
    
    for i in range(0, len(files)-1):
        table1 = getfiletable(files[i])
        table2 = getfiletable(files[i+1])
        #Get file name
        filename = os.path.splitext(files[i])[0]
        
        #Get the number of cases and deaths
        table1_confirmed_list = [ int(table1[i][7]) for i in range(1,len(table1)) ]
        table2_confirmed_list = [ int(table2[i][7]) for i in range(1,len(table2)) ]
        table1_deaths_list = [ int(table1[i][8]) for i in range(1,len(table1)) ]
        table2_deaths_list = [ int(table2[i][8]) for i in range(1,len(table2)) ]
    
        #Calculate the difference between the sum of the two days
        daily_new_cases = sum(table1_confirmed_list) - sum(table2_confirmed_list)
        daily_new_deaths = sum(table1_deaths_list) - sum(table2_deaths_list)
        
        print('%s : new cases: %d   new deaths: %d' % (filename, daily_new_cases, daily_new_deaths))
    print('\n')
    
    files.sort(reverse=False)
    for j in range(int(len(files) / 7), -1, -1):
        start_file = files[7 * j]
        table3 = getfiletable(start_file)
        
        if 7 * j + 6 > len(files):
            end_file = files[len(files) - 1]
            table4 = getfiletable(end_file)
        else:
            end_file = files[7 * j + 6]
            table4 = getfiletable(end_file)
            
        #Get the number of cases and deaths 
        table3_confirmed_list = [ int(table3[i][7]) for i in range(1,len(table3)) ]
        table4_confirmed_list = [ int(table4[i][7]) for i in range(1,len(table4)) ]
        table3_deaths_list = [ int(table3[i][8]) for i in range(1,len(table3)) ]
        table4_deaths_list = [ int(table4[i][8]) for i in range(1,len(table4)) ]
        
        #Calculate the difference between the sum of the two weeks
        weekly_new_cases = sum(table4_confirmed_list) - sum(table3_confirmed_list)
        weekly_new_deaths = sum(table4_deaths_list) - sum(table3_deaths_list)
         
        print('Week %s to %s : new cases: %d  new deaths: %d' 
              % (os.path.splitext(start_file)[0], os.path.splitext(end_file)[0], weekly_new_cases, weekly_new_deaths))
  
    
    '''
        Question 4
    '''
    print('\nQuestion 4:')
    
    
    
    

# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on folder containg all CSV files
    analyse('./covid-data')
