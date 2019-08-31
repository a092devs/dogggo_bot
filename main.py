from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bork(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('941843799:AAH_IkDvzX310eIS-zzv5or0ZVMLRKpdhHoN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bork',bork))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
