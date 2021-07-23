from datetime import datetime                                # So can tell the date/time

def getDate():
    now = datetime.now()
    dt_string = str(now.strftime("%d/%B/%Y %H:%M:%S"))
    date = (dt_string.split())[0] # Break date and time into a list with two elements - we need the first one
    date = date.split('/')

    for i in range(len(date)):
        if date[i][0] == '0':
            date[i] = date[i][1]
    if date[0] == '1':      
        return "Today is the first of " + date[1] + date[2]
    elif date[0] == '2':      
        return "Today is the second of " + date[1] + date[2]
    elif date[0] == '3':      
        return "Today is the third of " + date[1] + date[2]
    elif date[0] == '21':      
        return "Today is the twenty first of " + date[1] + date[2]
    elif date[0] == '22':      
        return "Today is the twenty second of " + date[1] + date[2]
    elif date[0] == '23':      
        return "Today is the twenty third of " + date[1] + date[2]
    elif date[0] == '31':      
        return "Today is the thirty first of " + date[1] + date[2]
    else:    
        return "Today is the" + date[0] + "th of " + date[1] + date[2]
        