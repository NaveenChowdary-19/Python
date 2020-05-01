import random

Real_Madrid_Squad_List = []

Barcelona_Squad_List = []

Match_Squad = []


class Football:

    def __init__(self, Squad, Minutes, Squad_List):

        self.Goal = random.choice(Squad_List)  # Squad["7"]

        self.Yellow_Card = random.choice(Squad_List)  # Squad["4"]

        self.Red_Card = random.choice(Squad_List)  # Squad["2"]

        self.Assist = random.choice(Squad_List)  # Squad["5"]

        self.Minutes = Minutes

        self.Passes = self.Minutes * 2

        self.Team_Passes = self.Minutes * 9

        self.Fouls = self.Minutes // 8


        try:
            self.Minutes <= 0 and self.Minutes >= 90

        except ValueError:
            print(
                "Given Minutes Are Out Of Game Time.. So Please Give The  Time Which Is In Between  Game Time Ra Gutle ga")




    def Real_Madrid_Stats(self):

        for stat_minute in range(self.Minutes):
            if stat_minute == 12:
                print(" ", end="\n\n")
                print("{:>45}12'".format(" "))
                print("{:>45} ".format(" ") + Real_Madrid.Goal, end="\n" + "{:>45}".format(" ") + Real_Madrid.Assist)

            if stat_minute == 28:
                print(" ", end="\n\n")
                print("{:>45}28'".format(" "))
                print("{:>45}".format(" ") + Real_Madrid.Yellow_Card)

            if stat_minute == 47:
                print(" ", end="\n\n")
                print("{:>45}47'".format(" "))
                print("{:>45}".format(" ") + Real_Madrid.Red_Card)

            if stat_minute == 65:
                print(" ", end="\n\n")
                print("{:>45}65'".format(" "))
                print("{:>45} ".format(" ") + Real_Madrid.Goal, end="\n" + "{:>45}".format(" ") + Real_Madrid.Assist)

            if stat_minute == 76:
                print(" ", end="\n\n")
                print("{:>45}76'".format(" "))
                print("{:>45}".format(" ") + "Own Goal", end="\n" + "{:>45}".format(" ") + Barcelona.Yellow_Card)



    def Barcelona_Stats(self):

        for stat_minute in range(self.Minutes):
            if stat_minute == 19:
                print(" ", end="\n\n")
                print("{:>72}19'".format(" "))
                print("{:>72}".format(" ") + Barcelona.Goal, end="\n" + "{:72}".format(" ") + Barcelona.Assist)

            if stat_minute == 38:
                print(" ", end="\n\n")
                print("{:>72}38'".format(" "))
                print("{:>72}".format(" ") + Barcelona.Yellow_Card, end="\n")

            if stat_minute == 62:
                print(" ", end="\n\n")
                print("{:>72}62'".format(" "))
                print("{:>72}".format(" ") + Barcelona.Red_Card, end="\n")

            if stat_minute == 86:
                print(" ", end="\n\n")
                print("{:>72}86'".format(" "))
                print("{:>72}".format(" ") + Barcelona.Goal, end="\n" + "{:>72}".format(" ") + Barcelona.Assist)

            if stat_minute == 89:
                print(" ", end="\n\n")
                print("{:>72}89'".format(" "))
                print("{:>72}".format(" ") + "Own Goal", end="\n" + "{:>72}".format(" ") + Real_Madrid.Yellow_Card)

    def stats_of_The_Match(self):

        # In Team Stats  1. Goals   2. Corner Kicks     3. Free kicks     4. Passes    5. Shots On target    6. Total shots    7. Fouls   8. Red Cards   9. Yellow cards

        print(" ", end="\n\n\n")

        print("{:>60} Stats Of The Match".format(" "))
        print("{:>60}".format(" ") + "=====================", end="\n\n")

        print("{:>42} :== Real Madrid :== ".format(" ") + "  ||  " + " :== Barcelona :==")

        self.Fouls = random.randint(6, 14)

        self.Yellow_Card = random.randint(2, 4)  # corner_kicks

        # self.free_kicks = random.randint(5,8)         # free_kicks

        # self.Goals = random.randint(1,2)

        # self.shots_on_target = random.randint(4,6)    #shots_on_target

        print("{:>50}".format(" ") + str(Real_Madrid.Yellow_Card) + "  Yellow Cards  " + "  " + str(
            Barcelona.Yellow_Card))

        # print(Barcelona.shots_on_target)




    def Result_Of_Match(self):

        print("{:>60} Result Of The Match".format(" "))
        print("{:>60}".format(" ") + "======================", end="\n\n")

        print("{:>42} :== Real Madrid :== ".format(" ") + "  ||  " + " :== Barcelona :==")

        Real_Madrid.Real_Madrid_Stats()

        Barcelona.Barcelona_Stats()

        Real_Madrid.stats_of_The_Match()

        # Txt =  "{:>24} Passes Completed By Real_Madrid Team Are::  {:>12}  "
        # print("{:<24}".format("Passes Completed By Real_Madrid Team Are  ::  " + str(Real_Madrid.Team_Passes)))
        # print(Txt.format(" ",str(Real_Madrid.Team_Passes)))
        # print("No Of Fouls Committed Are  :  " + str(Real_Madrid.Fouls))


