import csv

file_input = "budget_data.csv"
file_output = "budget_analysis.txt"

total_months = 0
total_rev = 0
last_rev = 0
rev_change = []
month_change = []


with open(file_input) as budgetRev:
    csvreader = csv.DictReader(budgetRev)
    for row in csvreader:
        total_months += 1
        total_rev += int(row["Revenue"])
        rev_diff = int(row["Revenue"]) - last_rev
        last_rev = int(row["Revenue"])
        rev_change.append(rev_diff)
        month_change.append(row["Date"])

maxIncrease = max(rev_change)
maxIncMonth = month_change[rev_change.index(maxIncrease)]
maxDecrease = min(rev_change)
maxDecMonth = month_change[rev_change.index(maxDecrease)]
avg_rev = sum(rev_change)/len(rev_change)

output = (f"\nFinanical Analysis\n"
          f"-------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total Revenue: ${total_rev}\n"
          f"Average Revenue Change: ${round(avg_rev,2)}\n"
          f"Greatest Increase in Revenue: {maxIncMonth} (${maxIncrease})\n"
          f"Greatest Decrease in Revenue: {maxDecMonth} (${maxIncrease})\n")
print(output)

with open(file_output, "w") as txt_file:
    txt_file.write(output)
