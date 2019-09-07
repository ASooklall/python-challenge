import os
import csv

voteid = []
candidatelist = set([])
candidatevotes = []

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
#    * The total number of votes cast
    for row in csvreader:
        voteid.append(row)
#   * A complete list of candidates who received votes
        candidatevotes.append(row[2])
        candidatelist.add(row[2])

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   ------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------


def vartext(statement):
        print(f'{statement}')
        newfile.write(f'{statement}\n')
        return

newfile = open("poll_analysis.txt","w+")

bestcandidate = 0

vartext("Election Results")
vartext("-"*30)
vartext(f'Total Votes: {len(voteid)}')
vartext("-"*30)
for candidate in candidatelist:
        vartext(f'{candidate}: {round((candidatevotes.count(candidate) / len(voteid) * 100))}% ({candidatevotes.count(candidate)})')
        if round((candidatevotes.count(candidate))) > bestcandidate:
                winner = candidate
                bestcandidate = int(candidatevotes.count(candidate))
vartext("-"*30)
vartext(f'Winner: {(winner)}')
vartext("-"*30)

newfile.close()
