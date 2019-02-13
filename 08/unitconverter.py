if __name__ == "__main__":
    
    print "---- UNIT Converter [km to miles] ----"
    
    again = True
    
    while again:
    
        number = raw_input("Which amount of kilometers to you want to convert into miles?" )
        
        converted = float(number) * 0.621371
        
        print str(number) + " kilometers equals " + str(converted)+ " miles."
        
        answer = raw_input("Would you like to convert another value? y/n" )
        
        answer = answer.lower()
        
        if answer == "n":
            again = False
            print "Thanks for using the unit converter."
