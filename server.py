from flask import Flask, request, redirect, render_template
import subprocess
import os
import threading
from pygame import mixer
from sense_hat import SenseHat
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)
sense = SenseHat()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_text = request.form['text-input']
    speak_thread = threading.Thread(target=speak, args=[user_text])
    display_thread = threading.Thread(target=show_message, args=[user_text])
    speak_thread.start()
    display_thread.start()
    return redirect('/')

def speak(text_to_speak):
    print(f'Speaking: {text_to_speak}')
    speech = gTTS(text = text_to_speak, lang = 'en', slow = False)
    fp = BytesIO()
    speech.write_to_fp(fp)
    fp.seek(0)
    mixer.init()
    mixer.music.load(fp)
    mixer.music.play()
    while mixer.music.get_busy():
        continue
    fp.close()

def show_message(text_to_display):
    print(f'Displaying: {text_to_display}')
    sense.show_message(text_to_display, 0.05)

if __name__ == '__main__':
    os.environ['PA_ALSA_PLUGHW'] = '1'
    sense.set_rotation(180)
    app.run(debug=True, host='0.0.0.0')