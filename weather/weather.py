import requests
import geocoder
from datetime import datetime                                # So can tell the date/time
import pytz
from difflib import SequenceMatcher

def getWeather(command):

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
        city = geocoder.ip('me').city
        time = datetime.now()
        time = time.strftime("%H:%M")
        time = time.split(":")


        hour = time[0]


        hour = int(hour)
        if(hour < 0):
            hour += 24
        
        return getForecast([city," "], hour)
            


    elif(len(possibleCities) == 1):
        hour = findHourGivenZone(possibleCities[0])
        return getForecast(possibleCities[0], hour)

    else:
        return possibleCities

def findCorrectCityAndHour(command, possibleCities):
    maxRatio = 0
    currCityInfo = []
    # print(possibleCities)

    for i in range(len(possibleCities)):
        currRatio = SequenceMatcher(None,command,possibleCities[i][0] + " " + possibleCities[i][1]).ratio()
        if(currRatio > maxRatio):
            maxRatio = currRatio
            currCityInfo = possibleCities[i]
    return getForecast(currCityInfo, findHourGivenZone(currCityInfo))

def findHourGivenZone(cityInfo):
    alternativeTime = pytz.timezone(cityInfo[2])
    time = datetime.now(alternativeTime)
    time = time.strftime("%H:%M")
    time = time.split(":")

    hour = time[0]

    hour = int(hour) - 2
    if(hour < 0):
        hour += 24

    return hour



def getForecast(currCityInfo, currHour):
    city_name = currCityInfo[0]
    country_name = currCityInfo[1]

    api_key = "64e227e42c69d247408b968ccff4bdc5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"  
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
        # print(" Temperature (in kelvin unit) = " +
        #                 str(current_temperature) +
        #     "\n atmospheric pressure (in hPa unit) = " +
        #                 str(current_pressure) +
        #     "\n humidity (in percentage) = " +
        #                 str(current_humidity) +
        #     "\n description = " +
        #                 str(weather_description))
        timeOfDay = ""
        temperature = str(round(current_temperature-273.15,0))
        humidity = ""
        description = weather_description

        
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
        if(country_name != " "):
            return "Considering its " + timeOfDay + " in " + city_name + " in " + country_name + " the current temperature is " + temperature + "Celsius. It is " + humidity + "outside with humidity levels at " + str(current_humidity) + " percent. I also notice the " + description 
        else:
            return "Considering its " + timeOfDay + " in " + city_name + " the current temperature is " + temperature + "Celsius. It is " + humidity + "outside with humidity levels at " + str(current_humidity) + " percent. I also notice the " + description 

    else:
        return "Sorry, this city is not in my database."
