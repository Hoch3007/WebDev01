if __name__ == "__main__":
    
    print("----- FIZZ BUZZ -----")
    
    again = True
    
    while again:
    
        number = input("Select a number between 1 and 100! " )
        
        for i in range(1, int(number)+1):
        
            if i % 15 == 0:
                print("fizzbuzz")

            elif i % 5 == 0:
                print("buzz")

            elif i % 3 == 0:
                print("fizz")
            else:
                print(i)
                
        answer = input("Would you like to play again! y/n" )
        
        answer = answer.lower()
    
        if answer == "n":
            again = False
            print("Thanks for playing FizzBuzz.")