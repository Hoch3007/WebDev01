def create_number(difficulty):
    
    import random

    secret=0
    max_attempt = 0
    
    if difficulty=="easy":
        secret = random.randint(0,10)
        max_attempt = 100
        upper=10
        
    elif difficulty=="medium":
        secret = random.randint(0,50)
        max_attempt = 10
        upper=50

    elif difficulty=="hard":
        secret = random.randint(0,100)
        max_attempt = 5
        upper=100
        
    else:
        print('Unknown difficulty! Difficulty is set to "easy".')

    return secret, max_attempt, upper


def load_scores(difficulty):
    
    import json   
  
    with open("scores_"+str(difficulty)+".json", "r") as f:
        scores = json.load(f)
        f.close()
        
    return scores


def save_score(difficulty, scores):

    import json
    
    with open("scores_"+str(difficulty)+".json", "w") as f:
        json.dump(scores,f)


def play(difficulty="easy"):
    
    import datetime
    now = datetime.datetime.now()
    
    secret, max_attempt, upper = create_number(difficulty)
    
    print("You've got " + str(max_attempt) + " attempts to guess.")
    print("Guess my secret number between 0 an "+ str(upper)+"!")
    
    scores = load_scores(difficulty)
    
    attempt = 0

    while attempt != max_attempt:
        
        attempt +=1
        
        guess = input("What's your guess? ")
    
        if int(guess)==secret:
            print("Great, you're right. That's my number.")
            print("It took you "+ str(attempt) + " attempts.")
            
            scores[str(now)]=attempt
            
            save_score(difficulty, scores)
            
            break
            
        else:
            print("Sorry, that's wrong.")
            
            if int(guess)<secret: 
                print("Guess higher!")
            elif int(guess)>secret:
                print("Guess lower!")
            else:
                print("I've got a problem! Please start the game again!")
                break

def highscore(difficulty):
    
    #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    
    scores = load_scores(difficulty)
    
    import operator
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
    
    if len(sorted_scores)>=3:
    
        print("--------------- Top 3 -----------------")
        print("First place: ", sorted_scores[0])
        print("Second place: ", sorted_scores[1])
        print("Third place: ", sorted_scores[2])
        
    else:
        
        print("There are no TOP 3, please play again!")
        
       
def main():


    
    print("Welcome to: GUESSING GAME!")
    
    difficulty = input("Which difficulty would you like to play: easy, medium, hard? ")
    
    play(difficulty)
    
    best_score = input("Would you like to see the highscores? y/n ")
    
    if best_score == "y":
        
        highscore(difficulty)
    
    else:
        
        print("Thanks for playing!")


main()