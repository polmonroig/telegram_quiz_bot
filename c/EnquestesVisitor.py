# Generated from Enquestes.g4 by ANTLR 4.7.2
from antlr4 import *
import networkx as nx
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.




class EnquestesVisitor(ParseTreeVisitor):

    def __init__(self):
        G = nx.Graph()
        self.question_ids = []
        self.answer_ids = []
        self.alternative_ids = []
        self.item_ids = []
        self.poll_ids = []

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#expression.
    def visitExpression(self, ctx:EnquestesParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#identifier.
    def visitIdentifier(self, ctx:EnquestesParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#text.
    def visitText(self, ctx:EnquestesParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#question.
    def visitQuestion(self, ctx:EnquestesParser.QuestionContext):

        self.question_ids.append(ctx.identifier().ID())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#answer.
    def visitAnswer(self, ctx:EnquestesParser.AnswerContext):

        self.answer_ids.append(ctx.identifier().ID())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        item = ctx.identifier()[0].ID()



        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#alternative.
    def visitAlternative(self, ctx:EnquestesParser.AlternativeContext):

        self.alternative_ids.append(ctx.identifier())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternativeAnswer.
    def visitAlternativeAnswer(self, ctx:EnquestesParser.AlternativeAnswerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#innerAlt.
    def visitInnerAlt(self, ctx:EnquestesParser.InnerAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#poll.
    def visitPoll(self, ctx:EnquestesParser.PollContext):
        self.poll_ids.append(ctx.identifier())
        child = ctx.getChild(3)
        print(child.getChildCount())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#end.
    def visitEnd(self, ctx:EnquestesParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#numeratedAnswer.
    def visitNumeratedAnswer(self, ctx:EnquestesParser.NumeratedAnswerContext):
        return self.visitChildren(ctx)





del EnquestesParser