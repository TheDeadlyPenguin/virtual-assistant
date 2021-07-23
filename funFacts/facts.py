from random import randint

def getFact():
    factCounter = 0
    facts = []
    with open("../virtual-assistant/data/fun-facts.txt") as file:
        for line in file:
                line = line[:-1]
                facts.append(line)
                factCounter += 1

    return facts[randint(0,factCounter - 1)]