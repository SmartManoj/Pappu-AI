import asyncio
from EdgeGPT import Chatbot, ConversationStyle
from pprint import pprint
bot = Chatbot(cookiePath='./cookies.json')
async def bing(text):
    res= (await bot.ask(prompt=text, conversation_style=ConversationStyle.balanced))
    o =  res['item']['messages'][1]['adaptiveCards'][0]['body'][0]['text']
    return o
    # print(2)
    # pprint(await bot.ask(prompt="What can you do?", conversation_style=ConversationStyle.balanced))


if __name__ == "__main__":
    pass