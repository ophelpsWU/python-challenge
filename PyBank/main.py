import os
import csv

# Get the path to the csv to read
csvpath = os.path.join("Resources", "budget_data.csv")

# create variables
totalPL = 0
totalDelta = 0
icount = 0
maxDelta = 0
minDelta = 0
prevPL = 0
delta = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # read each line in the csv and pull out important information
    for row in csvreader:
        icount +=1
        linePL = int(row[1])
        
        if icount == 1:
            totalDelta -= linePL
        else:
            delta = linePL - prevPL

        totalPL+=linePL
        if minDelta > delta:
            minMonth = row[0]   
            minDelta = delta
        if maxDelta < delta:
            maxDelta = delta
            maxMonth = row[0]
        prevPL = int(row[1])

# calculate the average
totalDelta += prevPL

average = round(totalDelta / (icount - 1),2)

# assemble the output string for the analysis
strOutput = "Financial Analysis\n----------------------------"
strOutput += "\nTotal Months: " + str(icount) 
strOutput += "\nTotal: $" + str(totalPL) 
strOutput += "\nAverage Change: $" + str('{0:.2f}'.format(average))
strOutput += "\nGreatest Increase in Profits: " + maxMonth + " (" + str(maxDelta) + ")" 
strOutput += "\nGreatest Decrease in Profits: " + minMonth + " (" + str(minDelta) + ")"


# write the output string to a file
output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w") as outfile:
    outfile.write(strOutput)

#print the output string
print(strOutput)
