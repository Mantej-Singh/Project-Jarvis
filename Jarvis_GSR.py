import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from  datetime import datetime
import webbrowser



#Create timestamp
time_stamp=time.strftime("%H%M%S")
file1 = str(str(time_stamp) + ".mp3")

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save(file1)
    os.system(file1)
    os.remove(file1)
    
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,timeout=2,phrase_time_limit=5)
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        print("You said: " + r.recognize_google(audio))
        data = r.recognize_google(audio)
        #print("You said: " + r.recognize_wit(audio,key='ION5SH3SH4QPDEVUUQVTNBZWNEK657MW'))
        #Sdata = r.recognize_wit(audio,key='ION5SH3SH4QPDEVUUQVTNBZWNEK657MW')
        if data=="":
            speak("If you just said something, I didn't hear what it was")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("If you just said something, I didn't hear what it was")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("Could not request results from Google Speech Recognition service")
 
    return data   


def jarvis(data):
    if "how are you" in data:
        speak("I am fine Mantej, Have a nice day!")
 
    if "time" in data:
        speak(ctime())
 
    if "location" in data:
        data = data.split(" ")
        location = data[2] + data[3]
        speak("Hold on Mantej, I will show you where " + location + " is.")
        webbrowser.open("https://www.google.com/maps/place/" + location)

    if "Google" in data:
        data = data.split(" ")
        print(type(data))
        find = data[0:]
        str1 = ' '.join(find)
        keyword='Google'
        after = str1[str1.index(keyword) + len(keyword):]
        #find=[]
        #find.append(data)
        #findall = find[0:]
        
        speak("Hold on Mantej, I will Google the request for you !")
        webbrowser.open("https://www.google.com/search?num=30&site=&source=hp&q=" + after)

    if "google" in data:
        data = data.split(" ")
        print(type(data))
        find = data[0:]
        str1 = ' '.join(find)
        keyword='google'
        after = str1[str1.index(keyword) + len(keyword):]
        #find=[]
        #find.append(data)
        #findall = find[0:]
        
        speak("Hold on Mantej, I will Google the request for you !")
        webbrowser.open("https://www.google.com/search?num=30&site=&source=hp&q=" + after)
#END THE PROGRAM

    if "Bye" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()
    if "close" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()
    if "end" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()
    if "terminate" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()
    if "goodbye" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()
    if "see you soon" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()
    if "take rest" in data:
        speak("Good Bye, Mantej, see you soon!!!")
        #exit()
        quit()


        
# Starting the Engine
time.sleep(2)
speak("Hi Mantej, what can I do for you?")
count = 0
#while (count < 3):
while 1:
    print('Request '+ str(count))
    data = recordAudio()
    jarvis(data)
    count = count + 1

 
