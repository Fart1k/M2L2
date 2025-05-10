import telebot
import os
import random
import requests
files = os.listdir('Images')


bot = telebot.TeleBot("7958738417:AAEWDGJBnfoLku4wN2zdvBpHJNldhCN_xIw")

@bot.message_handler(commands=['mem'])
def send_meme(message):
    image = random.choice(files)
    with open(f'Images/{image}', 'rb') as fn:  
        bot.send_photo(message.chat.id, fn)


def get_duck_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['link']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)


bot.polling()
