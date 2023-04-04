import asyncio
from EdgeGPT import Chatbot, ConversationStyle
from pprint import pprint
try:
    bot = Chatbot(cookiePath='./cookies.json')
except Exception as e:
    print(e)
    pass

async def bing(text):
    
    res= (await bot.ask(prompt=text, conversation_style=ConversationStyle.balanced))
    o =  res['item']['messages'][1]['adaptiveCards'][0]['body'][0]['text']
    print(o)
    return o

    # print(2)


if __name__ == "__main__":
    from datetime import datetime
    print(asyncio.run(bing('What can you do?')))
    pass