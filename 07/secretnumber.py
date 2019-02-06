if __name__ == "__main__":
    
    import random
    
    secret = random.randint(0,10)
    
    guess = raw_input("Guess my secret number between 0 an 10! " )
    
    if int(guess)==secret:
        print "Great, you're right. That's my number."
    else:
        print "Sorry, that's wrong. My number was "+ str(secret) +"."
