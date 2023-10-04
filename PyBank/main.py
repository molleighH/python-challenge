#First, import os module - allows to create file path across operating systems 
import os 

#Import module for reading csv files & set correct path to csv files 
import csv 
budget_data = os.path.join("PyBank", "budget_data.csv")

#Translate csv opening in Python 
with open(budget_data, newline="") as csvfile: 

    #csv reader specifies delimiter (parameter tells Python each comma within csv should be seen as moving into a new column for a row).
    csvreader = csv.reader(csvfile, delimiter=",") 

    #Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 

    #Set Variables  
    Months = []
    Profits = [] 

    #Read each row of data after the header
    #append() = method adds an item to the end of the list = list.append(item); append() is single arguement; item parameter: an item (number, sting, list, etc.) to be added at the end of the list 
    #int() = int(value, base [optional]) ; value parameter: any numberic-string, bytes-liek object or a number; base parameter: the number system the value is currently in
    for row in csvreader:
        Profit.append(int(rows [1])) 
        Months.append(rows[0])

    #Set Monthly_Change 
    Monthly_Change = []

    #Find Monthly_Change
    #len() + function returns the number of items (length) in an object = len(s); function takes a single arguement (s), which can be a sequence(= string, bytes, tuples, list, range) OR collection(= dictionary, set, frozen set) 
    for x in range(1, len(Profit)):
        Monthly_Change.append((int(Profit[x]) - int(Profit[x-1]))) 

    #Calculate average monthly_change
    Average_Monthly_Change = sum(Monthly_Change)/ len(Monthly_Change)
    Monthly_Average = round(Average_Monthly_Change, 2)

    #Calculate total number of months included in the dataset 
    Total_Months = len(Months)

    #Calculate greatest increase in Profit 
    Greatest_Increase = max(Monthly_Change)

    #Calculate greatest decrease in Profit 
    Greatest_Decrease = min(Monthly_Change)

    
    
