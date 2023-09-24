import csv

# File path, yes I am aware this is incredibly long. But that's where I want to put it. 
file_path = r"C:\Users\sampl\OneDrive\Desktop\Data_Analytics\Week3Python\Module3Challenge\python-challenge\PyBank\Resources\budget_data.csv"

# Initialize variables
total_months = 0
total_profit_losses = 0
prev_profit_losses = None
changes = []
greatest_increase = {'Date': None, 'Amount': float('-inf')}
greatest_decrease = {'Date': None, 'Amount': float('inf')}

# Opens CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    # This skips the header
    next(reader)  
    
    # Loop through each row in the CSV file
    for row in reader:
        date, profit_losses = row
        profit_losses = int(profit_losses)
        
        total_months += 1
        total_profit_losses += profit_losses
        
        if prev_profit_losses is not None:
            change = profit_losses - prev_profit_losses
            changes.append(change)
            
            if change > greatest_increase['Amount']:
                greatest_increase = {'Date': date, 'Amount': change}
            if change < greatest_decrease['Amount']:
                greatest_decrease = {'Date': date, 'Amount': change}
        
        prev_profit_losses = profit_losses

# Calculates average change
avg_change = sum(changes) / len(changes)

# Displays the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})")