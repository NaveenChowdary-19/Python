class Cricketer:
    #Matches_played = 218
    #catches = 143
    Runs = 876
    High_Score = 56
    Batting_Avg = 19.7
    Centuries = 0
    def __init__(self):
        #Matches_played = 218
        #catches = 143
        #self.Matches_played = details["Matches_played"]
        #self.catches = details["catches"]
        self.Matches_played = 218
        self.catches = 143

class Batsman(Cricketer):
    def __init__(self,details):
        super().__init__()
        self.Runs = details["Runs"]
        self.High_Score = details["High_Score"]
        self.Batting_Avg = details["Batting_Avg"]
        self.Centuries = details["Centuries"]

        self.Runs = 876
        self.High_Score = 56
        self.Batting_Avg = 19.7
        self.Centuries = 0


class Bowler(Batsman):
    def __init__(self,details):
        super().__init__(Runs,High_Score,Batting_Avg,Centuries)
        #super(Batsman).__init__()
        self.Wickets = details["Wickets"]
        self.Bowling_Avg = details["Bowling_Avg"]
        self.Highest_wickets = details["Highest_wickets"]


#class All-Rounder(Batsman,Bowler):
 #   def __init__(self):
  #      pass


class Wicket_Keeper(Cricketer):
    def __init__(self):
        self.Stumpings = deatails["Stumpings"]
        self.Run_outs = details["Run_outs"]

if __name__ == "__main__":
    import json
    details = json.loads(input())

Naveen = Cricketer()

#{"Matches_played":218,"catches":146}
#{"Runs":9988,"High_Score":264,"Batting_Avg":48.8,"Centuries":29}
#{"Wickets":324,"Bowling_Avg":19.4,"Highest_wickets": "6/23"}
#{"Stumpings":196,"Run_outs":183}

#print(Naveen.Matches_played)

#Sachin = Batsman(details)

#print(Sachin.Matches_played)

Zaheer_Khan = Bowler(details)

print(Zaheer_Khan.Highest_wickets)


print(Zaheer_Khan.Runs)

#print(Naveen.Matches_played)

#print(Cricketer.Matches_played)



