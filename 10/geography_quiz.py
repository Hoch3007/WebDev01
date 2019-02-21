if __name__ == "__main__":
    
    print "---- Guess the Capital ---"
    print "10 Questions to test your geography knowledige."

    import random

    used = []

    questions = 10
    question = 0
    number = 0
    correct_answers = 0

    while question!=questions:

        while number in used:

            number = random.randint(0,len(capitals))

        used.append(number)
        question += 1

        print "Question "+ str(question)+":"
        print "What's the capital of " + str(capitals[int(number)]['country'])+"?"

        answer = raw_input("Your answer: ")

        if answer == capitals[int(number)]['city']:

            print "You're right. You earn 1 Point!"

            correct_answers +=1

        else:

            print "I'm sorry, that's wrong. The capital is "+ str(capitals[int(number)]['city']) + "."

    print "Your final score is "+ str(correct_answers)+"."
