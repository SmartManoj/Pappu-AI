import os
import io
import tempfile
from time import sleep
import wave
import speech_recognition as sr
from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO, emit
os.chdir('Maniyaandi')
from ai import bing
with open('count.txt') as f:
    count=int(f.read())
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

r = sr.Recognizer()

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('stream')
def handle_stream(audio):
    with io.BytesIO(audio) as f:
        try:
            # save audio file
            audio_data = sr.AudioData(f.read(), sample_rate=44100, sample_width=2)
            with open('audio.wav', 'wb') as f:
                f.write(audio_data.get_wav_data())
            transcript = r.recognize_google(audio_data)
        except sr.UnknownValueError:
            transcript = 'Unknown'
        emit('transcript', transcript)

@app.route('/index')
def index():
    return render_template('index.html')

from ttime import time_in_tamil
import requests
import requests


@app.route('/playback', methods=['POST','GET'])
async def playback():
    global count
    pre_defined = request.args.get('pre_defined')
    if not pre_defined:
        if 1:
            # Get the uploaded audio file
            audio_file = request.files['audio']
            # audio_data = audio_file.read()
            # Save the audio file to a temporary location
            temp_file = 'audio.webm'

            audio_file.save(temp_file)
            os.system('ffmpeg -i audio.webm audio.wav -y')
            count +=1
            os.system(f'ffmpeg -i audio.webm data/audio{count}.wav -y')
            with open('count.txt','w') as f:
                f.write(str(count))
            # sleep(1)
            # save as 
            # os.system(f'ffplay -nodisp -autoexit ./{temp_file} ')

            audio_source = sr.AudioData(open('audio.wav','rb').read(), 44100, 2)
            try:
                transcript = r.recognize_google(audio_source, language='ta-IN')
                print(transcript)
            except sr.UnknownValueError as e:
                transcript = str(e)
            
        else:
            transcript='வணக்கம்.'
    else:
        transcript=pre_defined
            
    if transcript in ['மணி எத்தனை','மணி எத்தன']:
                transcript=time_in_tamil()
    else:
        if transcript:
            transcript=await bing(transcript)
        else:
            transcript= 'சரியா கேக்கலீங்க. இன்னொரு முற  சொல்லுங்க.'
    from gtts import gTTS
    tts = gTTS(transcript,lang='ta')
    tts.save('output.mp3')
    print('saved',flush=True)
    return send_file('output.mp3')
@app.route('/')
def index2():
    return render_template('t.html')

@app.route('/t2')
def t2():
    return render_template('t2.html')

if __name__ == '__main__':
    # https support
    context = ('server.crt', 'server.key')
    # socketio.run(app,host='0.0.0.0',port=5000,debug=True,keyfile='key.pem',certfile='cert.pem')
    app.run(host='0.0.0.0',debug=True, ssl_context='adhoc')

    

