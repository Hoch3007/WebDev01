# object einfügen wegen python 2.7, in python 3.7 nicht notwendig
class Player(object):
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    
class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        # BasketballPlayer, self wegen python 2.7, in 3.7 kann Null-Argument gemacht werden
        super(BasketballPlayer, self).__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
    
    def save(self):
        
        import json   
  
        with open("players_basketball.json", "r") as f:
            players = json.load(f)
            f.close()
        
        player = self.__dict__
        players.append(player)
        
        with open("players_basketball.json", "w") as f:
            json.dump(players,f)


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super(FootballPlayer, self).__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        
    def save(self):
        
        import json   
  
        with open("players_football.json", "r") as f:
            players = json.load(f)
            f.close()
        
        player = self.__dict__
        players.append(player)
        
        with open("players_football.json", "w") as f:
            json.dump(players,f)

            
            
def add_player(sport):
    
    first_name = raw_input("What's the first name of the player? ")
    last_name = raw_input("What's the last name of the player? ")
    height_cm = raw_input("What's the player's height in cm? ")
    weight_kg = raw_input("What's the player's weight in kg? ")
    
    if sport == "basketball":
        points = raw_input("How many points? ")
        rebounds = raw_input("How many rebounds? ")
        assists = raw_input("How many assists? ")
        
        player = BasketballPlayer(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, points=points, rebounds=rebounds, assists=assists)
        
    else:
        
        goals = raw_input("How many goals? ")
        yellow_cards = raw_input("How many yellow cards? ")
        red_cards = raw_input("How many red cards? ")
        
        player = FootballPlayer(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, goals=goals, yellow_cards=yellow_cards, red_cards=red_cards)
        
    
    player.save()
    
 

def player_database():
    
    print "--- The Basketball & Football Player Database ---"
       
    sport = raw_input("In which sport is the player active? football/basketball ")
    sport = sport.lower()
    
    add_player(sport)
    
    c = "y"
    
    answers = ["y", "n"]
    answer = 0
    
    while c!="n":
        
        while answer not in answers:
            answer = raw_input("Would you like to add another player? y/n ")
        
        if answer == "y":
            sport = raw_input("In which sport is the player active? football/basketball ")
            sport = sport.lower()
    
            add_player(sport)
        
        c= answer
        
    print "Thanks for using the database!"
    
player_database()
