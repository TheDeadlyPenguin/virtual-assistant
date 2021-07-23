dictOfAllCountries = {}
with open("../virtual-assistant/data/countries-and-capitals.txt") as file:
    for line in file:
        currCountryAndCapital = line.split()
        indexOfDash = 0
        countryName = ""
        capitalName = ""
        for i in range(len(currCountryAndCapital)):
            if currCountryAndCapital[i] == '-':
                indexOfDash = i
                break
        for i in range(indexOfDash):
            countryName += currCountryAndCapital[i] + " "
        for i in range(indexOfDash+1,len(currCountryAndCapital)):
            capitalName += currCountryAndCapital[i] + " "
        countryName = countryName.replace(" ","")
        capitalName = capitalName.replace(" ","")
        dictOfAllCountries[countryName] = capitalName


def getCapitalOrCountryName(command):
    countryNames = list(dictOfAllCountries.keys())
    for country in countryNames:
        if country in command:
            return "The capital of " + country + " is " + dictOfAllCountries[country]
    for country in countryNames:
        currCapital = dictOfAllCountries[country]
        if currCapital in command:
            return "The capital of " + country + " is " + currCapital
    return "Sorry! Didn't get what capital you mean."