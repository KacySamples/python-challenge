import csv
import os

# File Path
file_path = file_path = os.path.join("Resources", "election_data.csv")

# Variables
total_votes = 0
candidates = {}
winner = None

# Opens CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skips the header
    
    # Loops through each row in the CSV file
    for row in reader:
         # Extracting the candidate information
        _, _, candidate = row 
        
        total_votes += 1
        
        # Tallys up the votes 
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Determines the winner
winner = max(candidates, key=candidates.get)

# Displays the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