class Striker:
    def __init__(self):
        self.Goals = random.randint(1, 2)

        self.shots_on_target = random.randint(4, 6)  # shots_on_target

        self.dribbles = random.randint(6, 8)  # dribbles

        self.total_shots = random.randint(6, 9)  # total_shots

        self.penalty_kicks = random.randint(0, 2)  # penalty_kicks


class Mid_Fielder(Striker):
    def __init__(self):
        super().__init__()

        self.Assists = random.randint(0, 2)  # Assists

        self.Corner_kicks = random.randint(2, 5)  # corner_kicks

        self.free_kicks = random.randint(2, 4)  # free_kicks

        self.crosses = random.randint(1, 4)  # crosses

        self.retrives = random.randint(5, 10)  # retrives


class Deffender(Mid_Fielder):
    def __init__(self):
        super().__init__()

        self.Tackles = random.randint(4, 6)  # stats["Tackles"]

        self.Interceptions = random.randint(7, 10)  # stats["Interceptions"]

        self.Fouls = random.randint(3, 5)  # stats["Fouls"]

        self.Blocks = random.randint(3, 6)  # stats["Blocks"]


class Goal_Keeper(Deffender):
    def __init__(self):
        super().__init__()

        self.Saves = random.randint(1, 4)  # stats["Saves"]

        self.Goals_Awarded = random.randint(0, 3)  # stats["Goals_Awarded"]

        self.clean_sheets = random.randint(0, 1)  # stats["clean_sheets"]

        self.penalty_kicks_saved = random.randint(0, 1)  # stats["penalty_kicks_saved"]





class Player_stats(Goal_Keeper):
    def __init__(self):

        super().__init__()

    def Print_Player_Stats(self):

        if Fav_Player_is not in Match_Squad:
            print(
                "Arey Thuppals Yadava Your Favourite Player -{}- Not In Squad Ra Gutle. He Got Injured Give Another Player Ra Houle ".format(
                    Fav_Player_is))

        else:

            print(" ", end="\n\n\n")

            print("Your Favourite Player -{}- Stats Are ::".format(Fav_Player_is))
            print("====================================================", end="\n\n")

            print("{:>19} Goals  :--  ".format(" ") + str(self.Goals), end="\n\n")

            print("{:>19} shots_on_target :--  ".format(" ") + str(self.shots_on_target),
                  end="\n\n")  # = random.randint(4, 6)  # shots_on_target

            print("{:>19} Dribbles  :--  ".format(" ") + str(self.dribbles),
                  end="\n\n")  # = random.randint(6, 8)  # dribbles

            print("{:>19} Total Shots  :--  ".format(" ") + str(self.total_shots),
                  end="\n\n")  # = random.randint(6, 9)  # total_shots

            print("{:>19} Penalty Kicks  :--  ".format(" ") + str(self.penalty_kicks),
                  end="\n\n")  # = random.randint(0, 2)  # penalty_kicks

            print("{:>19} Assists  :--  ".format(" ") + str(self.Assists), end="\n\n")

            print("{:>19} Corner_kicks  :--  ".format(" ") + str(self.Corner_kicks), end="\n\n")

            print("{:>19} Free Kicks  :--  ".format(" ") + str(self.free_kicks), end="\n\n")

            print("{:>19} Crosses  :--  ".format(" ") + str(self.crosses), end="\n\n")

            print("{:>19} Retrives  :--  ".format(" ") + str(self.retrives), end="\n\n")

            print("{:>19} Fouls  :--  ".format(" ") + str(self.Fouls), end="\n\n")

            print("{:>19} Blocks  :--  ".format(" ") + str(self.Blocks), end="\n\n")

            print("{:>19} Interceptions  :--  ".format(" ") + str(self.Interceptions), end="\n\n")

            print("{:>19} Tackles  :--  ".format(" ") + str(self.Tackles), end="\n\n")

            print("{:>19} Saves  :--  ".format(" ") + str(self.Saves), end="\n\n")

            print("{:>19} Clean_sheets  :--  ".format(" ") + str(self.clean_sheets), end="\n\n")

            print("{:>19} Goals_Awarded  :--  ".format(" ") + str(self.Goals_Awarded), end="\n\n")

            print("{:>19} Penalty_kicks_saved  :--  ".format(" ") + str(self.penalty_kicks_saved), end="\n\n")


