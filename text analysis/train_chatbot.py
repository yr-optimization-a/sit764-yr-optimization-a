from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('bot')
bot.set_trainer(ListTrainer)

data = open('/Users/parth/Documents/data/daily-per-capita-supply-of-calories (1).csv' , 'r').readlines()
bot.train(data)


while True:
	message = input('You:') 
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Chatbot:', reply)
	if message.strip() == 'Bye':
		print('Chatbot: Bye')
		break
