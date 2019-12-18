grammar Enquestes;  // initial rule


// parser rules

root : expression end EOF;



expression : expression expression
            | question | answer | item | alternative | poll;

itemIds : ID;
identifier : ID;

text : (STRING | ID);

question : identifier COLON 'PREGUNTA' text;
questionId : ID;
answerId : ID;


answer : identifier COLON 'RESPOSTA' numeratedAnswer+;
item : identifier COLON 'ITEM' questionId ARROW answerId;

alternative :  identifier COLON 'ALTERNATIVA'
               identifier '[' alternativeAnswer ']';

alternativeAnswer : innerAlt | innerAlt ',' alternativeAnswer;
innerAlt : '(' NUMBER ',' identifier ')';



poll : identifier COLON 'ENQUESTA' itemIds+;

end : 'END';


numeratedAnswer : NUMBER COLON text SEMICOLON;




// lexer rules
NUMBER : [0-9]+;
ACCENTS : 'à' | 'á' | 'é' | 'è' | 'í' | 'ì' | 'ó' | 'ò' | 'ú' | 'ù';
ARROW : '->';
ID : ([0-9] | [a-z] | [A-Z] | ACCENTS | '?')+;
STRING : ([0-9] | [a-z] | [A-Z] | ACCENTS | '?')+ ' '* STRING | ([0-9] | [a-z] | [A-Z] | ACCENTS | '?')+;
COLON : ':';
SEMICOLON : ';';




// Skip tokens
WS : [ \n\t]+ -> skip;
COMMENT : '/*' .*? '*/' -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;