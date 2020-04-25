class Football:
    def __init__(self,Squad,Minutes):
        self.Goal = Squad["7"]
        self.Yellow_Card = Squad["4"]
        self.Red_Card = Squad["2"]
        self.Assist = Squad["5"]
        self.Minutes = Minutes

        self.Passes = self.Minutes * 9
        
        self.Fouls = self.Minutes // 8

        if self.Minutes <= 0 and self.Minutes >= 90:
            raise ValueError("Given Minutes Are Out Game Time.. So Please Give The  Time With In Game Time Ra Gutle ga")
        

class Striker:
    def __init__(self):
        
        self.Goals = Goals
        self.shots_on_target = shots_on_target
        self.dribbles = dribbles
        self.total_shots = total_shots
        self.penalty_kicks = penalty_kicks
        
        
class Mid_Fielder:
    def __init__(self):
        
        self.Assists = Assists
        self.Corner_kicks = corner_kicks
        self.free_kicks = free_kicks
        self.crosses = crosses
        self.retrives = retrives
        
        
class Deffender():
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


    
    def Stats(self):
        
        for stat_minute in range(self.Minutes):
            if stat_minute == 12:
                print("Goal By : " + Real_Madrid.Goal + " @  Assist By - " + Real_Madrid.Assist)
            
            if stat_minute == 28:
                print("Yellow Card for --  " + Real_Madrid.Yellow_Card)
            
            if stat_minute == 47:
                print("Red Card For ---  " + Real_Madrid.Red_Card)
            
            if stat_minute == 65:
                print("Goal By  : " + Real_Madrid.Goal + " @  Assist by - " + Real_Madrid.Assist)
                
        
    def Result_Of_Match(self):
        
        Real_Madrid.Stats()

        print("Passes Completed By Real_Madrid Team Are  ::  " + str(Real_Madrid.Passes))
        print()
        print("No Of Fouls Committed Are  :  " + str(Real_Madrid.Fouls))



if __name__ == "__main__":
    import json
    Squad = json.loads(input())
# {"7":"Cristiano Ronaldo" , "1":"Keylor Navas" , "2":"Sergio Ramos" , "3":"Marcelo" , "4":"Varane" , "5":"Toni Kroos" , "6":"Aaron Ramsey" , "8":"Casemiro" , "9":"Karim Benzma" , "10":"Jamie Vardy" , "11":"Gerath Bale"}
# {"7":Cristiano Ronaldo , "1":Keylor Navas , "2":Sergio Ramos , "3":Marcelo , "4":Varane , "5":Toni Kroos , "6":Aaron Ramsey , "8":Casemiro , "9":Karim Benzma , "10":Jamie Vardy , "11":Gerath Bale}
    Minutes = int(input())

Real_Madrid = Football(Squad,Minutes)

print(Real_Madrid.Passes)

print(Real_Madrid.Result_Of_Match())

print(Real_Madrid.Goal)

print(Real_Madrid.Fouls)



#  12'  Cristiano Ronaldo  Assist By Garath Bale

#  28'  Yellow Card For Sergio Ramos

#  45'  Red Card For Casemiro

#  67'  Toni Kroos Assist By Cristiano Ronaldo

#  76'  Aaron Ramsey Assist By Marcelo

#  88'  Cristiano Ronaldo Assist By Benzma

#  90'  Cristiano Ronaldo By Jamie Vardy

