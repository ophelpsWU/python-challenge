import os
import csv

# Get the path to the csv to read
csvpath = os.path.join("Resources", "budget_data.csv")

totalPL = 0
icount = 0
maxPL = 0
minPL = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        icount +=1
        linePL = int(row[1])
        totalPL+=linePL
        if minPL > linePL:
            minMonth = row[0]   
            minPL = linePL
        if maxPL < linePL:
            maxPL = linePL
            maxMonth = row[0]
average = round(totalPL / icount,2)

strOutput = "Financial Analysis\n----------------------------"
strOutput += "\nTotal Months: " + str(icount) 
strOutput += "\nTotal: $" + str(totalPL) 
strOutput += "\nAverage Change: $" + str('{0:.2f}'.format(average))
strOutput += "\nGreatest Increase in Profits: " + maxMonth + " (" + str(maxPL) + ")" 
strOutput += "\nGreatest Decrease in Profits: " + minMonth + " (" + str(minPL) + ")"

output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w") as outfile:
    outfile.write(strOutput)

print(strOutput)
