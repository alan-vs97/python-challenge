import csv
import os

# Path to file (renamed for simplicity)
path_read = os.path.join("Resources", "election_data.csv")
path_write = os.path.join("Resources", "election_results.txt")

# Create empty dict to keep track of votes
candidates = {}

with open(path_read) as csv_file:
    csv_read = csv.reader(csv_file)
    header = next(csv_read)
    for line in csv_read:
        # Each line is a vote for a candidate
        candidate = line[2]

        # Check if the candidate is already in the candidates dict.
        # Here we assume the candidate names are always spelled the same way.
        if candidate in candidates.keys():
            # If it is, update the vote count
            candidates[candidate] += 1
        else:
            # If it's not, start from one
            candidates[candidate] = 1

# Get the key whose value is the largest in the dictionary:
winner = max(candidates, key = candidates.get)

# Calculate the total number of votes cast
total_votes = sum(candidates.values())

with open(path_write, "w") as txt_file:

    # Print to file so that each sentence will be written in a new line (with no extra spaces)
    print("Election results", file = txt_file)
    print("---------------------------------", file = txt_file)
    print(f"Total votes: {total_votes}", file = txt_file)
    print("---------------------------------", file = txt_file)

    # Iterate over the dictionary to automatically print all the key-value pairs
    for key in candidates:
        #Calculate percentage of the votes
        percent = 100*candidates[key]/total_votes

        print(f"{key}: {round(percent,2)} % ({candidates[key]})", file = txt_file)
    
    print("---------------------------------", file = txt_file)
    print(f"Winner: {winner}", file = txt_file)
    print("---------------------------------", file=txt_file)

# Open the result file and output the results
with open(path_write, "r") as txt_file:
    print("\n")
    for line in txt_file:
        print(line)
    print("\n")
