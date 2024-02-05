import telebot
import main
from load_dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "I can help you with that")


# any message that contains "/get teacher search" will trigger this function
@bot.message_handler(regexp="\/get (.+) (.+)")
def get_class(message):
    teacher = int(message.text.split()[1])
    search = message.text.split()[2]
    state = main.main(teacher, search)
    bot.reply_to(message, state)


bot.polling()
