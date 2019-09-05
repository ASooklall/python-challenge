import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
months = []
total = []
change = []
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

# print(f'{avg(change)}')
#  Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
    for row in csvreader:
        months.append(row)


#   * The net total amount of "Profit/Losses" over the entire period
    # for profits in csvreader:
        total.append(int(row[1]))


#   * The average of the changes in "Profit/Losses" over the entire period
for values in range(len(total)):
    net = 0
    if values == 0:
        net = total[values]
        change.append(net)
    else:
        net = total[values]-total[values-1]
        change.append(net)
def avg(change):
    return sum(change) / len(change)       



#   * The greatest increase in profits (date and amount) over the entire period
greatestprofit = max(change)
# monthprofit = 


#   * The greatest decrease in losses (date and amount) over the entire period
greatestloss = (min(change))
# monthloss = 



# * As an example, your analysis should look similar to the one below:
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

monthprofit = "temp"
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total)}")
print(f"Averange Change: ${avg(change)}")
print(f"Greatest Increase in Profits: {monthprofit} (${greatestprofit})")
print(f"Greatest Decrease in Profits: {monthprofit} (${greatestloss})")


# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# write.txt


# print(average(total))