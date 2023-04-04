from gtts import gTTS
import os

text = input("Enter the text you want to convert to speech: ")
tts = gTTS(text=text, lang='en-uk')
tts.save("output.mp3")
os.system("start output.mp3")
