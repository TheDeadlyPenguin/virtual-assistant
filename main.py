import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

import capitals.capitals


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





toSpeak = gTTS(text=capitals.capitals.getCapitalName(spokenWords), lang="en", slow=False)
toSpeak.save("welcome.mp3")
  
# Playing the converted file
playsound('welcome.mp3')