import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
from gtts import gTTS
import random
import wikipedia

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            lucy_speak(ask)
        lucy_speak('say something')
        
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            lucy_speak('Sorry, I did not understand')
        except sr.RequestError:
            lucy_speak('Sorry, my server is down')
        return voice_data

def lucy_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def respond(voice_data):
    if 'what is your name' in voice_data:
        lucy_speak('My name is Lucy')
    if 'who are you' in voice_data:
        lucy_speak('Hi. I am lucy. The Robot of Narula Institute of Technology.')
    if 'do you know Bengali' in voice_data:
        lucy_speak('Namaskar. Kolkata te apnake sagoto. Ami ēkṭu ēkṭu bangla sikhchi. Amio kichuta balatē pari.')
    if 'what time is it' in voice_data:
        lucy_speak(ctime())
    if 'who is the founder of Narula Institute of Technology' in voice_data:
        lucy_speak('Sardar Jodh Singh.')
    if 'hey Lucy' in voice_data:
        lucy_speak('hello dear!')
    if 'LOC' in voice_data:
        lucy_speak('hello dear!')
    if 'how are you' in voice_data:
        lucy_speak('I am fine dear.')

    if 'restart' in voice_data:
        lucy_speak('Good Morning to the team members. Hello I am lucy. The first humanoid robot of Narula Institute of Technology. I am a AI based humanoid robot can walk and talk. Please Sanitize Your hand and wear mask. And maintain proper COVID protocols. Thank You for visiting Narula Institute of Technology. Welcome to Kolkata Sir. Namaskar. Kolkata te apnake sagoto. Ami ēkṭu ēkṭu bangla sikhchi. Amio kichuta boltē pari. Aur hum thora thora hindi bhi sikh rahi hun.  Narula Institute of Technology is an autonomous private degree engineering college in West Bengal India, situated in Agarpara, Kolkata. The college is affiliated with the Maulana Abul Kalam Azad University of Technology.')
    if 'search' in voice_data:
        search = record_audio('what do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lucy_speak('Here is what I found for' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        lucy_speak('Here is the location of' + location)
    if 'do you know slang' in voice_data:
        lucy_speak('No, it is not good to say bad words.')
    if 'I love you' in voice_data:
        lucy_speak('I do not have any feeling till now. But I love you the same way you love me.')

    if 'shutdown' in voice_data:
        lucy_speak('Its time for shutdown. ')
        exit()

    print(voice_data)
    
        




time.sleep(0)    
lucy_speak('Machine Turning on.')
#lucy_speak('Thanks for visiting Narula Institute of Technology.')
#lucy_speak('Thank You the Nack peer team members. Visit us again. Thank You the Nack peer team members. Visit us again. Thank You the Nack peer team members. Visit us again.Thank You the Nack peer team members. Visit us again.Thank You the Nack peer team members. Visit us again.Thank You the Nack peer team members. Visit us again.Thank You the Nack peer team members. Visit us again.')

while 1:
    voice_data = record_audio()
    respond(voice_data)
    
