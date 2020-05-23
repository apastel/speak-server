from flask import Flask, request, redirect, render_template
import subprocess
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/speak', methods=['POST'])
def speak():
    text_to_speak = request.form['text-input']
    subprocess.run(['espeak', text_to_speak, '2>/dev/null'], check=True)
    return redirect('/')


if __name__ == '__main__':
    os.environ['PA_ALSA_PLUGHW'] = '1'
    app.run(debug=True, host='0.0.0.0')