class Football:
    def __init__(self,Squad,Minutes):
        self.Goal = Squad["7"]
        self.Yellow_Card = Squad["4"]
        self.Red_Card = Squad["2"]
        self.Assist = Squad["5"]
        self.Minutes = Minutes

        self.Passes = self.Minutes * 9

        if Minutes <= 0 and Minutes >= 90:
            raise ValueError("Given Minutes Are Out Game Time.. So Please Give The  Time With In Game Time Ra Gutle ga")

    def Result_Of_Match(self):

        print("Passes Completed By Real_Madrid Team Are  ::  " + str(Real_Madrid.Passes))



if __name__ == "__main__":
    import json
    Squad = input()
# {"7":"Cristiano Ronaldo" , "1":"Keylor Navas" , "2":"Sergio Ramos" , "3":"Marcelo" , "4":"Varane" , "5":"Toni Kroos" , "6":"Aaron Ramsey" , "8":"Casemiro" , "9":"Karim Benzma" , "10":"Jamie Vardy" , "11":"Gerath Bale"}
# {"7":Cristiano Ronaldo , "1":Keylor Navas , "2":Sergio Ramos , "3":Marcelo , "4":Varane , "5":Toni Kroos , "6":Aaron Ramsey , "8":Casemiro , "9":Karim Benzma , "10":Jamie Vardy , "11":Gerath Bale}
    Minutes = input()

Real_Madrid = Football(Squad,Minutes)

print(Real_Madrid.Passes)

print(Real_Madrid.Result_Of_Match())

print(Real_Madrid.Goal)



#  12'  Cristiano Ronaldo  Assist By Garath Bale

#  28'  Yellow Card For Sergio Ramos

#  45'  Red Card For Casemiro

#  67'  Toni Kroos Assist By Cristiano Ronaldo

#  76'  Aaron Ramsey Assist By Marcelo

#  88'  Cristiano Ronaldo Assist By Benzma

#  90'  Cristiano Ronaldo By Jamie Vardy

