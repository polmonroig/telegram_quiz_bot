# Telegram QuizBot #

This is a telegram chatbot design to make polls/quiz to people and save its results. 

## Getting Started ##
To use the chatbot you first need to design a language like the one in the file c/language 
then you need to compile the language using the script in c/test.main.py. Finally to initialize the chatbot
you need to run bot/bot.py. 

### Requirements ###
First you need to install the requirements file, taking into account you need Python3 

```
pip install -r requirements.txt  
```
Second you need to create a poll in a text file like the following example.
```
P1: PREGUNTA                         // Question with identifier P1
Quants adults viuen a casa teva?
P2: PREGUNTA                         // Another question 
Quants menors vien a casa teva?
R1: RESPOSTA                         // Answer with identifier R1
0: zero ;                            // First option for answer R1
1: un ;
2: dos ;
3: més de dos ;
I1: ITEM                             // Item: connects a question with an answer
P1 -> R1                            
I2: ITEM
P2 -> R1
P3: PREGUNTA
Com vas a la feina majoritàriament?
R3: RESPOSTA
1: caminant ;
2: en cotxe ;
3: en transport públic ;
I3: ITEM
P3 -> R3
P4: PREGUNTA
Utilitzes car sharing?
R4: RESPOSTA
1: Si ;
2: No ;
I4: ITEM
P4 -> R4
P5: PREGUNTA
Quin mitja de transport utilitzes majoritàriament?
R5: RESPOSTA
1: Tren ;
2: Bus ;
3: Metro ;
4: Altres;
I5: ITEM
P5 -> R5
A1: ALTERNATIVA                      // An answer in I3 implies another answer 
I3 [(2,I4),(3,I5)]                   // another question
E: ENQUESTA                          // List of questions of a quiz
I1 I2 I3
END
``` 

Then you need to run the test.main.py file in the c folder where file is the file where the 
quiz has been written 
```
python c/test.main.py file
```
This will create a pickle file in the bot folder called graph.p,
this file contains the quiz structure in a graph. 
Finally to run the bot you need to initialize it using 
```
python bot/bot.py  
```

## Deployment ##
To the deploy the application it is necessary to acquire a token for a telegram bot with BotFather.  

## Author ##
Pol Monroig Company 