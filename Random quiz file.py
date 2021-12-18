# Generating a random quiz file
# random quiz generator with question and answers in random order, along with the key answer

import random

    # The quiz data with key as state and value as capital
capitals = {'Abia':'Umuahia','Adamawa':'Yola','Akwa Ibom':'Uyo','Anambra':'Awka','Bauchi':'Bauchi','Bayelsa':'Yenagoa',
            'Benue':'Makurdi','Borno':'Maiduguri','Cross River':'Calabar','Delta':'Asaba','Ebonyi':'Abakaliki','Edo':
            'Benin City','Ekiti':'Ado Ekiti','Enugu':'Enugu','Gombe':'Gombe','Imo':'owerri','Jigawa':'Dutse','Kaduna':
            'Kaduna','Kano':'Kano','Katsina':'Katsina','Kebbi':'Brinin Kebbi','Kogi':'Lokoja','Kwara':'Ilorin','Lagos':
            'Ikeja','Nasarawa':'Lafia','Niger':'Minna','Ogun':'Abeokuta','Ondo':'Akure','Osun':'Oshogbo','Oyo':'Ibadan',
            'Plateau':'Jos','Rivers':'Port Harcourt','Sokoto':'Sokoto','Taraba':'Jalingo','Yobe':'Damaturu','Zamfara':
            'Gusau','FCT':'Abuja'}   
    
    # Generate 35 files
for quizNum in range(35):

# Creat the quiz and answer file
    quizFile = open(f'capitalsQuiz{quizNum + 1}.txt', 'w')    
    answerKeyFile = open(f'capitalsQuiz_answer{quizNum + 1}.txt', 'w')

# Write down the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '* 20) + f'State Capital Quiz (Form{quizNum + 1}')
    quizFile.write('\n\n')

# Shuffle the order of the states
    states = list(capitals.keys())    
    random.shuffle(states)

# Loop through all the 36 states, making a question for each
    for questionNum in range(36):

# Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOption =  wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)

# Write the question and answer options to the quiz files
        quizFile.write(f'{questionNum + 1} What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}.{answerOption[i]}\n")
        quizFile.write('\n')    

# Write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOption.index(correctAnswer)]}")
    quizFile.close()   
    answerKeyFile.close()