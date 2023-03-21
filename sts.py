import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something... ")
    noise = r.adjust_for_ambient_noise(source)  
    print("Noise: "+str(noise))
    audio = r.listen(source)

try:
    print("TEXT: "+r.recognize_google(audio, language='ta-IN'))

except sr.UnknownValueError:
    print("Couldn't understand")
    
except sr.RequestError as e:
    print("Couldn't request results; {}".format(e))