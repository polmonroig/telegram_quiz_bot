grammar Enquestes;  // initial rule


// parser rules

root : expression end EOF;



expression : expression expression
            | question | answer | item | alternative | poll;




text : (STRING | ID);

question : identifier COLON 'PREGUNTA' text;



answer : identifier COLON 'RESPOSTA' numeratedAnswer+;
item : identifier COLON 'ITEM' questionId ARROW answerId;

alternative :  identifier COLON 'ALTERNATIVA'
               identifier '[' alternativeAnswer ']';

alternativeAnswer : innerAlt | innerAlt ',' alternativeAnswer;
innerAlt : '(' NUMBER ',' identifier ')';

identifier : ID;
itemIds : ID;
poll : identifier COLON 'ENQUESTA' itemIds+;

end : 'END';

questionId : ID;
answerId : ID;

numeratedAnswer : NUMBER COLON text SEMICOLON;




// lexer rules
ARROW : '->';
NUMBER : [0-9]+;
ID: ([0-9] | [a-z] | [A-Z] | [\u0080-\u00FF])+;
STRING : ([0-9] | [a-z] | [A-Z] | [\u0080-\u00FF] | '?')+ ' '* STRING | ([0-9] | [a-z] | [A-Z] | [\u0080-\u00FF] | '?')+;
COLON : ':';
SEMICOLON : ';';




// Skip tokens
WS : [ \n\t]+ -> skip;
COMMENT : '/*' .*? '*/' -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;