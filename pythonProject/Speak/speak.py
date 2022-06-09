from flask import Flask, redirect, url_for, render_template, request, session, flash
import os
import time
import playsound
from gtts import gTTS

app = Flask(__name__)
app.config['SECRET-KEY'] = 'Python'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        text = request.form['read']
        speak(text)
        print(text)
    return render_template('index.html')


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice2.mp3"
    tts.save(filename)
    playsound.playsound(filename)


# speak("hello ekaterine")

if __name__ == "__main__":
    app.run(debug=True)