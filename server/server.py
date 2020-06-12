from flask import Flask, jsonify, make_response, send_from_directory, request, redirect, render_template
import os
import subprocess
import threading
from pygame import mixer
from sense_hat import SenseHat
from gtts import gTTS
from io import BytesIO
from os.path import exists, join

from constants import CONSTANTS

app = Flask(__name__, static_folder='build')
sense = SenseHat()

@app.route('/api/submit', methods=['POST'])
def submit():
    print(f'Request received')
    user_text = request.data.decode('utf-8')
    speak_thread = threading.Thread(target=speak, args=[user_text])
    display_thread = threading.Thread(target=show_message, args=[user_text])
    speak_thread.start()
    display_thread.start()
    return "Whatever"

def speak(text_to_speak):
    print(f'Speaking: {text_to_speak}')
    speech = gTTS(text_to_speak)
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
    sense.show_message(text_to_display, 0.05, text_colour=[0,0,255])

if __name__ == '__main__':
    os.environ['PA_ALSA_PLUGHW'] = '1'
    sense.set_rotation(180)
    app.run(debug=False, host='0.0.0.0')
    # app.run(port=CONSTANTS['PORT'])