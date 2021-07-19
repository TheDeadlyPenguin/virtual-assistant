dictOfAllCountries = {}
with open("names.txt") as file:
    for line in file:
        currCountryAndCapital = line.split()
        if(len(currCountryAndCapital)>1):
            dictOfAllCountries[currCountryAndCapital[0]] = currCountryAndCapital[1]

def getCapitalName(countryName):
    return dictOfAllCountries[countryName]