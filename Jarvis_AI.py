import speech_recognition
import pyttsx3
import datetime
import wikipedia
import webbrowser

recognizer = speech_recognition.Recognizer()

# Audio System of A.I
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greeting System of A.I
def wishme():
    time = int(datetime.datetime.now().hour)
    if time >= 4 and time <= 12:
        print("\nGood Morning and Raam Raam Sir")
        speak("Good Morning and Raam Raam Sir")
    elif time > 12 and time <= 17:
        print("\nGood Afternoon Sir")
        speak("Good Afternoon Sir ")
    else:
        print("Good Evening and Raam Raam Sir")
        speak("Good Evening and Raam Raam Sir")
    
    speak("This is Jarvis A I . Your personal desktop assistant developed by Pratham Vajpayee to be at you service. How can I help you ?")
# Speech Recognition System of A.I
def takeCommand():
 # here speech recognition module takes sound from the microphone as mic and return string by google recogniser
 recognizer = speech_recognition.Recognizer()
 speak("Listening...")
 print("\nListening...")
 try:
    with speech_recognition.Microphone() as mic:
            
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        print("Recognizing...")
        speak("Recognizing..")
        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(f"\nUser Said,{text}")

 except speech_recognition.UnknownValueError:
        print("cant hear say that agian..")
        speak("cant hear, say that again..")
        recognizer = speech_recognition.Recognizer()
        return "None"

 if "your name" in text:
    speak("I am jarvis . Your personal desktop assistant")

 elif "hi" in text :
    speak("Hi Sir, How can I help you")

 elif "do you live" in text:
    speak("Sir I am a artificial intelligent made by pratham vajpayee, and live in your desktops memory. ")
    text = text.replace("do you live","")
    
 elif "wikipedia" in text:
    speak("searching wikipedia")
    text = text.replace("wikipedia","")
    results = wikipedia.summary(text, sentences= 3)
    speak("According to wikipedia")
    print(results)
    speak(results)
    text = text.replace("wikipedia","")

 elif "open youtube" in text:
    speak("Opening Youtube Sir")
    webbrowser.open("youtube.com")
    
 elif "open google" in text:
    speak("Opening Google Sir")
    webbrowser.open_new_tab("google.com")
   
 elif "the time" in text:
    strft = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"sir the time rignt now is{strft}")
    
 #elif "quit" or "stop" or "terminate" in text:
   # speak("Good Bye sir, I hope I help you . and I hope your day will go good . Your well-wisher jarvis ")
   # quit()
 elif "make a password" or "create a password" in text:
    speak("Importing password generator module.")
    import Practice_day_1
    speak("Importing password gen . I hope jarvis password generator from gen series one helped you.")

 return takeCommand()

#Execution
if __name__ == "__main__":
 wishme()
 while True:
  takeCommand()
  continue


   
        
