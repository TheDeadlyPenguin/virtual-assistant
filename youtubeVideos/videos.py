def clearRequest(command):

    command = command.split()
    indexOfPlay = 0
    for i in range(len(command)):
        if(command[i]=="play"):
            indexOfPlay = i
            break
    toBeSearched = ""
    for i in range(indexOfPlay + 1, len(command)):
        toBeSearched += command[i] + " "

    return toBeSearched
