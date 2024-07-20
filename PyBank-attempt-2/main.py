import os
import csv

csvpath = os.path.join('Resources-attempt-2', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    total_months = 0
    net_total = 0
    changes = []
    previous_profit_losses = None
    profit_loss_date = []

    for row in csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])

        if previous_profit_losses is not None:
            change = int(row[1]) - previous_profit_losses
            changes.append(change)
            profit_loss_date.append(row[0])

        previous_profit_losses = int(row[1])

max_index = changes.index(max(changes))
min_index = changes.index(min(changes))
max_date = profit_loss_date[max_index]
min_date = profit_loss_date[min_index]


analysis = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${sum(changes)/len(changes):.2f}\n"
    f"Greatest Increase in Profits: {max_date} (${max(changes)})\n"
    f"Greatest Decrease in Profits: {min_date} (${min(changes)})\n"
)

txtpath = os.path.join('analysis-attempt-2', 'budget_results.txt')

with open(txtpath, mode='w') as txtfile:
    txtfile.write(analysis)

print(f"PyBank analysis and results have been written to {txtpath}")
print(analysis)


