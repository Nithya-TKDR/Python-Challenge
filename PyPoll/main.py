"""
Short Description: This is a Python script aimed at modernizing the voting for a small rural town.
    Input: The script takes in election dataset as input in the form of a CSV file that is composed of three columns (Ballot ID, County and Candidate Name). 
    Output: The script produces an output both on the terminal and a separate TXT file the following based on the analysis of the election data:
        1) The total number of votes cast
        2) A complete list of candidates who received votes
        3) The percentage of votes each candidate won
        4) The total number of votes each candidate won and
        5) The winner of the election based on popular vote
"""
# Import the desired modules for the script to work properly
# Module to allow for operating system operations for file handling
import os
# Module to allow for Reader method to be used with CSV files
import csv

# Set the file handle for the input CSV file - this is in a folder called Resources that is at the same level as this script
# Generate the full path to the directory and use absolute path to remove just the filename prior to creating the entire path
election_data_csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Resources','election_data.csv')

# Initiatize the total number of votes cast in the election
# Based on the CSV file, each Ballot ID corresponds to a single vote cast and is the total number of rows (barring the header) in the file
totalvotes = 0
# Initialize a dictionary data structure to store (candidate name, votes per candidate) as key-value pairs
votespercandidate = {}

# Open the CSV file with election data using the CSV Reader
with open(election_data_csv_file, newline='') as csvfile:
# Specify delimiter and set the CSV Reader variable to hold contents from each row of the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the CSV File Header and store the contents in a separate variable
    csvheader = next(csvreader)
# Read each subsequent row of the CSV file after the header
    for row in csvreader:
# Count the running total of the number of votes cast
        totalvotes = totalvotes + 1
# Store the votes cast per candidate as a key-value pair within the dictionary based on the candidate name read from the CSV file
        if row[2] not in votespercandidate:
            votespercandidate[row[2]] = 1
        else:
            votespercandidate[row[2]] = votespercandidate[row[2]] + 1

# Print the election results to the terminal with the desired formating
# Convert values to string as appropriate prior to printing
print("--------------------------------")
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(totalvotes))
print("--------------------------------")

# Use the items dictionary method to compute the percent of votes won by each candidate
# Format the percent of votes won by each candidate to 3 decimal places
for candidate, votes in votespercandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalvotes) + "  (" + str(votes) + ")")
# Print the election winner based on the popular vote
# Use the get dictionary method in combination with max function to determine the election winner
electionwinner = max(votespercandidate, key=votespercandidate.get)
print("--------------------------------")
print("Winner: " + electionwinner)
print("--------------------------------")

# Write the above output with formating to a separate TXT file in a sibling folder
# Set the file handle for the output file - Change Directory to the path relative to the directory where the file needs to be created
os.chdir(os.path.dirname(__file__))

# Create the desired TXT file in a write mode to write the output
with open('Analysis/election_results.txt','w') as output_text:
    output_text.write("---------------------------------------\n")
    output_text.write("Election Results\n")
    output_text.write("---------------------------------------\n")
    output_text.write("Total Votes: " + str(totalvotes) + "\n")
    output_text.write("---------------------------------------\n")
# Use the items dictionary method to compute the percent of votes won by each candidate
# Format the percent of votes won by each candidate to 3 decimal places
    for candidate, votes in votespercandidate.items():
        output_text.write(candidate + ": " + "{:.3%}".format(votes/totalvotes) + "  (" + str(votes) + ")")
        output_text.write('\n')
# Print the election winner based on the popular vote
# Use the get dictionary method in combination with max function to determine the election winner
    electionwinner = max(votespercandidate, key=votespercandidate.get)
    output_text.write("--------------------------------\n")
    output_text.write("Winner: " + electionwinner + "\n")
    output_text.write("--------------------------------\n")