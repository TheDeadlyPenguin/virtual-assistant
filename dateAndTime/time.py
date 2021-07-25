from datetime import datetime                                # So can tell the date/time

def getTime():
    now = datetime.now()
    dt_string = str(now.strftime("%d/%B/%Y %H:%M:%S"))
    time = (dt_string.split())[1] # Break date and time into a list with two elements - we need the second one
    time = time.split(':')
    for i in range(len(time)):
        if time[i][0] == '0':
            time[i] = time[i][1]
    return "The time is " + time[0] + " o'clock and " + time[1] + " minutes"

def getTimezoneOffsetAndName(command,currentCity):
    cityList = []
    timezoneNameList = []
    timezoneGMTList = []

    city_name = ""
    zone_name = ""
    zone_offset = ""

    with open("../virtual-assistant/data/cities-and-full-timezones.txt") as file:
        for line in file:
            line = line[:-1].split(";")
            cityList.append(line[0])
            timezoneNameList.append(line[1])
            timezoneGMTList.append(line[2])


    command = command.split()
    for i in range (len(cityList)):
        if cityList[i] in command or cityList[i].lower() in command:
            city_name = cityList[i]
            zone_name = timezoneNameList[i]
            zone_offset = timezoneGMTList[i][3:]
    
    if(city_name == ""):
        city_name = currentCity
        # for i in range(len(cityList)):
        #     if(cityList[i] == currentCity):
        #         zone_name = timezoneNameList[i]
        #         zone_offset = timezoneGMTList[i]
    

    cityNameAndTimezoneInfo = []
    cityNameAndTimezoneInfo.append(city_name)
    cityNameAndTimezoneInfo.append(zone_name)
    cityNameAndTimezoneInfo.append(zone_offset)
    return cityNameAndTimezoneInfo

def getTimeWithZoneInfo(cityInfo,time):
    hour = int(time.split()[3])
    mins = int(time.split()[6])

    print(hour)
    print(mins)
    print(cityInfo)

    if(cityInfo[1] != ""):
        cityName = cityInfo[0]
        zoneName = cityInfo[1]
        GMTOffset = cityInfo[2]

        hourOffset = 0
        minsOffset = 0

        if(GMTOffset[0] == "+"):  
            if not (":" in GMTOffset):
                hourOffset = int(GMTOffset[1:])
            else:
                GMTOffset = GMTOffset[1:].split(":")
                hourOffset = int(GMTOffset[0])
                minsOffset = int(GMTOffset[1])
            hour += hourOffset
            mins += minsOffset
        elif(GMTOffset[0] == "-"):  
            if not (":" in GMTOffset):
                hourOffset = int(GMTOffset[1:])
            else:
                GMTOffset = GMTOffset[1:].split(":")
                hourOffset = int(GMTOffset[0])
                minsOffset = int(GMTOffset[1])
            hour -= hourOffset
            mins -= minsOffset

        # To avoid overflow
        if(mins >= 60):
            mins -= 60
            hour += 1
        elif(mins < 0):
            mins += 60
            hour -= 1
            if(hour < 0):
                hour += 24
        if(hour >= 24):
            hour -= 24
        elif(hour < 0):
            hour += 24
        

        return cityName + " is in the " + zoneName + " timezone so the time there right now is " + str(hour) + "hours and " + str(mins) + "minutes."
    else:
        return "The time in " + cityInfo[0] + " is " + str(hour) + "hours and " + str(mins) + "minutes."

