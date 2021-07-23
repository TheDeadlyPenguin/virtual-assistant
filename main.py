import speech_recognition as sr                              # So voice can be recognized
from gtts import gTTS                                        # So the program can ssave .mp3 files
from playsound import playsound                              # So can run .mp3 files
# from datetime import datetime                              # So can tell the date/time
# import requests, json                                        # required for Weather API


from capitals.capitals import getCapitalOrCountryName          # To find a capital/country given a capital/country
from dateAndTime.date import getDate                           # So can say the date
from dateAndTime.time import getTime,getTimezoneOffsetAndName,getTimeWithZoneInfo  
                                                               # So can say the time and timezones
from weather.weather import getWeather                         # So can tell the weather

def take_command():
    recognizeSpeech = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        print("Talk")
        audio_text = recognizeSpeech.listen(source, timeout = 5.0)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            spokenWords = recognizeSpeech.recognize_google(audio_text)
            print("Text: " + spokenWords) #add    , language = "bg-BG"   for bg
        except:
            print("Sorry, I did not get that - is your connection alright?")
    return spokenWords


def run_bot():
    command = take_command()
    print(command)
    toSay = ""

    if("repeat" in command):
        repeat()
    elif("capital" in command):
        toSay = getCapitalOrCountryName(command)
    elif("weather" in command):
        time = getTime()
        toSay = getWeather(command,time)
    elif("time" in command):
        time = getTime()
        cityInfo = getTimezoneOffsetAndName(command)
        toSay = getTimeWithZoneInfo(cityInfo,time)
    elif("date" in command or ("what" in command and "today" in command)):
        toSay = getDate()
    else:
        toSay = "I'm so sorry! I couldn't understand you."
    
    talk(toSay)


def talk(toSay):
    toSpeak = gTTS(text=toSay, lang="en", slow=False)
    toSpeak.save("reply.mp3")
    
    # Playing the converted file
    playsound('reply.mp3')

def repeat():
    repeatIntro = "The last thing I said was"

    toSpeak = gTTS(text=repeatIntro, lang="en", slow=False)
    toSpeak.save("repeat.mp3")
    playsound('repeat.mp3')
    playsound('reply.mp3')


run_bot()