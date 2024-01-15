"""
Short Description: This Python script provides an analysis of the financial records of a company. 
    Input: The script takes in an input a financial dataset comprising two columns (Date, Profits/Losses) as a CSV file. 
    Output: The script produces a simple output analyzing the financial records to both the terminal and an output TXT file as below:
        1) Total number of months included in the dataset
        2) The net total amount of "Profits/Losses" over the entire period in the dataset. 
        3) The changes in "Profits/Losses" over the entire period and the average of those changes. 
        4) The greatest increase in profits (date and amount) over the entire period. 
        5) The greatest decrease in profits (date and amount) over the entire period. 
"""
# Import the desired modules for the script to work properly
# Module to allow for operating system operations for file handling
import os
# Module to allow for Reader method to be used with CSV files
import csv
# Module to enable statistical functions in the script
import statistics
# Set the file handle for the input CSV file - this is in a folder called Resources that is at the same level as this script
# Generate the full path to the directory and use absolute path to remove just the filename prior to creating the entire path
budget_data_csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Resources','budget_data.csv')
# Initialize relevant variables to be used in the calculations
total_months = 0
net_total_amount = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
best_month = ''
worst_month = ''
# Create and initialize three lists to store each of the columns in the CSV file and related calculations
dates = []
profit_loss = []
month_to_month_change = []

# Open the CSV file with election data using the CSV Reader
with open(budget_data_csv_file, newline='') as csvfile:
# Specify delimiter and set the CSV Reader variable to hold contents from each row of the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the CSV File Header and store the contents in a separate variable
    csvheader = next(csvreader)
# Read each subsequent row of the CSV file after the header
    for row in csvreader:
# Use the APPEND method to store all dates in the CSV file and the corresponding "Profit/Loss" values in two separate lists
        dates.append(row[0])
        profit_loss.append(int(row[1]))

# Calculate the total months in the dataset
total_months = len(dates)
# Count the total amount based on the second column of the CSV file
i = 0
for i in profit_loss:
    net_total_amount = net_total_amount + int(i)
# Track monthly changes to compute the average of the changes over the entire dataset
# Use RANGE function in combination with a FOR loop for the above
i = 0
for i in range(len(profit_loss) - 1):
    delta = (int(profit_loss[i+1]) - int(profit_loss[i]))
# Use the APPEND method to add the monthly change to the related list
    month_to_month_change.append(delta)
# Compute the average of the changes over the entire period
average_change = statistics.mean(month_to_month_change)

# Iteratively calculate the greatest increase and decrease in profits using MAX and MIN functions on the list storing the monthly differences
greatest_increase_profits = max(month_to_month_change)
greatest_decrease_profits = min(month_to_month_change)

# Use the INDEX function to find the dates corresponding to the greatest increase and decrease within the dataset
greatest_increase_index = month_to_month_change.index(greatest_increase_profits)
greatest_decrease_index = month_to_month_change.index(greatest_decrease_profits)

# Find the corresponding best and worst months based on the indices computed above
best_month = dates[greatest_increase_index + 1]
worst_month = dates[greatest_decrease_index + 1]

# Print the analysis of the financial dataset to the terminal with the desired formating
# Convert values to string where applicable prior to printing
print("--------------------------------")
print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total_amount))
# Format the average change to two decimal places as desired in the output
print("Average Change is: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + str(best_month) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(greatest_decrease_profits) + ")")

# Write the above output with formating to a separate TXT file in a sibling folder
# Set the file handle for the output file - Change Directory to the path relative to the directory where the file needs to be created
os.chdir(os.path.dirname(__file__))

# Create the desired TXT file in a write mode to write the output
with open('Analysis/financial_analysis.txt','w') as output_text:
    output_text.write("---------------------------------------\n")
    output_text.write("Financial Analysis\n")
    output_text.write("---------------------------------------\n")
    output_text.write("Total Months: " + str(total_months) + "\n")
    output_text.write("Total: $" + str(net_total_amount) + "\n")
    output_text.write("Average Change is: $" + str(round(average_change, 2)) + "\n")
    output_text.write("Greatest Increase in Profits: " + str(best_month) + " ($" + str(greatest_increase_profits) + ")\n")
    output_text.write("Greatest Decrease in Profits: " + str(worst_month) + " ($" + str(greatest_decrease_profits) + ")\n")
    output_text.write("---------------------------------------\n")