import os
import telebot
import json
import requests
from keep_alive import keep_alive

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['meme'])
def getMeme(message):
  response = requests.get("https://meme-api.herokuapp.com/gimme/IndianDankMemes")
  json_data = json.loads(response.content)['url']
  bot.send_photo(message.chat.id, json_data)

@bot.message_handler(commands=['inspire']) 
def getQuote(message):
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  bot.send_message(message.chat.id,quote)

@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message, "Hey! How r u?")

@bot.message_handler(commands=['menu'])
def commands(message):
  bot.send_message(message.chat.id, "/greet \n/meme \n/inspire")

print("Compiled!")
keep_alive()
bot.polling()
