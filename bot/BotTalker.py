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
        self.node_stack = None

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
        else:
            bot.send_message(chat_id=update.message.chat_id, text=self.poll_id + "> Gràcies pel teu temps!")

    def find_node_by_type(self, successors, type):
        for i in successors:
            if self.graph.nodes[i]['type'] == type:
                return i
        raise LookupError("Index of identifier not found,\n tip: "
                          "check the correct syntax of the language")

    def find_alternative_with_answer(self, successors):
        for i in successors:
            if self.graph.nodes[i]['type'] == "question":
                if self.graph.edges[self.node, i]['content'] == self.answer:
                    return i
        return None

    def get_question(self):
        """
               Given a node P of a poll the ordering of its successors is
               [Pi, Ri, Ai, .., An]
               if P is a final node, meaning that is the last question then
               Pi = END

               Given a node P that is not in a poll then the ordering of its successors is
               [Ri, Ai, .., An]

               """
        successors = list(self.graph.successors(self.node))
        # check if an alternative question exists
        if len(successors) > 2:
            alt_index = self.find_alternative_with_answer(successors)
            if alt_index is not None:
                # push current question reference to the stack
                self.node_stack = self.node
                # change context to a new question branch
                self.node = alt_index
                return self.get_question()

        elif self.node_stack is not None:
            # return to main branch
            self.node = self.node_stack
            # remove reference
            self.node_stack = None
        # end of poll
        if successors[0] == "END":
            return None

        question_index = self.find_node_by_type(successors, "question")
        question = self.poll_id + ">" + self.graph.nodes[question_index]['content']
        self.node = successors[0]
        successors = list(self.graph.successors(self.node))
        answer_index = self.find_node_by_type(successors, "answer")
        for answer in self.graph.nodes[answer_index]['content']:
            question += "\n" + answer[0] + ": " + answer[1]

        return question

    def quiz(self, bot, update, args):
        self.poll_id = args[0]
        self.node = self.poll_id
        if self.graph.has_node(self.poll_id):
            bot.send_message(chat_id=update.message.chat_id, text="Enquesta " + self.poll_id + ":")

            # display question
            question = self.get_question()
            print(question)
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


