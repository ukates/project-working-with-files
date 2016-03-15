#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random, os
os.makedirs(os.path.join('answers'), exist_ok=True) #creates folder titled Answers, if folder already exists it returns true so that the program can continue. 
os.makedirs(os.path.join('quizzes'), exist_ok=True) #creates folder for Quizzes

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 
            'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(5):
                    
    quizFile = open('./quizzes/capitalsquiz%s.txt' % (quizNum + 1), 'w') #this opens the random quiz files, and assignes them to the ./quizzes directory.) 
    answerKeyFile = open('./answers/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w') #opens random answer files that correspond with quizzes and assignes to answers folder/ directory. 

       # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

       # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50): # gives range from 1 to 50 
        correctAnswer = capitals[states[questionNum]] #selects the correct answer from the capitals directory assigns it to correctAnswer
        wrongAnswers = list(capitals.values()) # wrong answers from the capitals directory assigns to wrongAnswers
        del wrongAnswers[wrongAnswers.index(correctAnswer)] 
        wrongAnswers = random.sample(wrongAnswers, 3) #chooses 3 random wrong answers from directory 
        answerOptions = wrongAnswers + [correctAnswer] #these are the options you have 1-4 on the test, one is correct three are wrong. 
        random.shuffle(answerOptions) #shuffles the answers so that each version of quiz is different. 


        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum])) #this writes out the question taking a random state

        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i])) #assigns a b c d to answers 

            quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()




   
    

    #todo: create folder titled quizzes and one titled answers
    #write out the header for the quiz
    #shuffel the order of the states
    #Loop through all 50 states, making a question for each.

            #TODO: follow the 'generating random quiz files' project in the textbook to fill in this file.
            #TODO: however, make the following modificatiosn to the instructions on the textbook:
            #       1. instead of making 35 quiz versions, you'll only make 5 quiz versions
            #       2. instead of creating quiz and answer files in the current working directory, create a folder titled 'quizzes' and another folder titled 'answers'.
            #       3. place the randomly-generated quizzes in the 'quizzes' directory.
            #       4. plaec the corresponding answers in the 'answers' directory.
            
            
