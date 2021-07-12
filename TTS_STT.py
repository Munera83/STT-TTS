import speech_recognition as sr
import pyttsx3 
  
def SpeakText(command): #convert text to speech and save it as mp3 file
    engine = pyttsx3.init()
    engine.say(command) 
    engine.save_to_file(command, 'speech.mp3')
    engine.runAndWait()

def saveTextToFile(txt): #print text and save it as txt file
    print(txt)
    text_file =open("Output.txt", "w")
    text_file.write(txt)
    text_file.close()

r = sr.Recognizer()
try:      
    with sr.Microphone() as source2: 
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
  
        saveTextToFile(MyText)
        SpeakText("you said "+MyText+ " How can I help you")
         
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
          
except sr.UnknownValueError:
    print("unknown error occured")