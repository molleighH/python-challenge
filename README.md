# Module 3 Challenge: Python-Challenge  

# Python Challenge: PyBank and PyPoll

Welcome to the Python Challenge! This project showcases my ability to transition from Excel-based data analysis to leveraging Python for more powerful and efficient data processing. In this challenge, I will apply my newly developed Python scripting skills to analyze financial and election data through two specific tasks: PyBank and PyPoll.

## Project Overview

This assignment consists of two distinct Python challenges, each addressing a real-world scenario where Python scripting proves invaluable:

- **PyBank:** A financial data analysis task aimed at evaluating a company's financial records.
- **PyPoll:** A voting data analysis task designed to modernize a small town's vote-counting process.

## Repository Structure

- **`PyBank/`**
  - **`main.py`**: The primary Python script for financial data analysis.
  - **`Resources/`**: Contains the `budget_data.csv` file used for the analysis.
  - **`analysis/`**: Includes the output text file with the results of the analysis.
  
- **`PyPoll/`**
  - **`main.py`**: The primary Python script for election data analysis.
  - **`Resources/`**: Contains the `election_data.csv` file used for the analysis.
  - **`analysis/`**: Includes the output text file with the election results.
  
- **`README.md`**: This file, providing an overview and detailed instructions for the project.

## PyBank Instructions

In PyBank, the goal is to analyze a company's financial records provided in the `budget_data.csv` file. The dataset contains two columns: "Date" and "Profit/Losses". The Python script will perform the following analyses:

1. **Total Months:** Calculate the total number of months included in the dataset.
2. **Net Total Amount:** Compute the net total amount of "Profit/Losses" over the entire period.
3. **Average Change:** Determine the average of the changes in "Profit/Losses" over the period.
4. **Greatest Increase in Profits:** Identify the date and amount of the greatest increase in profits.
5. **Greatest Decrease in Profits:** Identify the date and amount of the greatest decrease in profits.

The final script will print the results to the terminal and export them to a text file.

## PyPoll Instructions

In PyPoll, the task is to assist in modernizing a rural town's vote-counting process using the `election_data.csv` file, which contains three columns: "Voter ID", "County", and "Candidate". The Python script will calculate:

1. **Total Votes:** The total number of votes cast.
2. **Candidates:** A complete list of candidates who received votes.
3. **Vote Percentage:** The percentage of votes each candidate won.
4. **Total Votes per Candidate:** The total number of votes each candidate won.
5. **Election Winner:** The candidate who won the election based on the popular vote.

Similar to PyBank, the script will output the results to both the terminal and a text file.


## SOURCES 
- Bootcamp Powerpoint Lectures
- Professor and TA answering questions during office hours
- Slack Questions & Answers  
- https://www.programiz.com/python-programming/methods/built-in/int  
- https://www.w3schools.com/python/ref_func_len.asp  
- https://realpython.com/python-append/  
- https://www.programiz.com/python-programming/methods/list/append  
- https://www.programiz.com/python-programming/methods/built-in/len  
- https://python-reference.readthedocs.io/en/latest/docs/operators/addition_assignment.html  
- https://careerkarma.com/blog/python-operator/  
- https://www.programiz.com/python-programming/methods/list/index  
- https://www.programiz.com/python-programming/methods/built-in/str  
- https://www.datacamp.com/tutorial/f-string-formatting-in-python  
- https://www.scaler.com/topics/python/how-to-write-a-file-in-python/  
- https://www.idtech.com/blog/what-is-n-in-python  
- https://www.programiz.com/python-programming/input-output-import#google_vignette  
- https://realpython.com/python-counter/#:~:text=Counter%20is%20a%20subclass%20of,argument%20to%20the%20class's%20constructor.
- https://runestone.academy/ns/books/published/fopp/SimplePythonData/UpdatingVariables.html
- https://www.askpython.com/python/string/print-format-3f
- https://cs.stanford.edu/people/nick/py/python-print.html#:~:text=The%20Python%20print()%20function%20takes%20in%20any%20number%20of,'%5Cn'%20and%20nothing%20else.
