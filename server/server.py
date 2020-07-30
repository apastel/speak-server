from flask import Flask, jsonify, request
import os
import subprocess
import threading
import datetime
from pygame import mixer
from sense_hat import SenseHat
from gtts import gTTS
from io import BytesIO

app = Flask(__name__, static_folder='build')
sense = SenseHat()
sense.set_rotation(180)
quiet_hours_start = datetime.time(23, 30)
quiet_hours_end = datetime.time(9, 0)

@app.route('/api/submit', methods=['POST'])
def submit():
    print(f'Request received', flush=True)
    user_text = request.data.decode('utf-8')
    now = datetime.datetime.now()
    now_time = datetime.time(now.hour, now.minute, now.second)
    if time_in_range(quiet_hours_start, quiet_hours_end, now_time):
        print(f'Received message during quiet hours: {user_text}', flush=True)
    else:
        speak_thread = threading.Thread(target=speak, args=[user_text])
        display_thread = threading.Thread(target=show_message, args=[user_text])
        speak_thread.start()
        display_thread.start()
    return jsonify({"success": True})

def speak(text_to_speak):
    print(f'Speaking: {text_to_speak}', flush=True)
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
    print(f'Displaying: {text_to_display}', flush=True)
    sense.show_message(text_to_display, 0.05, text_colour=[0,0,255])

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

if __name__ == '__main__':
    os.environ['PA_ALSA_PLUGHW'] = '1'
    app.run(debug=False, host='0.0.0.0')