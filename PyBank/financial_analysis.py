import csv
import os

# Get the path to the data file we will read from (renamed for simplicity)
path_read = os.path.join("Resources", "budget_data.csv")

#Get the path for the data file we will write the results on
path_write = os.path.join("Resources", "results.txt")

# Declare the variables that we will need to keep track of as we analyze the data
num_months = 0
total_profit = 0

# Store the greatest increase and loss in a dict to keep both amount and date easily accesible
greatest_increase = {"Date" : "", "Profit" : 0}
greatest_decrease = {"Date": "", "Loss": 0}

with open(path_read, "r") as csv_file:

    data = csv.reader(csv_file)
    header = next(data)

    # Each line in the csv contains the data for one month.

    # This variable indicates that we are on the first line
    first = True

    for line in data:

        # Get the information contained in the line
        date = line[0]
        profit = float(line[1])

        #Check if it is the first line, and if so, save the first profit listed
        if first:
            first_profit = profit

            # Change the variable to indicate we're no longer in the first line
            first = False

        # Update number of months and total profit
        num_months += 1
        total_profit += profit

        #Check if we need to update greatest increase or loss
        if profit > 0 and profit > greatest_increase["Profit"]:
            greatest_increase["Date"] = date
            greatest_increase["Profit"] = profit
        
        elif profit < 0 and profit < greatest_decrease["Loss"]:
            greatest_decrease["Date"] = date
            greatest_decrease["Loss"] = profit
    
    # Now get the profit from the last line
    last_profit = float(line[1])

# Finally, calculate average change. The sum of all the changes is equal to the last entry minus the first one.
# So, for N profits x_1, x_2, x_3, ...., x_N we have (x_2 - x_1) + (x_3 - x_2) + ... + (x_N - x_(N-1))
# All the terms cancel except for x_N - x_1.
# The number of changes that happen is equal to the number of months minus one. So the average becomes:

average_change = (last_profit - first_profit)/(num_months - 1)

# Write all the results to a file
with open(path_write, "w") as txt_file:

    # Print to file so that each sentence will be written in a new line (with no extra spaces)
    print("Financial analysis:", file = txt_file)
    print("-------------------------------- \n", file = txt_file)
    print(f"Total months: {num_months}", file = txt_file)
    print(f"Total profit: ${total_profit}", file = txt_file)

    # Print only 2 decimal places for the average
    print(f"Average change: ${round(average_change,2)}", file = txt_file)

    print(f"Greatest increase in profits: {greatest_increase['Date']} ---> ${greatest_increase['Profit']}", file = txt_file)
    print(f"Greatest decrease in profits: {greatest_decrease['Date']} ---> ${greatest_decrease['Loss']}", file = txt_file)

# Open the result file and output the results
with open(path_write, "r") as txt_file:
    print("\n")
    for line in txt_file:
        print(line)
    print("\n")
