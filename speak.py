import os

#speak the given text
def speak(audio):
    print(audio)
    os.system(f"say {audio}")

if __name__ == "__main__":
    str = "hello my name is krish"
    speak(str)