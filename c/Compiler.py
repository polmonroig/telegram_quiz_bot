import sys
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from EnquestesVisitor import EnquestesVisitor
from NetworkGenerator import NetworkGenerator
import pickle


class Compiler:
    def __init__(self):
        self.text = None
        self.tree = None
        self.generator = NetworkGenerator()

    def read(self):
        file = open(sys.argv[1], encoding='utf-8')
        self.text = InputStream(file.read())

        file.close()

    def parse(self):
        lexer = EnquestesLexer(self.text)
        token_stream = CommonTokenStream(lexer)
        parser = EnquestesParser(token_stream)
        self.tree = parser.root()


    def visit(self):
        visitor = EnquestesVisitor()
        visitor.visitRoot(self.tree)  # save questions and things

        # add base nodes
        for q in visitor.question_ids:
            self.generator.add_node(q, "")

        for a in visitor.answer_ids:
            self.generator.add_node(a, "")

        # add the end node
        self.generator.add_node("END")

        # add poll relationships
        for poll_id, item_list in zip(visitor.poll_ids, visitor.poll_item_list):
            self.generator.add_node(poll_id)
            items_ids = str(item_list).split()
            items = []
            for id in items_ids:
                items.append(visitor.item_pairs[id])

            self.generator.add_poll_edge(str(poll_id), items[0][0])
            for i in range(1, len(items)):
                self.generator.add_poll_edge(items[i - 1][0], items[i][0])
            self.generator.add_poll_edge(items[-1][0], 'END')

        # add item edges
        for pair in visitor.item_pairs.items():
            self.generator.add_item_edge(pair[1][0], pair[1][1], pair[0])

        # add alternative edges
        for alt in visitor.alternative_pairs.items():
            questionId = visitor.item_pairs[alt[0]][0]
            for a in alt[1]:
                self.generator.add_alt_edge(questionId, visitor.item_pairs[a[1]][0], a[0])

        self.generator.draw()


    def save_graph(self):
        pickle.dump( self.generator, open( "GraphGenerator.p", "wb" ))

