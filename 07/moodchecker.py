if __name__ == "__main__":
    
    mood = raw_input("How's your mood today? Choose from: sad, happy, nervous, excited, relaxed. Your choice: " )
    
    moods = ["sad"," happy", "nervous","excited", "relaxed"]
    
    if mood == moods[0]:
        print "Don't be! Life is beautiful."
    elif mood == moods[1]:
        print "It is great to see you happy!"
    elif mood == moods[2]:
        print "Take a deep breath 3 times."
    elif mood == moods[3]:
        print "Great. I hope it's positive excitement."
    elif mood == moods[4]:
        print "Cool."
    else:
        print "I don't recognize this mood."
