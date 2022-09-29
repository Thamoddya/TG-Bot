from imaplib import Commands
import os

from click import command
import telebot

bot= telebot.TeleBot("API KEY")

@bot.massage_handler(Commands=["start"])
def send_welcome(massage):
    bot.reply_to(massage,"Hey Im thamoddya rashmitha")

@bot.massage_handler(Commands=["how"])
def send_massage(massage):
    bot.send.massage(massage, "https://www.youtube.com/watch?v=mYMMfI6QBHA")
    
bot.pollig()
