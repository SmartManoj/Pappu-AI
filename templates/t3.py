url='https://translate.google.com/translate_tts?ie=UTF-8&q=yes%21&tl=en-US&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269'
import requests
r=requests.get(url)
with open('output.mp3','wb' ) as f:
    for i in r.iter_content(100000):
        f.write(i)