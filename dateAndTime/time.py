from datetime import datetime                                # So can tell the date/time
import pytz
from difflib import SequenceMatcher


def getTime(command):

    cityList = []
    countryList = []
    timezoneList = []

    with open("../virtual-assistant/data/cities-and-full-timezones.txt") as file:
        for line in file:
            line = line[:-1].split(";")
            cityList.append(line[0])
            countryList.append(line[1])
            timezoneList.append(line[3])

    possibleCities = []
    for i in range (len(cityList)):
        if cityList[i] in command or cityList[i].lower() in command:
            possibleCities.append([cityList[i],countryList[i],timezoneList[i]])

    if(len(possibleCities) == 0):
        time = datetime.now()
        time = time.strftime("%H:%M")
        time = time.split(":")


        hour = time[0]
        mins = time[1]

        if(hour[0] == '0'):
            hour = hour[1]
        if(mins[0] == '0'):
            mins = mins[1]
        hour = int(hour)
        if(hour < 0):
            hour += 24



        return "The time is " + str(hour) + " o'clock and " + str(mins) + " minutes."

    elif(len(possibleCities) == 1):


        return findTimeGivenZone(possibleCities[0])
    else:
        return possibleCities

def findCorrectCity(command, possibleCities):
    maxRatio = 0
    currCityInfo = []

    for i in range(len(possibleCities)):
        currRatio = SequenceMatcher(None,command,possibleCities[i][0] + " " + possibleCities[i][1]).ratio()
        if(currRatio > maxRatio):
            maxRatio = currRatio
            currCityInfo = possibleCities[i]

    return findTimeGivenZone(currCityInfo)

def findTimeGivenZone(cityInfo):
    alternativeTime = pytz.timezone(cityInfo[2])
    time = datetime.now(alternativeTime)
    time = time.strftime("%H:%M")
    time = time.split(":")


    hour = time[0]
    mins = time[1]

    if(hour[0] == '0'):
        hour = hour[1]
    if(mins[0] == '0'):
        mins = mins[1]
    hour = int(hour)
    if(hour < 0):
        hour += 24


    
    return "The time in " + cityInfo[0] + " in " + cityInfo[1] + " is " + str(hour) + " o'clock and " + str(mins) + " minutes."