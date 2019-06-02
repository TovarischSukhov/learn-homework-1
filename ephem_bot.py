"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import datetime
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def get_const_planet(bot, update):
    text = update.message.text
    planet = split(text)[1]
    print(text)
    print(planet)
    # у тебя ксть логгирование, давай логами, а не принтами
    planets_list = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    # сможешть объяснить эту строку?)
    
    if planet in planets_list:
      pl = ephem.planet(now.strftime("%Y/%m/%d"))
      const = ephem.constellation(pl)
      print(const)
      update.message.reply_text(const)

def main():
    #learn1_axl_bot
    mybot = Updater("886440728:AAEWAxQ7haqJ3wjvQZJZe6Sv4Q2NUsLsC7Y", request_kwargs=PROXY)
    # тебе гитхаб, наверное, уже скзазал, но коммитить ключи - плохо, так как по нему любой человек можкт получить
    # доступ к твоему боту, обычно ключи выносят в файл secrets.py и добавляют его в .gitignore
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_const_planet))
    
    mybot.start_polling()
    mybot.idle()
       
main()
