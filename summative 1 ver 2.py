#Variables:
score = wrong = 0
questionnumber = 0
#Lists:
answerlist = [] #user answers
scorevaluelist = ["d","b","c","d","b","c","b","d","a","c","b","a","b","b","b"] #actual answers
possibleanswerlist = ["a","b","c","d"] #possible answers

def question():
    global score, wrong, questionnumber, possibleanswerlist
    while questionnumber < 15: #While loop for 15 questions (number can be changed if necessary)
        print ("Question",questionnumber+1) #Question number
        listofquestions = open("version 2 questions","r")
        lines = listofquestions.readlines()
        print (lines[questionnumber*5]+lines[questionnumber*5+1]+lines[questionnumber*5+2]+lines[questionnumber*5+3]+lines[questionnumber*5+4])
        question = input("") #References the Question List and item in the list
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
        listofquestions.close()

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
