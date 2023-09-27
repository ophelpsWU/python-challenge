import os
import csv

# Get the path to the csv to read
csvpath = os.path.join("Resources", "election_data.csv")

icount = 0
candidates = dict()

strOutput = "Election Results"
strLine = "\n-------------------------"

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # read each line in the csv and pull out important information
    for row in csvreader:
        icount +=1
        if row[2] in candidates:
            candidates[row[2]]+=1
        else:
            candidates[row[2]]=1

maxVotes = 0

#create the output string of the analysis
strOutput += strLine
strOutput += "\nTotal Votes: " + str(icount)
strOutput += strLine

#for each candidate, compute a percentage of the vote; also store the winner
for person in candidates:
    strOutput += "\n" + person + ": "
    votepercent = round(candidates[person] * 100/icount,3)
    strOutput += str(votepercent) + "% (" + str(candidates[person]) + ")"
    if maxVotes < candidates[person]:
        maxVotes = candidates[person]
        winner = person

strOutput += strLine
strOutput += "\nWinner: " + winner
strOutput += strLine

# write the output string to a file
output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w") as outfile:
    outfile.write(strOutput)

#print the output string
print(strOutput)
