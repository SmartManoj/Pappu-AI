import os
import io
import tempfile
from time import sleep
import wave
import speech_recognition as sr
from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO, emit

from ai import bing

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

@app.route('/')
def index():
    return render_template('index.html')

from pydub import AudioSegment
from ttime import time_in_tamil
import requests
import requests

def say( text, lang = 'en-US'):

    cookies = {
        'SID': 'UghJC6vR4gcClUthe86yWFoojAcC6uLm_Q3BXwaVjTlDlppoR7m5VvgIb8boUgUq5bnMYQ.',
        '__Secure-1PSID': 'UghJC6vR4gcClUthe86yWFoojAcC6uLm_Q3BXwaVjTlDlppoUFdTQ8GZxJNbaf43fnqySQ.',
        '__Secure-3PSID': 'UghJC6vR4gcClUthe86yWFoojAcC6uLm_Q3BXwaVjTlDlppojsz048qEvCU_3J_E4MfCEw.',
        'HSID': 'A2iRvWV6Jjn5gFcNg',
        'SSID': 'AVlPW3977tkchXGhe',
        'APISID': 'wwm92c0tKeevFxQc/AUnMjct5eBLbERiPp',
        'SAPISID': '1kSU7-TPFWgxVoMc/A11OY3qHDQt5x5bwL',
        '__Secure-1PAPISID': '1kSU7-TPFWgxVoMc/A11OY3qHDQt5x5bwL',
        '__Secure-3PAPISID': '1kSU7-TPFWgxVoMc/A11OY3qHDQt5x5bwL',
        'SEARCH_SAMESITE': 'CgQI7JcB',
        'NID': '511=VaGPr5gJJsP8gKyfEmCxYN2GaEfhm1ETt-WKK3-UKSWlmtr94zIUuj913Yve85Dudx-LeRM1KKRUkr-bfhmt7C_zi9wewy3g3gOQcALYWbVDRseal6YTKWR97K1VAdRofruvaWnn3BrfkSL7jcZHTuIfWbsg29d8N7e3RtjqgDO1tnqn3--HBzV-CPwCweN-LPptVhgCntFMkeTb7o5KiNdhmBViVOgdKstGFXaV9rTFEUU71tVsdFo',
        'SIDCC': 'AFvIBn-bnWriv-4OheNrWgx6VYKeFjA2qyNByDrfe6c7sV3ps3-xDs5480vg-jU-WZ4dyNmaJg',
        '__Secure-1PSIDCC': 'AFvIBn-eR1RmrHLNebmioyvTWmHgIuxkWVZcDk-tS-SdCURAZmO8qoTDPXgSQQruCG-JJlF0rA',
        '__Secure-3PSIDCC': 'AFvIBn-CDBZ_fVLMCMccqtqs11ckMZfqb1_EFgxSDA_mzAT335Gn2xT7O6O_63MQtQcr4aGdnqI',
    }

    headers = {
        'authority': 'translate.google.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'SID=UghJC6vR4gcClUthe86yWFoojAcC6uLm_Q3BXwaVjTlDlppoR7m5VvgIb8boUgUq5bnMYQ.; __Secure-1PSID=UghJC6vR4gcClUthe86yWFoojAcC6uLm_Q3BXwaVjTlDlppoUFdTQ8GZxJNbaf43fnqySQ.; __Secure-3PSID=UghJC6vR4gcClUthe86yWFoojAcC6uLm_Q3BXwaVjTlDlppojsz048qEvCU_3J_E4MfCEw.; HSID=A2iRvWV6Jjn5gFcNg; SSID=AVlPW3977tkchXGhe; APISID=wwm92c0tKeevFxQc/AUnMjct5eBLbERiPp; SAPISID=1kSU7-TPFWgxVoMc/A11OY3qHDQt5x5bwL; __Secure-1PAPISID=1kSU7-TPFWgxVoMc/A11OY3qHDQt5x5bwL; __Secure-3PAPISID=1kSU7-TPFWgxVoMc/A11OY3qHDQt5x5bwL; SEARCH_SAMESITE=CgQI7JcB; NID=511=VaGPr5gJJsP8gKyfEmCxYN2GaEfhm1ETt-WKK3-UKSWlmtr94zIUuj913Yve85Dudx-LeRM1KKRUkr-bfhmt7C_zi9wewy3g3gOQcALYWbVDRseal6YTKWR97K1VAdRofruvaWnn3BrfkSL7jcZHTuIfWbsg29d8N7e3RtjqgDO1tnqn3--HBzV-CPwCweN-LPptVhgCntFMkeTb7o5KiNdhmBViVOgdKstGFXaV9rTFEUU71tVsdFo; SIDCC=AFvIBn-bnWriv-4OheNrWgx6VYKeFjA2qyNByDrfe6c7sV3ps3-xDs5480vg-jU-WZ4dyNmaJg; __Secure-1PSIDCC=AFvIBn-eR1RmrHLNebmioyvTWmHgIuxkWVZcDk-tS-SdCURAZmO8qoTDPXgSQQruCG-JJlF0rA; __Secure-3PSIDCC=AFvIBn-CDBZ_fVLMCMccqtqs11ckMZfqb1_EFgxSDA_mzAT335Gn2xT7O6O_63MQtQcr4aGdnqI',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="111", "Google Chrome";v="111.0.5563.64"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"111.0.1661.44"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="111.0.1661.44", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.64"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '"5.15.89"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    params = {
        'ie': 'UTF-8',
        'q': text,
        'tl': lang,
        'ttsspeed': '1',
        'total': '.5',
        'idx': '0',
        'client': 'tw-ob',
        'textlen': '14',
        'tk': '594228.1040269',
    }

    return requests.get('https://translate.google.com/translate_tts', params=params, cookies=cookies, headers=headers)

@app.route('/playback', methods=['POST'])
async def playback():
    if 1:
        # Get the uploaded audio file
        audio_file = request.files['audio']
        # audio_data = audio_file.read()
        # Save the audio file to a temporary location
        temp_file = 'audio.webm'

        audio_file.save(temp_file)
        os.system('ffmpeg -i audio.webm audio.wav -y')
        # sleep(1)
        # save as 
        # os.system(f'ffplay -nodisp -autoexit ./{temp_file} ')

        audio_source = sr.AudioData(open('audio.wav','rb').read(), 44100, 2)
        try:
            transcript = r.recognize_google(audio_source, language='ta-IN')
            print(transcript)
        except sr.UnknownValueError as e:
            transcript = str(e)
        
        if transcript in ['மணி எத்தனை','மணி எத்தன']:
            transcript=time_in_tamil()
        else:
            if transcript:
                transcript=await bing(transcript)
            else:
                transcript= 'சரியா கேக்கலீங்க. இன்னொரு முற  சொல்லுங்க.'
    else:
        transcript='வணக்கம்.'
    from gtts import gTTS
    tts = gTTS(transcript,lang='ta')
    tts.save('output.mp3')
    print('saved',flush=True)
    return send_file('output.mp3')
@app.route('/t')
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

    

