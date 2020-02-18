#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:27:31 2020

@author: lucasabdalah
"""

import telegram.ext
import utils as ut
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

my_token = "917394528:AAGfMNosAr2BZmC-r7GqOHwi77EaFCCpzUc"

bot = telegram.Bot(token=my_token)

# Default Functions
def start(bot, update):
    update.message.reply_text("Ola, seja bem-vindo ao IntercampiBOT !")

def help(bot, update):
    update.message.reply_text("je vais chercher!")

def error(bot,update,error):
        print('error')
        update.message.reply_text("Desculpa, eu não conheço esse comando.")

def PiciBenfica(bot, update):
    PiciBenfica = ut.getPiciBenfica()
    update.message.reply_text("O status desse onibus: {}".format(PiciBenfica))

def PiciLabomar(bot,update):
    PiciLabomar = ut.getPiciLabomar()
    update.message.reply_text("{}".format(PiciLabomar))

def PiciLabomar_Timetable(bot,update):
    Timetable = ut.getTimeTable('LABOMAR.csv')
    # update.message.reply_text("Tabela de Horarios:\n{}".format(Timetable))
    update.message.reply_text("Tabela de Horarios:\n" +  Timetable)

# Commands Handling Part
updater = Updater(my_token)

dp = updater.dispatcher

# Default Commands
dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",help))
dp.add_error_handler(error)

# Functions Commands
dp.add_handler(CommandHandler("PiciBenfica",PiciBenfica))
dp.add_handler(CommandHandler("PiciLabomar",PiciLabomar))

# Timetables Commands
dp.add_handler(CommandHandler("PiciLabomar_Timetable",PiciLabomar_Timetable))

# Bot Updater
updater.start_polling()
updater.idle()
