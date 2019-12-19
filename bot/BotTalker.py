# importing Telegram API
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import pickle
import networkx as nx

class BotTalker:

    def __init__(self, token):
        self.TOKEN = token
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.graph = None
        self.answer = None
        self.poll_id = None
        self.node = None

    def add_commands(self):
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(CommandHandler('author', self.author))
        self.dispatcher.add_handler(CommandHandler('quiz', self.quiz, pass_args=True))
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
        """
        bot.send_message(chat_id=update.message.chat_id, text="Help screen not implemented")

    @staticmethod
    def author(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="Pol Monroig Company\npol.monroig@est.fib.upc.edu")


    def read_answer(self, bot, update):
        msg = update.message.text
        self.answer = msg
        print("Answered")
        question = self.get_question()
        if question is not None:
            bot.send_message(chat_id=update.message.chat_id, text=question)

    """
       Given a node P of a poll the ordering is 
       [Pi, Ri, Ai, .., An]
       if P is a final node, meaning that is the last question then 
       Pi = END 

       Given a node P that is not in a poll then the ordering is 
       [Ri, Ai, .., An]

       """
    def get_question(self):
        successors = list(self.graph.successors(self.node))
        if successors[0] == "END":
            return None
        question = self.poll_id + ">" + self.graph.nodes[successors[0]]['content']
        self.node = successors[0]
        successors = list(self.graph.successors(self.node))
        for i, answer in enumerate(self.graph.nodes[successors[1]]['content']):
            question += "\n" + str(i) + ": " + answer

        return question

    def quiz(self, bot, update, args):
        self.poll_id = args[0]
        self.node = self.poll_id
        if self.graph.has_node(self.poll_id):
            bot.send_message(chat_id=update.message.chat_id, text="Enquesta " + self.poll_id + ":")

            # display question
            question = self.get_question()
            bot.send_message(chat_id=update.message.chat_id, text=question)
            # read answer
            self.dispatcher.add_handler(MessageHandler(Filters.text, self.read_answer))


        else:
            bot.send_message(chat_id=update.message.chat_id, text="No existe la encuesta seleccionada")

    @staticmethod
    def bar(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Not implemented")

    @staticmethod
    def pie(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Not implemented")

    @staticmethod
    def report(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Not implemented")


