from flask import Flask, jsonify, request
import os
import subprocess
import threading
import datetime
import logging
from pygame import mixer
from sense_hat import SenseHat
from gtts import gTTS
from io import BytesIO

app = Flask(__name__, static_folder='build')
sense = SenseHat()
quiet_hours_start = datetime.time(23, 30)
quiet_hours_end = datetime.time(9, 0)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M',
    handlers=[logging.FileHandler('speak-server.log')]
)

@app.route('/api/submit', methods=['POST'])
def submit():
    logging.info('Request received')
    user_text = request.data.decode('utf-8')
    now = datetime.datetime.now()
    now_time = datetime.time(now.hour, now.minute, now.second)
    if time_in_range(quiet_hours_start, quiet_hours_end, now_time):
        logging.info('Received message during quiet hours: %s', user_text)
    else:
        speak_thread = threading.Thread(target=speak, args=[user_text])
        display_thread = threading.Thread(target=show_message, args=[user_text])
        speak_thread.start()
        display_thread.start()
    return jsonify({"success": True})

def speak(text_to_speak):
    logging.info('Speaking: %s', text_to_speak)
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
    logging.info('Displaying: %s', text_to_display)
    sense.set_rotation(180)
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