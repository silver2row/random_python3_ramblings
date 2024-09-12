#!/usr/bin/python3

# Reading from Weather.txt and making adjustments

y = 0
m = 0

#### Read in Data ####
filename = open("Weather.txt", "r")

infile = filename.read()

#### Read Line from File ####
datalist = []

for line in infile:
    date = m, y
    date = (line.split('-'))
    #### Get Data from Line ####
    m, y, h, l, r = (line.split(','), line.split(','), line.split(','), line.split(','), line.split(','))
    highTemp = str(h)
    lowTemp  = str(l)
    rainfall = str(r)
    #### Get Date Correct ####
    month = str(m)
    year  = str(y)
    date = (month, year)

    #### Put data in a List ####
    datalist.append([month, year, highTemp, lowTemp, rainfall])

# Close the File #
filename.close()

#### Analyze the Data ####
singlemonth = int(input("For the median of high-low temps and median rainfall, enter in the month of your choosing: "))
singleyear  = int(input("Enter in your favorite year, i.e. as long as it is '22, '23, or '24: "))

# Search for Historical Data #
gooddata = []
for singlemonth in datalist:
    if (singlemonth[0] == month) and (singlemonth[1] == year):
        gooddata.append([(singlemonth[2] == highTemp), (singlemonth[3] == lowTemp), (singlemonth[4] == rainfall)])

# Perform Analysis #
minsofar     = 120
maxsofar     = -100
numgooddates = 0
sumofmin     = 0
sumofmax     = 0
rainfall_One = 1
for singlemonth in gooddata:
    numgooddates += 1
    sumofmin = (singlemonth[0]) / 2
    sumofmax = (singlemonth[1]) / 2
    if (singlemonth[1]) < minsofar:
        minsofar += (singlemonth[1])
    if (singlemonth[2]) > maxsofar:
        maxsofar += (singlemonth[2])

avgLow  = sumofmax / numgooddates
avgHigh = sumofmin / numgooddates
rain_percent = rainfall_One / numgooddates * 100

#### Present the Results ####
print("There were", numgooddates - 1, "days")
print("The median low temperature on record was", maxsofar)
print("The median high temperature on record was", minsofar)
print("The average high was", avgHigh)
print("The average low was", avgLow)
print("The chance of rain during this year was", rain_percent, "%")
