def change_string(string, operation):

    if operation == "uppercase":
        print(string.upper())
    elif operation == "lowercase":
        print(string.lower())
    elif operation == "join":
        string = string.split(" ")
        
        print("".join(string))
    
    else:
        print("Operation not possible.")


if __name__ == "__main__":

    string = input("What words or sentences would you like to change?  ")
    operation = input("What would you like to do? uppercase, lowercase, join ")
    
    change_string(string,operation)
    
    again = True
    
    while again:
        
        answer = input("Would you like to change another text! y/n")
        
        answer = answer.lower()
    
        if answer == "n":
            again = False
            print("Bye!")
        
        else:
           
            string = input("What words or sentences would you like to change?  ")
            operation = input("What would you like to do? uppercase, lowercase, join ")
    
            change_string(string, operation)
