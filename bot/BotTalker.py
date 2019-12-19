# importing Telegram API
from telegram.ext import Updater
from telegram.ext import CommandHandler
import pickle
import networkx as nx

class BotTalker:

    def __init__(self, token):
        self.TOKEN = token
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.graph = None

    def add_commands(self):
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(CommandHandler('author', self.author))
        self.dispatcher.add_handler(CommandHandler('quiz', self.quiz))
        self.dispatcher.add_handler(CommandHandler('bar', self.bar))
        self.dispatcher.add_handler(CommandHandler('pie', self.pie))
        self.dispatcher.add_handler(CommandHandler('report', self.report))

    def init(self):
        file = open("graph.p", "rb")
        self.graph = pickle.load(file)
        file.close()
        self.updater.start_polling()

    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Hello world!")

    @staticmethod
    def help(bot, update):
        """
        TODO
        :param bot:
        :param update:
        :return:
        """
        bot.send_message(chat_id=update.message.chat_id, text="Help screen not implemented")

    @staticmethod
    def author(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="Pol Monroig Company\npol.monroig@est.fib.upc.edu")

    @staticmethod
    def quiz(bot, update):
        bot.send_message(chat_id=update.message.chat_id,text="Not implemented")

    @staticmethod
    def bar(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Not implemented")

    @staticmethod
    def pie(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Not implemented")

    @staticmethod
    def report(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Not implemented")


