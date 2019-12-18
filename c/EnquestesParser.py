# Generated from Enquestes.g4 by ANTLR 4.5.2
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\27")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\'\n\3")
        buf.write("\3\3\3\3\7\3+\n\3\f\3\16\3.\13\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\6\7=\n\7\r\7\16\7>\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\5\nU\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\6\fa\n\f\r\f\16\fb\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\2\3\4\17\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\2\3\3\2\21\22f\2\34\3\2\2\2\4&\3\2\2\2")
        buf.write("\6/\3\2\2\2\b\61\3\2\2\2\n\63\3\2\2\2\f8\3\2\2\2\16@\3")
        buf.write("\2\2\2\20G\3\2\2\2\22T\3\2\2\2\24V\3\2\2\2\26\\\3\2\2")
        buf.write("\2\30d\3\2\2\2\32f\3\2\2\2\34\35\5\4\3\2\35\36\5\30\r")
        buf.write("\2\36\37\7\2\2\3\37\3\3\2\2\2 !\b\3\1\2!\'\5\n\6\2\"\'")
        buf.write("\5\f\7\2#\'\5\16\b\2$\'\5\20\t\2%\'\5\26\f\2& \3\2\2\2")
        buf.write("&\"\3\2\2\2&#\3\2\2\2&$\3\2\2\2&%\3\2\2\2\',\3\2\2\2(")
        buf.write(")\f\b\2\2)+\5\4\3\t*(\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3")
        buf.write("\2\2\2-\5\3\2\2\2.,\3\2\2\2/\60\7\21\2\2\60\7\3\2\2\2")
        buf.write("\61\62\t\2\2\2\62\t\3\2\2\2\63\64\5\6\4\2\64\65\7\23\2")
        buf.write("\2\65\66\7\3\2\2\66\67\5\b\5\2\67\13\3\2\2\289\5\6\4\2")
        buf.write("9:\7\23\2\2:<\7\4\2\2;=\5\32\16\2<;\3\2\2\2=>\3\2\2\2")
        buf.write("><\3\2\2\2>?\3\2\2\2?\r\3\2\2\2@A\5\6\4\2AB\7\23\2\2B")
        buf.write("C\7\5\2\2CD\5\6\4\2DE\7\20\2\2EF\5\6\4\2F\17\3\2\2\2G")
        buf.write("H\5\6\4\2HI\7\23\2\2IJ\7\6\2\2JK\5\6\4\2KL\7\7\2\2LM\5")
        buf.write("\22\n\2MN\7\b\2\2N\21\3\2\2\2OU\5\24\13\2PQ\5\24\13\2")
        buf.write("QR\7\t\2\2RS\5\22\n\2SU\3\2\2\2TO\3\2\2\2TP\3\2\2\2U\23")
        buf.write("\3\2\2\2VW\7\n\2\2WX\7\16\2\2XY\7\t\2\2YZ\5\6\4\2Z[\7")
        buf.write("\13\2\2[\25\3\2\2\2\\]\5\6\4\2]^\7\23\2\2^`\7\f\2\2_a")
        buf.write("\5\6\4\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\27\3")
        buf.write("\2\2\2de\7\r\2\2e\31\3\2\2\2fg\7\16\2\2gh\7\23\2\2hi\5")
        buf.write("\b\5\2ij\7\24\2\2j\33\3\2\2\2\7&,>Tb")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PREGUNTA'", "'RESPOSTA'", "'ITEM'", 
                     "'ALTERNATIVA'", "'['", "']'", "','", "'('", "')'", 
                     "'ENQUESTA'", "'END'", "<INVALID>", "<INVALID>", "'->'", 
                     "<INVALID>", "<INVALID>", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "ACCENTS", "ARROW", "ID", "STRING", "COLON", 
                      "SEMICOLON", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_root = 0
    RULE_expression = 1
    RULE_identifier = 2
    RULE_text = 3
    RULE_question = 4
    RULE_answer = 5
    RULE_item = 6
    RULE_alternative = 7
    RULE_alternativeAnswer = 8
    RULE_innerAlt = 9
    RULE_poll = 10
    RULE_end = 11
    RULE_numeratedAnswer = 12

    ruleNames =  [ "root", "expression", "identifier", "text", "question", 
                   "answer", "item", "alternative", "alternativeAnswer", 
                   "innerAlt", "poll", "end", "numeratedAnswer" ]

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
    NUMBER=12
    ACCENTS=13
    ARROW=14
    ID=15
    STRING=16
    COLON=17
    SEMICOLON=18
    WS=19
    COMMENT=20
    LINE_COMMENT=21

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
            self.state = 26
            self.expression(0)
            self.state = 27
            self.end()
            self.state = 28
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
            self.state = 36
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 31
                self.question()
                pass

            elif la_ == 2:
                self.state = 32
                self.answer()
                pass

            elif la_ == 3:
                self.state = 33
                self.item()
                pass

            elif la_ == 4:
                self.state = 34
                self.alternative()
                pass

            elif la_ == 5:
                self.state = 35
                self.poll()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EnquestesParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 38
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 39
                    self.expression(7) 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 6, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
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
        self.enterRule(localctx, 8, self.RULE_question)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.identifier()
            self.state = 50
            self.match(EnquestesParser.COLON)
            self.state = 51
            self.match(EnquestesParser.T__0)
            self.state = 52
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
        self.enterRule(localctx, 10, self.RULE_answer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.identifier()
            self.state = 55
            self.match(EnquestesParser.COLON)
            self.state = 56
            self.match(EnquestesParser.T__1)
            self.state = 58 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 57
                    self.numeratedAnswer()

                else:
                    raise NoViableAltException(self)
                self.state = 60 
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def ARROW(self):
            return self.getToken(EnquestesParser.ARROW, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.identifier()
            self.state = 63
            self.match(EnquestesParser.COLON)
            self.state = 64
            self.match(EnquestesParser.T__2)
            self.state = 65
            self.identifier()
            self.state = 66
            self.match(EnquestesParser.ARROW)
            self.state = 67
            self.identifier()
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
        self.enterRule(localctx, 14, self.RULE_alternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.identifier()
            self.state = 70
            self.match(EnquestesParser.COLON)
            self.state = 71
            self.match(EnquestesParser.T__3)
            self.state = 72
            self.identifier()
            self.state = 73
            self.match(EnquestesParser.T__4)
            self.state = 74
            self.alternativeAnswer()
            self.state = 75
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
        self.enterRule(localctx, 16, self.RULE_alternativeAnswer)
        try:
            self.state = 82
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.innerAlt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.innerAlt()
                self.state = 79
                self.match(EnquestesParser.T__6)
                self.state = 80
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
        self.enterRule(localctx, 18, self.RULE_innerAlt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(EnquestesParser.T__7)
            self.state = 85
            self.match(EnquestesParser.NUMBER)
            self.state = 86
            self.match(EnquestesParser.T__6)
            self.state = 87
            self.identifier()
            self.state = 88
            self.match(EnquestesParser.T__8)
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(EnquestesParser.COLON, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_poll




    def poll(self):

        localctx = EnquestesParser.PollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_poll)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.identifier()
            self.state = 91
            self.match(EnquestesParser.COLON)
            self.state = 92
            self.match(EnquestesParser.T__9)
            self.state = 94 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 93
                    self.identifier()

                else:
                    raise NoViableAltException(self)
                self.state = 96 
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
        self.enterRule(localctx, 22, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(EnquestesParser.T__10)
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
        self.enterRule(localctx, 24, self.RULE_numeratedAnswer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(EnquestesParser.NUMBER)
            self.state = 101
            self.match(EnquestesParser.COLON)
            self.state = 102
            self.text()
            self.state = 103
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
         




