import requests, json

def getTimeGivenZone(GMTOffset, currTime):

    hour = int(currTime.split()[3])
    mins = int(currTime.split()[6])

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
    if(hour >= 24):
        hour -= 24

    updatedTime = []
    updatedTime.append(hour)
    updatedTime.append(mins)

    return updatedTime

def getWeather(command, time, city):

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
   


#     for i in range(len(cityAndZoneList)):
#         currCity = cityAndZoneList[i].split(";")[0]
#         currZone = cityAndZoneList[i].split(";")[1]
#         cityList.append(currCity)
#         timezoneList.append(currZone)


    api_key = "64e227e42c69d247408b968ccff4bdc5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"  



    command = command.split()
    for i in range (len(cityList)):
        if cityList[i] in command or cityList[i].lower() in command:
            city_name = cityList[i]
            zone_name = timezoneNameList[i]
            zone_offset = timezoneGMTList[i][3:]
    
    if(city_name == ""):
        city_name = city


    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # print(x)
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = x['main']
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
    
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
        timeOfDay = ""
        temperature = str(round(current_temperature-273.15,0))
        humidity = ""
        description = weather_description

        print(city_name)
        if(zone_offset != ""):
            currTime = getTimeGivenZone(zone_offset, time)
            currHour = currTime[0]
        else:
            currHour = int(time.split()[3])

        
        if(currHour>=6 and currHour<=10):
            timeOfDay = "morning"
        elif(currHour>=11 and currHour<=13):
            timeOfDay = "around noon"
        elif(currHour>=14 and currHour<= 18):
            timeOfDay = "the afternoon"
        elif(currHour>=19 and currHour<=23):
            timeOfDay = "evening"
        else: timeOfDay = "nighttime"

        if(current_humidity<=30):
            humidity = "very dry"
        elif(current_humidity>30 and current_humidity<=50):
            humidity = "not too dry not too humid"
        elif(current_humidity>50 and current_humidity<=80):
            humidity = "quite humid"
        else:
            humidity = "very humid"
        return "Considering its " + timeOfDay + " in " + city_name + " the current temperature is " + temperature + "Celsius. It is " + humidity + "outside with humidity levels at " + str(current_humidity) + " percent. I also notice the " + description 

    else:
        print(" City Not Found ")
