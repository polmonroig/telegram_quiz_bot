# Generated from Enquestes.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\26")
        buf.write("x\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3-\n\3\3\3\3\3\7\3\61\n\3\f\3\16")
        buf.write("\3\64\13\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\6\6A\n\6\r\6\16\6B\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tY\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\6\ri\n\r\r\r\16\rj\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\2\3\4\22\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \2\3\3\2\20\21o\2\"\3\2\2\2\4")
        buf.write(",\3\2\2\2\6\65\3\2\2\2\b\67\3\2\2\2\n<\3\2\2\2\fD\3\2")
        buf.write("\2\2\16K\3\2\2\2\20X\3\2\2\2\22Z\3\2\2\2\24`\3\2\2\2\26")
        buf.write("b\3\2\2\2\30d\3\2\2\2\32l\3\2\2\2\34n\3\2\2\2\36p\3\2")
        buf.write("\2\2 r\3\2\2\2\"#\5\4\3\2#$\5\32\16\2$%\7\2\2\3%\3\3\2")
        buf.write("\2\2&\'\b\3\1\2\'-\5\b\5\2(-\5\n\6\2)-\5\f\7\2*-\5\16")
        buf.write("\b\2+-\5\30\r\2,&\3\2\2\2,(\3\2\2\2,)\3\2\2\2,*\3\2\2")
        buf.write("\2,+\3\2\2\2-\62\3\2\2\2./\f\b\2\2/\61\5\4\3\t\60.\3\2")
        buf.write("\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\5\3")
        buf.write("\2\2\2\64\62\3\2\2\2\65\66\t\2\2\2\66\7\3\2\2\2\678\5")
        buf.write("\24\13\289\7\22\2\29:\7\3\2\2:;\5\6\4\2;\t\3\2\2\2<=\5")
        buf.write("\24\13\2=>\7\22\2\2>@\7\4\2\2?A\5 \21\2@?\3\2\2\2AB\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2C\13\3\2\2\2DE\5\24\13\2EF\7")
        buf.write("\22\2\2FG\7\5\2\2GH\5\34\17\2HI\7\16\2\2IJ\5\36\20\2J")
        buf.write("\r\3\2\2\2KL\5\24\13\2LM\7\22\2\2MN\7\6\2\2NO\5\24\13")
        buf.write("\2OP\7\7\2\2PQ\5\20\t\2QR\7\b\2\2R\17\3\2\2\2SY\5\22\n")
        buf.write("\2TU\5\22\n\2UV\7\t\2\2VW\5\20\t\2WY\3\2\2\2XS\3\2\2\2")
        buf.write("XT\3\2\2\2Y\21\3\2\2\2Z[\7\n\2\2[\\\7\17\2\2\\]\7\t\2")
        buf.write("\2]^\5\24\13\2^_\7\13\2\2_\23\3\2\2\2`a\7\20\2\2a\25\3")
        buf.write("\2\2\2bc\7\20\2\2c\27\3\2\2\2de\5\24\13\2ef\7\22\2\2f")
        buf.write("h\7\f\2\2gi\5\26\f\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3")
        buf.write("\2\2\2k\31\3\2\2\2lm\7\r\2\2m\33\3\2\2\2no\7\20\2\2o\35")
        buf.write("\3\2\2\2pq\7\20\2\2q\37\3\2\2\2rs\7\17\2\2st\7\22\2\2")
        buf.write("tu\5\6\4\2uv\7\23\2\2v!\3\2\2\2\7,\62BXj")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PREGUNTA'", "'RESPOSTA'", "'ITEM'", 
                     "'ALTERNATIVA'", "'['", "']'", "','", "'('", "')'", 
                     "'ENQUESTA'", "'END'", "'->'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ARROW", "NUMBER", "ID", "STRING", "COLON", "SEMICOLON", 
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_root = 0
    RULE_expression = 1
    RULE_text = 2
    RULE_question = 3
    RULE_answer = 4
    RULE_item = 5
    RULE_alternative = 6
    RULE_alternativeAnswer = 7
    RULE_innerAlt = 8
    RULE_identifier = 9
    RULE_itemIds = 10
    RULE_poll = 11
    RULE_end = 12
    RULE_questionId = 13
    RULE_answerId = 14
    RULE_numeratedAnswer = 15

    ruleNames =  [ "root", "expression", "text", "question", "answer", "item", 
                   "alternative", "alternativeAnswer", "innerAlt", "identifier", 
                   "itemIds", "poll", "end", "questionId", "answerId", "numeratedAnswer" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    ARROW=12
    NUMBER=13
    ID=14
    STRING=15
    COLON=16
    SEMICOLON=17
    WS=18
    COMMENT=19
    LINE_COMMENT=20

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(EnquestesParser.ExpressionContext,0)


        def end(self):
            return self.getTypedRuleContext(EnquestesParser.EndContext,0)


        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_root




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.expression(0)
            self.state = 33
            self.end()
            self.state = 34
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def question(self):
            return self.getTypedRuleContext(EnquestesParser.QuestionContext,0)


        def answer(self):
            return self.getTypedRuleContext(EnquestesParser.AnswerContext,0)


        def item(self):
            return self.getTypedRuleContext(EnquestesParser.ItemContext,0)


        def alternative(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativeContext,0)


        def poll(self):
            return self.getTypedRuleContext(EnquestesParser.PollContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ExpressionContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EnquestesParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 37
                self.question()
                pass

            elif la_ == 2:
                self.state = 38
                self.answer()
                pass

            elif la_ == 3:
                self.state = 39
                self.item()
                pass

            elif la_ == 4:
                self.state = 40
                self.alternative()
                pass

            elif la_ == 5:
                self.state = 41
                self.poll()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EnquestesParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 44
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 45
                    self.expression(7) 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EnquestesParser.STRING, 0)

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_text




    def text(self):

        localctx = EnquestesParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==EnquestesParser.ID or _la==EnquestesParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuestionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_question




    def question(self):

        localctx = EnquestesParser.QuestionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_question)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.identifier()
            self.state = 54
            self.match(EnquestesParser.COLON)
            self.state = 55
            self.match(EnquestesParser.T__0)
            self.state = 56
            self.text()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnswerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def numeratedAnswer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.NumeratedAnswerContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.NumeratedAnswerContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_answer




    def answer(self):

        localctx = EnquestesParser.AnswerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_answer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.identifier()
            self.state = 59
            self.match(EnquestesParser.COLON)
            self.state = 60
            self.match(EnquestesParser.T__1)
            self.state = 62 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 61
                    self.numeratedAnswer()

                else:
                    raise NoViableAltException(self)
                self.state = 64 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def questionId(self):
            return self.getTypedRuleContext(EnquestesParser.QuestionIdContext,0)


        def ARROW(self):
            return self.getToken(EnquestesParser.ARROW, 0)

        def answerId(self):
            return self.getTypedRuleContext(EnquestesParser.AnswerIdContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_item




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.identifier()
            self.state = 67
            self.match(EnquestesParser.COLON)
            self.state = 68
            self.match(EnquestesParser.T__2)
            self.state = 69
            self.questionId()
            self.state = 70
            self.match(EnquestesParser.ARROW)
            self.state = 71
            self.answerId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def alternativeAnswer(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativeAnswerContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternative




    def alternative(self):

        localctx = EnquestesParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_alternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.identifier()
            self.state = 74
            self.match(EnquestesParser.COLON)
            self.state = 75
            self.match(EnquestesParser.T__3)
            self.state = 76
            self.identifier()
            self.state = 77
            self.match(EnquestesParser.T__4)
            self.state = 78
            self.alternativeAnswer()
            self.state = 79
            self.match(EnquestesParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativeAnswerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def innerAlt(self):
            return self.getTypedRuleContext(EnquestesParser.InnerAltContext,0)


        def alternativeAnswer(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativeAnswerContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativeAnswer




    def alternativeAnswer(self):

        localctx = EnquestesParser.AlternativeAnswerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_alternativeAnswer)
        try:
            self.state = 86
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.innerAlt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.innerAlt()
                self.state = 83
                self.match(EnquestesParser.T__6)
                self.state = 84
                self.alternativeAnswer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InnerAltContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(EnquestesParser.NUMBER, 0)

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_innerAlt




    def innerAlt(self):

        localctx = EnquestesParser.InnerAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_innerAlt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(EnquestesParser.T__7)
            self.state = 89
            self.match(EnquestesParser.NUMBER)
            self.state = 90
            self.match(EnquestesParser.T__6)
            self.state = 91
            self.identifier()
            self.state = 92
            self.match(EnquestesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_identifier




    def identifier(self):

        localctx = EnquestesParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemIdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_itemIds




    def itemIds(self):

        localctx = EnquestesParser.ItemIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_itemIds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PollContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def itemIds(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ItemIdsContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ItemIdsContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_poll




    def poll(self):

        localctx = EnquestesParser.PollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_poll)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.identifier()
            self.state = 99
            self.match(EnquestesParser.COLON)
            self.state = 100
            self.match(EnquestesParser.T__9)
            self.state = 102 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 101
                    self.itemIds()

                else:
                    raise NoViableAltException(self)
                self.state = 104 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EndContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EnquestesParser.RULE_end




    def end(self):

        localctx = EnquestesParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(EnquestesParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuestionIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_questionId




    def questionId(self):

        localctx = EnquestesParser.QuestionIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_questionId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnswerIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_answerId




    def answerId(self):

        localctx = EnquestesParser.AnswerIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_answerId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumeratedAnswerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(EnquestesParser.NUMBER, 0)

        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def SEMICOLON(self):
            return self.getToken(EnquestesParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_numeratedAnswer




    def numeratedAnswer(self):

        localctx = EnquestesParser.NumeratedAnswerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_numeratedAnswer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(EnquestesParser.NUMBER)
            self.state = 113
            self.match(EnquestesParser.COLON)
            self.state = 114
            self.text()
            self.state = 115
            self.match(EnquestesParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         




