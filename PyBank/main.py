# REMINDER: to create a folder in GitHub use "/" at the end of the folder name to transform into a folder

# First, import os module - allows to create file path across operating systems 
import os 

# Import module for reading csv files & set correct path to csv files 
import csv 
budget_data = os.path.join("python-challge", "PyBank", "budget_data.csv")

#Translate csv opening in Python 
with open(budget_data, newline="") as csvfile: 

    #csv reader specifies delimiter (parameter tells Python each comma within csv should be seen as moving into a new column for a row).
    csvreader = csv.reader(csvfile, delimiter=",") 

    #Read the header row first (skip this step if there is now header) 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 

# Variables  
Profit = []
Months = []
Monthly_Change = []


    #Read each row of data after the header
    for row in csvreader:
        Profit.append(int(rows [1])) 
        Months.append(rows[0])

    #Find Monthly change 
    for x in range(1, len(Profit)):
        Monthly_Change.append((int(Profit[x])- int(Profit[x-1]))) 
