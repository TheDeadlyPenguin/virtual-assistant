cityAndZoneList = []
cities = []
zones = []
zonesCleared = []

with open("../virtual-assistant/data/cities-and-zones.txt") as file:
    for line in file:
        line = line[:-1]
        cityAndZoneList.append(line)
        cities.append(line.split(";")[0])
        zones.append(line.split(";")[1])

zonesSet = list(set(zones))
print(len(zonesSet))

dictZoneLettersToNumbers = {}
for i in range(len(zonesSet)):

    zoneInNumbers = str(input(str(i+1) + ". " + zonesSet[i] ))
    dictZoneLettersToNumbers[zonesSet[i]] = "GMT" + zoneInNumbers

print(dictZoneLettersToNumbers)

with open("cities-and-full-timezones.txt","w") as file:
    for i in range(len(cities)):
        file.write(str(cities[i]) + ";" + zones[i] + ";" + dictZoneLettersToNumbers[zones[i]] + '\n')


