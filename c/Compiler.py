import sys
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from EnquestesVisitor import EnquestesVisitor
from NetworkGenerator import NetworkGenerator
import codecs


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
        print(self.tree.toStringTree(recog=parser))

    def visit(self):
        visitor = EnquestesVisitor()
        visitor.visitRoot(self.tree)  # save questions and things

        for q in visitor.question_ids:
            self.generator.add_node(q)

        for p in visitor.poll_ids:
            self.generator.add_node(p)

        for a in visitor.answer_ids:
            self.generator.add_node(a)

        self.generator.draw()


