from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == 2 else False  # remove this


def lifeLine(i):
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    from random import choice
    print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}')
    print(f'\t\tOptions:')
    correct = QUESTIONS[i]["answer"]
    l = [1, 2, 3, 4]
    l.remove(correct)
    x = choice(l)
    if correct > x:
        print(f'\t\t\tOption {x}: {QUESTIONS[i]["option"+str(x)]}')
        print(f'\t\t\tOption {correct}: {QUESTIONS[i]["option"+str(correct)]}')
    else:
        print(f'\t\t\tOption {correct}: {QUESTIONS[i]["option"+str(correct)]}')
        print(f'\t\t\tOption {x}: {QUESTIONS[i]["option"+str(x)]}')


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    lifeline_valid = True
    game_play = True
    i = 0
    while game_play and i < 15:

        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

    # check for the input validations
        if ans.lower() == "quit":
            if i == 0:
                print("Total amount won 0")
                return
            print("Total amount won ", QUESTIONS[i-1]['money'])
            return
            game_play = False

        if ans.lower() == "lifeline" and lifeline_valid and i != 14:
            lifeline_valid = False
            lifeLine(i)
            ans = input('Your choice ( 1-4 ) : ')
            if ans.lower() == "quit":
                game_play = False

        if isAnswerCorrect(i, int(ans)):

            # print the total money won.
            print("Total amount won ", QUESTIONS[i]['money'])
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            i += 1

        else:
            # end the game now.
            print("OOps!! YOUR ANSWER IS INCORRECT , the correct answer is",
                  QUESTIONS[i]['answer'])
            # also print the correct answer
            print('\nIncorrect !')
        # print the total money won in the end.
            if i >= 5 and i < 10:
                print("Total amount won 10000")
            elif i >= 10 and i < 15:
                print("Total amount won 3,20,000")
            else:
                print("Total amount won 0")
            break


kbc()
