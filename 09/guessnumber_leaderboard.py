if __name__ == "__main__":
    
    import json
    
    import datetime
    now = datetime.datetime.now()
    
    with open("score.json", "r") as f:
        scores = json.load(f)
        f.close()
    
    import random
    
    secret = random.randint(0, 100)
    
    max_attempt = 10
    attempt = 0
    
    print("You've got 10 attempts to guess.")
    print("Guess my secret number between 0 an 100!")
    
    while attempt != max_attempt:
        
        attempt += 1
        
        guess = input("What's your guess? ")
    
        if int(guess) == secret:
            print("Great, you're right. That's my number.")
            print("It took you " + str(attempt) + " attempts.")
            
            scores[str(now)] = attempt
            
            with open("score.json", "w") as f:
                json.dump(scores,f)
            
            break
        else:
            print("Sorry, that's wrong.")
            
            if int(guess)<secret: 
                print("Guess higher!")
            elif int(guess)>secret:
                print("Guess lower!")
            else:
                print("I've got a problem!")
    
    import operator
    
    with open("score.json", "r") as f:
        scores = json.load(f)
        f.close()
    
    print("TOP 3 Attempts")
    
    print(max(scores.items(), key=operator.itemgetter(1))[0])
    print(max(scores.items(), key=operator.itemgetter(1))[1])
    print(max(scores.items(), key=operator.itemgetter(1))[2])
