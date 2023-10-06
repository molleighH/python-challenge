#Import os module & module for reading CSVfiles 
import os 
import csv 

#CSV File Path &  create object out of CSV File 
election_data = os.path.join("PyPoll", "election_data.csv")

#Capture Candidates in a list, #  of votes per Candidate, percentage of total votes each Candidate wins, total number of votes 
Candidates = []
Vote_Count = []
Vote_Percentage = []
Total_Votes = 0 

#Open & read CSV file 
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)

    for row in csvreader: 
        
        #Increment counter by 1s 
        Total_Votes += 1 

        if row[2] not in Candidates:
            Candidates.append(row[2])
            Index = Candidates.index(row[2])
            Vote_Count.append(1)
        else:
            Index = Candidates.index(row[2])
            Vote_Count[Index] += 1

    #For each vote, change the Vote Percentage [%.3f %SOME_NUMBER = format specifier to format floating-point numbers to display only three decimal places; 3 = number of decimal places ]
    for Votes in Vote_Count:
        Percentage = (Votes/Total_Votes) * 100
        Percentage = "%.3f%%" % Percentage
        Vote_Percentage.append(Percentage)
            
    #Who is the winning Candidate?
    Winner = max(Vote_Count)
    Index = Vote_Count.index(Winner)
    Candidate_Winner = Candidates[Index] 

#Print Results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(Total_Votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f" {Candidates[i]} : {str(Vote_Percentage[i])} {str(Vote_Count[i])}")
print("--------------------------")
print(f"Winner: {Candidate_Winner}")
print("--------------------------")


#Export. Specifiy the file to write to 
output_path = os.path.join("PyPoll", "analysis")

#Open the file using "write" mode.
with open(output_path, "w") as csvfile:

    #Initialize csv.writer (tells Python that this application will write code into an external CSV file)
    csvwriter = csv.writer(csvfile)

    #Write the each row 
    csvwriter.writerow("Election Results")
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(str(f"Total Votes: {str(Total_Votes)}"))
    csvwriter.writerow(["----------------------------"])
    for i in range(len(Candidates)):
        csvwriter.writerow(f"(Candidates[i]: {str(Vote_Percentage[i]({str(Vote_Count[i])}))}")
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(f"Winner: {Candidate_Winner}")
    csvwriter.writerow(["----------------------------"])