if __name__ == "__main__":
    import json

    Real_Madrid_Squad = json.loads(input())

    Barcelona_Squad = json.loads(input())

    # {"7":"Cristiano Ronaldo" , "1":"Keylor Navas" , "2":"Sergio Ramos" , "3":"Marcelo" , "4":"Varane" , "5":"Toni Kroos" , "6":"Aaron Ramsey" , "8":"Casemiro" , "9":"Karim Benzma" , "10":"Jamie Vardy" , "11":"Gerath Bale"}
    # {"10":"Lionel Messi" , "1":"Cluadio Bravo" , "3":"Gerard Pique" , "4":"Virgil Vandijk" , "5":"Sergio Roberto" , "2":"David Luiz" , "6":"Robert Levendowski" , "7":"James Rodrguize" , "8":"Paulo Dybala" , "9":"Masuet Ozil" , "11":"Mohammad Salah"}

    Minutes = int(input())

    Fav_Player_is = str(input())

    print(Minutes)
    # print(Fav_Player)

for Keys in Real_Madrid_Squad:
    Real_Madrid_Squad_List.append(Real_Madrid_Squad[Keys])

for Keys in Barcelona_Squad:
    Barcelona_Squad_List.append(Barcelona_Squad[Keys])

Match_Squad = Real_Madrid_Squad_List + Barcelona_Squad_List

# print(Match_Squad)
# print(Fav_Player)

# print(" ",end = "\n\n\n")


playing_XI = len(Real_Madrid_Squad_List)

print(" ", end="\n\n\n")

print("Real Madrid Playing XI are :" + "{:>70}".format(" ") + "Barcelona Playing XI are :")

print("===========================" + "{:>70}".format(" ") + "===========================", end="\n\n")

for player in range(playing_XI):

    Barca = "{}. {:<30}".format(str(player + 1), str(Barcelona_Squad_List[player]))

    Real = "{}. {:<30} {:<63}".format(str(player + 1), str(Real_Madrid_Squad_List[player]), " ")

    print(Real, Barca)

print(" ", end="\n\n\n")

Real_Madrid = Football(Real_Madrid_Squad, Minutes, Real_Madrid_Squad_List)

Barcelona = Football(Barcelona_Squad, Minutes, Barcelona_Squad_List)

print(Real_Madrid.Result_Of_Match())

# print(Real_Madrid.Team_Passes)
# print(Real_Madrid.Goal)
# print(Real_Madrid.Fouls)
# Isco = Striker()
# print(Isco.Goals)


Fav_Player = Player_stats()

print(Fav_Player.Print_Player_Stats())

# print(Fav_Player.dribbles)
# print(Real_Madrid_Squad_List)
# print(Barcelona_Squad_List)


print(Match_Squad)

'''
{"7":"Cristiano Ronaldo" , "1":"Keylor Navas" , "2":"Sergio Ramos" , "3":"Marcelo" , "4":"Varane" , "5":"Toni Kroos" , "6":"Aaron Ramsey" , "8":"Casemiro" , "9":"Karim Benzma" , "10":"Jamie Vardy" , "11":"Gerath Bale"}
{"10":"Lionel Messi" , "1":"Cluadio Bravo" , "3":"Gerard Pique" , "4":"Virgil Vandijk" , "5":"Sergio Roberto" , "2":"David Luiz" , "6":"Robert Levendowski" , "7":"James Rodrguize" , "8":"Paulo Dybala" , "9":"Masuet Ozil" , "11":"Mohammad Salah"}
90
Chowdary


'''
