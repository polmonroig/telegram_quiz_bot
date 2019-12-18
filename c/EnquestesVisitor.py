# Generated from Enquestes.g4 by ANTLR 4.5.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):

    def __init__(self):
        self.question_ids = []
        self.answer_ids = []
        self.alternative_ids = []
        self.item_pairs = {}
        self.poll_ids = []
        self.poll_item_list = []

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#expression.
    def visitExpression(self, ctx:EnquestesParser.ExpressionContext):
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
        self.item_pairs[str(ctx.identifier().ID())] = (str(ctx.questionId().ID()), str(ctx.answerId().ID()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternative.
    def visitAlternative(self, ctx:EnquestesParser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternativeAnswer.
    def visitAlternativeAnswer(self, ctx:EnquestesParser.AlternativeAnswerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#innerAlt.
    def visitInnerAlt(self, ctx:EnquestesParser.InnerAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#identifier.
    def visitIdentifier(self, ctx:EnquestesParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#itemIds.
    def visitItemIds(self, ctx:EnquestesParser.ItemIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#poll.
    def visitPoll(self, ctx:EnquestesParser.PollContext):
        self.poll_ids.append(ctx.identifier().ID())
        self.poll_item_list.append(ctx.itemIds().STRING())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#end.
    def visitEnd(self, ctx:EnquestesParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#questionId.
    def visitQuestionId(self, ctx:EnquestesParser.QuestionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#answerId.
    def visitAnswerId(self, ctx:EnquestesParser.AnswerIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#numeratedAnswer.
    def visitNumeratedAnswer(self, ctx:EnquestesParser.NumeratedAnswerContext):
        return self.visitChildren(ctx)



del EnquestesParser