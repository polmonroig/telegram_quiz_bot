grammar Enquestes;  // initial rule


// parser rules

root : expression end EOF;



expression : expression expression
            | question | answer | item | alternative | poll;

identifier : ID;
text : (STRING | ID);

question : identifier COLON 'PREGUNTA' text;



answer : identifier COLON 'RESPOSTA' numeratedAnswer+;
item : identifier COLON 'ITEM' identifier ARROW identifier;

alternative :  identifier COLON 'ALTERNATIVA'
               identifier '[' alternativeAnswer ']';

alternativeAnswer : innerAlt | innerAlt ',' alternativeAnswer;
innerAlt : '(' NUMBER ',' identifier ')';

poll : identifier COLON 'ENQUESTA' identifier+;

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