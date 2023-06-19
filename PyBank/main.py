import os
import csv

CSV_PATH = os.path.join('Resources', 'budget_data.csv')
OUTPUT_PATH = os.path.join('analysis', 'budget_analysis.txt')
MONTH_INDEX = 0
PROFIT_INDEX = 1

month_count = 0
month_of_change_list = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
net_total= 0
profit_changes= 0

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvreader)
    first_row = next(csvreader)
    month_count += 1
    net_total += int(first_row[1])
    profit_changes = int(first_row[1])

    for row in csvreader:
        #print(row)
        month_count += 1

        #current_profit = int(row[PROFIT_INDEX])
        net_total += int(row[1])
        net_change = int(row[1]) - profit_changes 
        
        profit_changes = int(row[1]) 

        #profit_loss_changes = int(row[PROFIT_INDEX])
        #change_list.append(profit_loss_changes-profit_changes)
        #print(profit_changes)
        
        net_change_list += [net_change] 
        month_of_change_list += [row[0]]

        #Calculate the greatest increase
        if net_change > greatest_increase [1]: 
            greatest_increase [0] = row[0]
            greatest_increase [1] = net_change

        #Calculate the greatest decrease 
        if net_change < greatest_decrease [1]: 
            greatest_decrease [0] = row[0]
            greatest_decrease [1] = net_change
        
average_change = sum(net_change_list) / len(net_change_list)

output = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {month_count}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

# print("Total Months: " + str(int(month_count)))
# print("Total: " + '$'+str(int(net_total)))
# print("Average Change: " + '$' + str(int(average_change)))
# print("Greatest Increase in Profits: " + str(greatest_increase))
# print("Greatest Decrease in Profits: " + str(greatest_decrease))

#Export the results to the text file
with open ("analysis/analysis.txt", "w") as file:
    file.write(output)
    


