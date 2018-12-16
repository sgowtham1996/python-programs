from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Gowtham\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\chatterbot_corpus\data\english/'):
    data = open('C:/Users/Gowtham\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\chatterbot_corpus\data\english/' + files,'r').readlines()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot:',reply)
    
    if message.strip() == 'Bye':
        print('Chartbot: bye ')
        break
