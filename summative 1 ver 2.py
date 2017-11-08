#Variables:
score = wrong = 0
questionnumber = 0

#Lists:
questionlist = ["""What is 9+10?
a. 18
b. 19
c. 20
d. 21
""",
"""When did the Cassini spacecraft plunge into Saturn's atmosphere (UTC)?
a. 9/14/17
b. 9/15/17
c. 9/16/17
d. 9/17/17
""",
"""How did Stephen Hawking lose his voice?
a. ALS
b. Cancer
c. Pneumonia
d. STDs
""",
"""What is the last dynasty of China?
a. Ming
b. Song
c. Tang
d. Qing
""",
"""What mathematical symbol is used for summation?
a. Exponent
b. Sigma
c. Sqrt
d. Factorial
""",
"""What is the most expensive property in the American version of Monopoly?
a. Park Place
b. Illinois Ave
c. Boardwalk
d. Mediterranean Ave
""",
"""How many lines does the MTR consist of?
a. 10
b. 11
c. 12
d. 13
""",
"""What is the most viewed video on YouTube?
a. Shape of You
b. Gangnam Style
c. Baby
d. Despacito
""",
"""How many member states are in the UN?
a. 193
b. 194
c. 195
d. 196
""",
"""Which ferry connects Lower Manhattan to Staten Island?
a. North Ferry
b. West Ferry
c. South Ferry
d. East Ferry
""",
"""What is HK's flagship airline?
a. Dragonair
b. Cathay Pacific Airways
c. Hong Kong Airlines
d. Hong Kong Express
""",
"""What is the practical maximum output for a 56K modem?
a. 48 kbit/s
b. 50 kbit/s
c. 52 kbit/s
d. 54 kbit/s
""",
"""When were the first gravitational waves detected?
a. 9/13/15
b. 9/14/15
c. 9/15/15
d. 9/16/15
""",
"""What is ax^2 + bx + c called?
a. Vertex Form
b. Standard Form
c. Intercept Form
d. Point-Slope Form
""",
"""What subway system has the most amount of stations in the world?
a. Beijing Subway
b. NYC Subway
c. Taipei Metro
d. Tokyo Metro
"""] #List of multiple choice questions
answerlist = [] #user answers
scorevaluelist = ["d","b","c","d","b","c","b","d","a","c","b","a","b","b","b"] #actual answers
possibleanswerlist = ["a","b","c","d"] #possible answers

def question():
    global score, wrong, questionnumber, possibleanswerlist
    while questionnumber < 15: #While loop for 15 questions (number can be changed if necessary)
        print ("Question",questionnumber+1) #Question number
        question = str(input(questionlist[questionnumber])).lower() #References the Question List and item in the list
        if question.lower() == scorevaluelist[questionnumber]: #Correct answer
            print ("You got the question right!")
            score += 1
            questionnumber += 1
            answerlist.append(True) #Adds user answer to Answerlist
        elif question.lower() in possibleanswerlist: #if user answered correctly this elif would not run
            print ("You got the question wrong!")
            wrong += 1
            questionnumber += 1
            answerlist.append(False) #Adds answer to Answerlist
        else: #invalid answer
            print ("Please enter true or false.")

def finalscore():
    global score, wrong, questionnumber
    print ("""
\
\
You have finished the quiz.
You got""",score,"questions correct and",wrong,"""questions wrong.
Here is what you got for each question:
""")
    questionnumber = 0
    for i in answerlist: #i is placeholder
        if answerlist[questionnumber] == True: #Prints out which questions user got correct and incorrect
            print ("You got question",questionnumber+1,"correct.")
        else:
            print ("You got question",questionnumber+1,"incorrect.")
        questionnumber += 1
    print ("Thanks for playing the quiz!")

#start of game
print ("""
Welcome to the quiz.
There are four choices for each question. Please input one.
That's all.
""")
#run functions
question()
finalscore()
