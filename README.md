#Module 3 Challenge: Python-Challenge  

SOURCES  

Bootcamp Powerpoint Lectures,  
Professor and TA answering questions during office hours,  
Slack Questions & Answers  

https://www.programiz.com/python-programming/methods/built-in/int
https://www.w3schools.com/python/ref_func_len.asp
https://realpython.com/python-append/
https://www.programiz.com/python-programming/methods/list/append
https://www.programiz.com/python-programming/methods/built-in/len
https://python-reference.readthedocs.io/en/latest/docs/operators/addition_assignment.html
https://careerkarma.com/blog/python-operator/
https://www.programiz.com/python-programming/methods/list/index
https://www.programiz.com/python-programming/methods/built-in/str
https://www.datacamp.com/tutorial/f-string-formatting-in-python
https://www.scaler.com/topics/python/how-to-write-a-file-in-python/
https://www.idtech.com/blog/what-is-n-in-python
https://www.programiz.com/python-programming/input-output-import#google_vignette



PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

Hints and Considerations
Consider what you've learned so far. You've learned how to import modules like csv. You’ve learned how to read and write files in various formats. You’ve learned how to store content in variables, lists, and dictionaries. You’ve learned how to iterate through basic data structures. And you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.

The datasets for these Challenges are quite large. This was done purposefully to showcase one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more powerful options for handling big data.

Write one script for each of the provided datasets. Run each script separately to make sure that the code works for its respective dataset.

Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

Requirements
Correctly Reads in the CSV (10 points)
Reads in the CSVs for both PyBank and PyPoll using Python (5 points)

Successfully stores the header row (5 points)

Results Printed out to correctly to terminal (40 points)
Results correctly display for PyBank:

Total Months (5 points)

Total (5 points)

Average Change (5 points)

Greatest Increase (5 points)

Greatest Decrease (5 points)

Results correctly display for PyPoll:

Total Votes (5 points)

Each candidate’s total votes and percent of votes (5 points)

Winner (5 points)

Code Runs Error Free (10 points)
Error Free (5 points)

Producing consistent results (5 points)

Exports results to text file (30 points)
The text file contains for PyBank:

Total Months (2.5 points)

Total (2.5 points)

Average Change (5 points)

Greatest Increase (5 points)

Greatest Decrease (5 points)

The text file contains for Pypoll:

Total Votes (2.5 points)

Each candidate’s total votes and percent of votes (2.5 points)

Winner (5 points)

Code is cleaned and commented (10 points)
Has additional tests and debugging removed (5 points)

Commented (5 points)
