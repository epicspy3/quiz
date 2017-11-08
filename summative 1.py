#Variables:
score = wrong = 0
questionnumber = 0

#Lists:
questionlist = ["9+10 is 21.",
"The best 3x3 speedcube is the YJ Guanlong.",
"Voyager 1 blasted off from Earth before Voyager 2.",
"Mr Dratz is not boring.",
"Black holes emit Hawking radiation.",
"""Question 1 was not not not not not not not not not not
not not not not not not not not not not false.""",
"Mr Davis plays the drum.",
"Despacito is the most viewed video on YouTube.",
"The Vatican City is a UN member state.",
"Tetris was originally coded by an American.",
"Airlines are not able to make their own tracks for flights across the Atlantic.",
"The second last Chinese dynasty was the Song dynasty.",
"Gravitational waves have never been detected before.",
"ax^2 + bx + c is called vertex form.",
"The NYC Subway has the most amount of stations in the world."
] #List of true/false statements
answerlist = [] #user answers
scorevaluelist = ["true","false","false","false","true","true","true","true","false","false","true","false","false","false","true"] #actual answers
possibleanswerlist = ["true","false"]

def question():
    global score, wrong, questionnumber
    while questionnumber < 15: #While loop for 15 questions (number can be changed if necessary)
        print ("Question",questionnumber+1) #Question number
        question = input(questionlist[questionnumber]) #References the Question List and item in the list
        question = str(question) #makes sure it's a string
        if question.lower() == scorevaluelist[questionnumber]: #Correct answer
            print ("You got the question right!")
            score += 1
            questionnumber += 1
            answerlist.append("correct") #Adds user answer to Answerlist
        elif question.lower() == possibleanswerlist: #if user answered correctly this elif would not run
            print ("You got the question wrong!")
            wrong += 1
            questionnumber += 1
            answerlist.append("incorrect") #Adds answer to Answerlist
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
        if answerlist[questionnumber] == "correct": #Prints out which questions user got correct and incorrect
            print ("You got question",questionnumber+1,"correct.")
        else:
            print ("You got question",questionnumber+1,"incorrect.")
        questionnumber += 1
    print ("Thanks for playing the quiz!")

#start of game
print ("""
Welcome to the quiz.
Just enter true/false for each statement. That's all.
""")
#run functions
question()
finalscore()
