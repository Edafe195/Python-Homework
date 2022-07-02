# Import Dependencies
from pathlib import Path
import csv 

# File location through pathlib
csvpath = Path('Resources/budget_data.csv')

# iterate through specific rows for the following variables
total_months = []
total_profit = []
change_in_profit = []
 
# Open csv in read mode 
with open(csvpath, 'r') as csvfile:

     # Save contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skipping the header labels
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total_months and total_profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # To get the change in profits, we iterate through the profits in order
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        change_in_profit.append(total_profit[i+1]-total_profit[i])
        
# Obtaining the max and min of the the montly profit change list

max_increase_value = max(change_in_profit)
max_decrease_value = min(change_in_profit)

# Correlating the max and min to the proper month by using month list and index from max and min

max_increase_month = change_in_profit.index(max(change_in_profit)) + 1
max_decrease_month = change_in_profit.index(min(change_in_profit)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(change_in_profit)/len(change_in_profit),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
outpath = Path('output.txt')

with open(outpath,"w") as file:
    
# Using Write method to print to Financial_Analysis_Summary 

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change_in_profit)/len(change_in_profit),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")