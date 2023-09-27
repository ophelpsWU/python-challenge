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

    # read each line in the csv and pull out important information
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

# calculate the average
average = round(totalPL / icount,2)

# assemble the output string for the analysis
strOutput = "Financial Analysis\n----------------------------"
strOutput += "\nTotal Months: " + str(icount) 
strOutput += "\nTotal: $" + str(totalPL) 
strOutput += "\nAverage Change: $" + str('{0:.2f}'.format(average))
strOutput += "\nGreatest Increase in Profits: " + maxMonth + " (" + str(maxPL) + ")" 
strOutput += "\nGreatest Decrease in Profits: " + minMonth + " (" + str(minPL) + ")"


# write the output string to a file
output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, "w") as outfile:
    outfile.write(strOutput)

#print the output string
print(strOutput)
