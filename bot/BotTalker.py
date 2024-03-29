# importing Telegram API
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import pickle
import matplotlib.pyplot as plt
from os.path import isfile


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
        self.successors = None
        self.quiz_started = False
        self.TALKER_PICKLE_PATH = "talker.p"
        self.answers_data = {}

    def add_commands(self):
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(CommandHandler('author', self.author))
        self.dispatcher.add_handler(CommandHandler('quiz', self.quiz, pass_args=True))
        self.dispatcher.add_handler(CommandHandler('bar', self.bar, pass_args=True))
        self.dispatcher.add_handler(CommandHandler('pie', self.pie, pass_args=True))
        self.dispatcher.add_handler(CommandHandler('report', self.report))

    def init(self):
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.add_commands()
        file = open("graph.p", "rb")
        self.graph = pickle.load(file)
        file.close()
        if isfile(self.TALKER_PICKLE_PATH):
            file = open(self.TALKER_PICKLE_PATH, 'rb')
            self.answers_data = pickle.load(file)
            file.close()
        self.updater.start_polling()

    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Hola soc un robot d'enquestes, enviam /help per veure "
                                                              "el que puc fer!")

    @staticmethod
    def help(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="*Ajuda del chatbot de enquestes*\n"
                                                              "/start: inicialitza el bot\n"
                                                              "/help: mostra la pantalla d'ajuda actual amb la "
                                                              "descripcio de cada comanda\n "
                                                              "/author: mostra la descripcio de l'autor de la "
                                                              "aplicacio\n "
                                                              "/quiz <idEnquesta> donat el identificador de una "
                                                              "encuesta especifica, "
                                                              "s'initializa la secuencia de preguntes\n"
                                                              "/bar <idPregunta> donat el identificador de una "
                                                              "pregunta especifica es mostra "
                                                              "un diagrama de barres cada resposta de "
                                                              "la pregunta seleccionada i la quantitat de "
                                                              "cada resposta\n"
                                                              "/pie <idPregunta> donat el identificador de una "
                                                              "pregunta especifica es mostra "
                                                              "un diagrama de formatget similar al diagrama "
                                                              "de barres nomes que amb un altre tipus de "
                                                              "visualitzacio\n "
                                                              "/report mostra las estadistiques de totes les "
                                                              "preguntes\n",
                         parse_mode=ParseMode.MARKDOWN)

    @staticmethod
    def author(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text="Pol Monroig Company\npol.monroig@est.fib.upc.edu")

    def update_answers(self):
        if self.node in self.answers_data:
            if self.answer in self.answers_data[self.node]:
                self.answers_data[self.node][self.answer] += 1
            else:
                self.answers_data[self.node][self.answer] = 1
        else:
            self.answers_data[self.node] = {self.answer: 1}

    def good_answer(self):
        answer_index = self.find_node_by_type("answer")
        for answer in self.graph.nodes[answer_index]['content']:
            if answer[0] == self.answer:
                return True
        return False

    def read_answer(self, bot, update):
        msg = update.message.text
        if self.quiz_started:
            self.answer = msg
            if self.good_answer():
                self.update_answers()
                question = self.get_question()
                if question is not None:
                    bot.send_message(chat_id=update.message.chat_id, text=question)
                else:
                    bot.send_message(chat_id=update.message.chat_id, text=self.poll_id + "> Gràcies pel teu temps!")
                    # reset bot state
                    self.answer = None
                    self.quiz_started = False
                    # save bot data
                    file = open("talker.p", "wb")
                    pickle.dump(self.answers_data, file)
                    file.close()
            else:
                bot.send_message(chat_id=update.message.chat_id, text="Esa no es una respuesta valida")

    def find_node_by_type(self, node_type):
        for i in self.successors:
            if self.graph.nodes[i]['type'] == node_type:
                return i
        raise LookupError("Index of identifier not found,\n tip: "
                          "check the correct syntax of the language")

    def find_alternative_with_answer(self):
        for i in self.successors:
            node_type = self.graph.nodes[i]['type']
            if node_type and self.graph.nodes[i]['type'] == "question":
                edge = self.graph.edges[self.node, i]
                if 'content' in edge:
                    content = self.graph.edges[self.node, i]['content']
                    if content == self.answer:
                        return i
        return None

    def get_question_string(self):
        """
        Generates a string for the current question-answer pair
        :return: a string with the question and the possible answers
        """
        question = self.poll_id + ">" + self.graph.nodes[self.node]['content']
        answer_index = self.find_node_by_type("answer")
        for answer in self.graph.nodes[answer_index]['content']:
            question += "\n" + answer[0] + ": " + answer[1]
        return question

    def in_alternative_branch(self):
        """
        Determines if we are in a alternative edge(branch)
        :return: if we have saved a reference to the main branch
        """
        return self.node_stack is not None

    def reset_node(self):
        """
        Resets the node to the main branch
        """
        self.node = self.node_stack
        self.node_stack = None
        self.update()

    def is_poll_end(self):
        """
        Determines if the current poll has ended
        :return: if the next question does not exist
        """
        return self.successors[0] == "END"

    def get_question(self):
        """
               Get question has all the logic of the graph navigability,
               it works by defining a node element that represents the current node
               we move this node around and if we go to an alternative question (branch)
               we save the node.
               Given a node P of a poll the ordering of its successors is
               [Pi, Ri, Ai, .., An]
               if P is a final node, meaning that is the last question then
               Pi = END

               Given a node P that is not in a poll then the ordering of its successors is
               [Ri, Ai, .., An]


        """
        # update node

        alternative_index = self.find_alternative_with_answer()
        if alternative_index is not None:  # node alternative has been found
            if not self.in_alternative_branch():  # if we are in the main branch we must save the context
                self.node_stack = self.node
            self.node = alternative_index  # move to alternative branch
            self.update()
        elif self.in_alternative_branch():  # no alternative, move back to main branch
            self.reset_node()
            if self.is_poll_end():  # no more questions in poll
                return None
        else:
            if self.is_poll_end():  # no more questions in poll
                return None
            self.next()

        # get display_text
        display_text = self.get_question_string()
        return display_text

    def update(self):
        self.successors = list(self.graph.successors(self.node))

    def next(self):
        """
        Advance the node to the next question
        """
        self.node = self.find_node_by_type("question")
        self.successors = list(self.graph.successors(self.node))

    def quiz(self, bot, update, args):
        self.quiz_started = True
        self.poll_id = args[0]
        # find first question
        self.node = self.poll_id
        self.update()
        self.next()
        if self.graph.has_node(self.poll_id):
            bot.send_message(chat_id=update.message.chat_id, text="Enquesta " + self.poll_id + ":")

            # display question
            question = self.get_question_string()
            bot.send_message(chat_id=update.message.chat_id, text=question)
            # read answer
            self.dispatcher.add_handler(MessageHandler(Filters.text, self.read_answer))

        else:
            bot.send_message(chat_id=update.message.chat_id, text="La enquesta seleccionada no existeix")

    def save_bar_plot(self, question_id):
        names = list(self.answers_data[question_id].keys())
        values = list(self.answers_data[question_id].values())
        plt.clf()
        plt.bar(names, values)
        plt.savefig("bar.png")

    def save_pie_plot(self, question_id):
        names = list(self.answers_data[question_id].keys())
        values = list(self.answers_data[question_id].values())
        plt.clf()
        plt.pie(values, labels=names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.savefig("pie.png")

    def bar(self, bot, update, args):
        question_id = args[0]
        if question_id not in self.answers_data:
            bot.send_message(chat_id=update.message.chat_id, text="No hi ha dades per la pregunta seleccionada")
        elif self.graph.has_node(question_id):
            self.save_bar_plot(question_id)
            file = open('bar.png', 'rb')
            bot.send_photo(chat_id=update.message.chat_id,
                           photo=file)
            file.close()
        else:
            bot.send_message(chat_id=update.message.chat_id, text="La pregunta seleccionada no existeix")

    def pie(self, bot, update, args):
        question_id = args[0]
        if question_id not in self.answers_data:
            bot.send_message(chat_id=update.message.chat_id, text="No hi ha dades per la pregunta seleccionada")
        elif self.graph.has_node(question_id):
            self.save_pie_plot(question_id)
            file = open('pie.png', 'rb')
            bot.send_photo(chat_id=update.message.chat_id,
                           photo=file)
            file.close()
        else:
            bot.send_message(chat_id=update.message.chat_id, text="La pregunta seleccionada no existeix")

    def report(self, bot, update):
        text = "*pregunta valor respostes*\n"
        for item in self.answers_data.items():
            for answer in item[1].items():
                text += item[0] + " " + answer[0] + " " + str(answer[1]) + "\n"
        bot.send_message(chat_id=update.message.chat_id, text=text,
                         parse_mode=ParseMode.MARKDOWN)
