from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

# init
TOKEN = '429278408:AAGwedZI-TpW7caRu7q3TqM7r75WhcAJdK0'
updater = Updater(TOKEN)
dev_mode = True

# aliases
dispatcher = updater.dispatcher

# setup logging
if dev_mode:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to secret hitler. Lets play a game.")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
