class result(object):
    def __init__(self, score, player_name, date, difficulty):
        self.score = score
        self.player_name = player_name
        self.date = date
        self.difficulty = difficulty
        
    def save(self):
        
        import json   
  
        with open("results.json", "r") as f:
            results_dict = json.load(f)
            f.close()
        
        result_now = self.__dict__
        results_dict.append(result_now)
        
        with open("results.json", "w") as f:
            json.dump(results_dict,f)

def create_number(difficulty):
    
    import random
    
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

def play(difficulty="easy", player_name = "Unknown"):
    
    import datetime
    now = datetime.datetime.now()
    
    secret, max_attempt, upper = create_number(difficulty)
    
    print("You've got " + str(max_attempt) + " attempts to guess.")
    print("Guess my secret number between 0 an "+ str(upper)+"!")

    attempt = 0

    while attempt != max_attempt:
        
        attempt +=1
        
        guess = input("What's your guess? ")
    
        if int(guess)==secret:
            print("Great, you're right. That's my number.")
            print("It took you "+ str(attempt) + " attempts.")
            
            victory = result(score= attempt, player_name= player_name, date= str(now), difficulty=difficulty)
            victory.save()
            
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

def main():
    
    print("Welcome to: GUESSING GAME!")
    
    player_name = input("What's your name? ")
    difficulty = input("Which difficulty would you like to play: easy, medium, hard? ")
    
    play(difficulty, player_name)
      
    print("Thanks for playing!")

main()
