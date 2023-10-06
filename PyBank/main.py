#Import os module & module for reading CSVfiles 
import os 
import csv 

#CSV File Path &  create object out of CSV File 
budget_data = os.path.join("PyBank", "budget_data.csv")

Profits = [] 
Dates = []
Total_Months = 0
Total_Profit = 0
Value = 0 
Change = 0 

#Open & read the CSV file 
with open(budget_data, newline="") as csvfile:
    cvsreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row
    csv_header = next(cvsreader)

    #Iterate through First Row & assign results to variable 
    First_Row = next(cvsreader) 
    Total_Months += 1
    Total_Profit += int(First_Row[1])
    Value = int(First_Row[1])

    #Read through each row after header & first row 
    for row in cvsreader: 
        
        #Place holder
        Dates.append(row[0])

        #Calculate Change and then add to new list  
        Change = int(row[1])-Value
        Profits.append(Change)
        Value = int(row[1])

        #Calculate the Total Number of Months 
        Total_Months = len(Dates)
        Total_Months += 1

        #Calculate net amount of Profit over entire period 
        Total_Profit = Total_Profit + int(row[1]) 

    #Calculate Greatest increase in Profits (date and amount over entire period)
    Greatest_Increase = max(Profits) 
    Greatest_Index = Profits.index(Greatest_Increase)
    Greatest_Date = Dates[Greatest_Index]

    #Calculate Greatest decrease in Profits (date and amount over entire period)
    Greatest_Decrease = min(Profits)
    Lowest_Index = Profits.index(Greatest_Decrease)
    Lowest_Date = Dates[Lowest_Index]

    #Calculate average Profit Change
    Average_Profit_Change = sum(Profits)/len(Profits)

#Print results 
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(Total_Months)}")
print(f"Total : ${str(Total_Profit)}")
print(f"Average Change: ${str(round(Average_Profit_Change, 2))}")
print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})")

#Specifiy the file to write to (tells ython the file to write to while assigning it to the variable output_path)
output_path = os.path.join("PyBank", "analysis")

#Open the file using "write" mode. Spicify the variabble to hold the contents (tells Python to open the file by using write mode, while holding the contents in output_path)
with open(output_path, "w") as csvfile:

    #Initialize csv.writer (tells Python that this application will write code into an external CSV file)
    csvwriter = csv.writer(csvfile)

    #Write the first row (column headers) [csv.writerow is the code to write a new row into a CSV file]
    csvwriter.writerow(["Financial Analysis"])

    #Write the second row, etc 
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(str(f"Total Months: {str(Total_Months)}"))
    csvwriter.writerow(str(f"Total: ${str(Total_Profit)}"))
    csvwriter.writerow(str(f"Average Change: ${str(round(Average_Profit_Change))}"))
    csvwriter.writerow(str(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})"))
    csvwriter.writerow(str(f"Greatest Decrease in Profits: {Lowest_Date} (${str(Greatest_Decrease)})"))
