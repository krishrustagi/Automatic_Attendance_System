from gtts import gTTS
from playsound import playsound

#speak the given text
def speak(audio):
    print(audio)

    obj = gTTS(text=audio, lang='en', slow=False)
    obj.save("speak.mp3")
    playsound('speak.mp3')

if __name__ == "__main__":
    str = "Inti"
    speak(str)