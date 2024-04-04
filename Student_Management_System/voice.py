import speech_recognition
import speech_recognition as sr
voice=sr.Recognizer()

with sr.Microphone() as source:
    audio = voice.listen(source)
    try:
        text = voice.recognize_google(audio)
        print('you say:', text)
    except:
        print('your voice is not clear')

