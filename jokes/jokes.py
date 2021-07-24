from random import randint

def getJoke():
    jokeCounter = 0
    jokes = []
    with open("../virtual-assistant/data/jokes.txt") as file:
        for line in file:
                line = line[:-1]
                jokes.append(line)
                jokeCounter += 1

    return jokes[randint(0,jokeCounter - 1)]