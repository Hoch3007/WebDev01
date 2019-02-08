if __name__ == "__main__":
    
    moods = {"sad": "Don't be! Life is beautiful.", "happy": "It is great to see you happy!",
             "nervous": "Take a deep breath 3 times.",
             "excited": "Great. I hope it's positive excitement.", "relaxed": "Cool."}

    mood = input("How's your mood today? Choose from: " + str(moods.keys()) + " Your choice: ")

    if mood in moods:
        print(moods[mood])
    else:
        print("I don't recognize this mood.")

