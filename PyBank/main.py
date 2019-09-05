import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
months = []
total = []
change = []
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    data = list(csv.reader(csvfile, delimiter=','))

#  Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
    for row in data:
        months.append(row)


#   * The net total amount of "Profit/Losses" over the entire period
    # for profits in csvreader:
        total.append(int(row[1]))


#   * The average of the changes in "Profit/Losses" over the entire period
for values in range(len(total)):
    net = 0
    if values == 0:
        net = total[values]
        # change.append(net)
    else:
        net = total[values]-total[values-1]
        change.append(net)
def avg(change):
    return sum(change) / len(change)       


#   * The greatest increase in profits (date and amount) over the entire period

greatestprofit = max(change)
for i in range(len(change)):
    if change[i] == greatestprofit:
        monthprofit = data[i+1][0]


#   * The greatest decrease in losses (date and amount) over the entire period
greatestloss = (min(change))
for i in range(len(change)):
    if change[i] == greatestloss:
        monthloss = data[i+1][0]



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

def analysis():
        print("Financial Analysis")
        print("-"*30)
        print(f"Total Months: {len(months)}")
        print(f"Total: ${sum(total)}")
        print(f"Averange Change: ${avg(change)}")
        print(f"Greatest Increase in Profits: {monthprofit} (${greatestprofit})")
        print(f"Greatest Decrease in Profits: {monthloss} (${greatestloss})")

analysis()


# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

newfile = open("budget_data.txt","w+")
newfile.write(analysis())
newfile.close()