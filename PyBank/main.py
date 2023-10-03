#REMINDER: to create a folder in GitHub use "/" at the end of the folder name to transform into a folder

#First, import os module - allows to create file path across operating systems 
import os 

#Import module for reading csv files & set correct path to csv files 
import csv 
csvpath = os.path.join("Users", "molleighhughes", "Desktop", "MSU DATA ANALYSIS", "Module 3 Challenge", "Starter_Code", "PyBank", "Resources")

#Translate csv opening in Python 
with open(csvpath) as csvfile: 

  #csv reader specifies delimiter (parameter tells Python each comma within csv should be seen as moving into a new column for a row) and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=",") 

  print(csvreader)

  #Read the header row first (skip this step if there is now header) 
  csv_header = next(csvreader)
  print(f"CSV Header: {csv_header}") 

  #Read each row of data after the header 
  for row in csvreader:
      print(row) 
