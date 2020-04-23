class Footballer:
    def __init__(self):
        self.Appearances = 198 #stats["Appearances"]
        self.Mins = 1659 #stats["Mins"]
        self.Yellow_cards = 54 # stats["Yellow_cards"]
        self.Red_cards = 12 # stats["Red_cards"]

class Striker(Footballer):
    def __init__(self):
        super().__init__()
        self.Goals = 218 # stats["Goals"]
        self.Shots_on_Target = 324 # stats["Shots_on_Target"]
        self.Assists = 67 #stats["Assists"]
        self.Dribbles = 352 # stats["Dribbles"]


class Mid_Fielder(Striker):
    def __init__(self):
        super().__init__()
        self.Assists = 178 # stats["Assists"]
        self.Crosses = 152 # stats["Crosses"]
        self.Goals = 76 # stats["Goals"]
        self.Retrives = 243 # stats["Retrives"]


class Deffender(Mid_Fielder):
    def __init__(self):
        super().__init__()
        self.Tackles = 256 # stats["Tackles"]
        self.Interceptions = 333 # stats["Interceptions"]
        self.Fouls = 189 # stats["Fouls"]
        self.Blocks = 165 # stats["Blocks"]

class Goal_Keeper(Deffender):
    def __init__(self):
        super().__init__()
        self.Saves = 167 # stats["Saves"]
        self.Goals_Awarded = 145 # stats["Goals_Awarded"]
        self.clean_sheets = 43 # stats["clean_sheets"]
        self.penalty_kicks_saved = 32 # stats["penalty_kicks_saved"]

#if __name__ == "__main__":
 #   import json
  #  stats = json.loads(input())


Player = Footballer()

#print(Player.Appearances)

Cristiano = Striker()

#print(Cristiano.Mins)

Marcelo = Mid_Fielder()

print(Marcelo.Shots_on_Target)
print(Marcelo.Yellow_cards)

Varane = Deffender()

print(Varane.Assists)
print(Varane.Shots_on_Target)
print(Varane.Red_cards)

Kylor_Navas = Goal_Keeper()

print(Kylor_Navas.Saves)
print(Kylor_Navas.Fouls)
print(Kylor_Navas.Goals)
print(Kylor_Navas.Shots_on_Target)



#{"Goals":228,"Shots_on_Target":334,"Assists":77,"Dribbles":362}
#{"Assists":188,"Crosses":162,"Goals":77,"Retrives":244}
#{"Tackles":257,"Interceptions":334,"Fouls":188,"Blocks":166}
#{"Saves":168,"Goals_Awarded":146,"clean_sheets":44,"penalty_kicks_saved":33}


