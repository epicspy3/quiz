#Variables:
score = wrong = 0 #Default is 0
questnum = 0 #questionnumber
#Lists:
answerlist = [] #user answers
scorevaluelist = ["d","b","c","d","b","c","b","d","a","c","b","a","b","b","b"] #actual answers
possibleanswerlist = ["a","b","c","d"] #possible answers

def question():
    global score, wrong, questnum, possibleanswerlist
    while questnum < 15: #While loop for 15 questions (number can be changed if necessary)
        print ("Question",questnum+1) #Question number
        listofquestions = open("version 2 questions","r")
        lines = listofquestions.readlines()
        print (lines[questnum*5]+
               lines[questnum*5+1]+
               lines[questnum*5+2]+
               lines[questnum*5+3]+
               lines[questnum*5+4]) #Prints question and answer options
        question = input("") #Empty input because question included above
        if question.lower() == scorevaluelist[questnum]: #Correct answer
            print ("You got the question right!")
            score += 1
            questnum += 1
            answerlist.append(True) #Adds user answer to Answerlist
        elif question.lower() in possibleanswerlist: #if user answered correctly this elif would not run
            print ("You got the question wrong!")
            wrong += 1
            questnum += 1
            answerlist.append(False) #Adds answer to Answerlist
        else: #invalid answer
            print ("Please enter true or false.")
        listofquestions.close()

def finalscore():
    global score, wrong, questnum
    print ("""
\
\
You have finished the quiz.
You got""",score,"questions correct and",wrong,"""questions wrong.
Here is what you got for each question:
""")
    questnum = 0
    for i in answerlist: #i is placeholder
        if answerlist[questnum] == True: #Prints out which questions user got correct and incorrect
            print ("You got question",questnum+1,"correct.")
        else:
            print ("You got question",questnum+1,"incorrect.")
        questnum += 1
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
