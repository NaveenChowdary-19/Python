"""
Mumbai Indians , Chennai Kings
{"1":"Rohith Sharma (Cap)" , "2":"Quinton DeKock (Wk)" , "3":"Chris Lynn" , "4":"Yuvaraj Singh" , "5":"Kerion Pollard" , "6":"Hardik Pandya" , "7":"Krunal Pandya" , "8":"Lasith Malinga" , "9":"Nathan Coulter-Nile" , "10":"Dhawal Kulakarni" , "11":"Jasprith Bumrah"}
{"1":"Shane Watson" , "2":"Ambati Rayudu" , "3":"Sursh Raina" , "4":"Faf Duplesis" , "5":"M S Dhoni (Cap)&(Wk)" , "6":"Dwayne Bravo" , "7":"Ravindra Jadeja" , "8":"Harbajan Singh" , "9":"Deepak Chahar" , "10":"Shardaul Thakur" , "11":"Josh Hazlewood"}

"""
import random

Mumbai_Indians_Squad = []

Team_II_Squad = []

if __name__ =="__main__":
    import json
    Teams = input().split(",")



    Mumbai_Team = json.loads(input())

    Team_II = json.loads(input())


Coin_Spin = ['Bat' , 'Bowl']
Toss = random.choice(Coin_Spin)

print(" ",end = "\n\n\n")

Toss_won = random.choice(Teams)
print("Hello... We Bleed Blue.. Welcome To The Wankade .. Its Time For The Toss.. Ganguly Will Spin Coin.. Rohith Calls Annnddddd... ",end = "\n\n")
print("{}Won The Toss And Choice To {} First".format(Toss_won,Toss))


for keys in Mumbai_Team:
    Mumbai_Indians_Squad.append(Mumbai_Team[keys])

for keys in Team_II:
    Team_II_Squad.append(Team_II[keys])


playing_XI = len(Mumbai_Indians_Squad)

print(" ",end = "\n\n\n")

print("{:>10}Mumbai Indians Playing XI are :".format(" ") + "{:>70}".format(" ") + "Chennai Kings Playing XI are :")

print("{:>10}=============================".format(" ") + "{:>72}".format(" ") + "============================",end="\n\n")

for player in range(playing_XI):
    print("{:>11}{}. {:<30} {:<66}".format(" ", str(player + 1), str(Mumbai_Indians_Squad[player]), " "),
          "{}. {:<30}".format(str(player + 1), str(Team_II_Squad[player])) , end = "\n\n")


print(" ",end = "\n\n\n")




"""

So far ... Output Comes As below
---------------------------------

Hello... We Bleed Blue.. Welcome To The Wankade .. Its Time For The Toss.. Ganguly Will Spin Coin.. Rohith Calls Annnddddd... 

Mumbai Indians Won The Toss And Choice To Bat First
 


          Mumbai Indians Playing XI are :                                                                      Chennai Kings Playing XI are :
          =============================                                                                        ============================

           1. Rohith Sharma (Cap)                                                                               1. Shane Watson                  

           2. Quinton DeKock (Wk)                                                                               2. Ambati Rayudu                 

           3. Chris Lynn                                                                                        3. Sursh Raina                   

           4. Yuvaraj Singh                                                                                     4. Faf Duplesis                  

           5. Kerion Pollard                                                                                    5. M S Dhoni (Cap)&(Wk)          

           6. Hardik Pandya                                                                                     6. Dwayne Bravo                  

           7. Krunal Pandya                                                                                     7. Ravindra Jadeja               

           8. Lasith Malinga                                                                                    8. Harbajan Singh                

           9. Nathan Coulter-Nile                                                                               9. Deepak Chahar                 

           10. Dhawal Kulakarni                                                                                  10. Shardaul Thakur               

           11. Jasprith Bumrah                                                                                   11. Josh Hazlewood                

 



Process finished with exit code 0


"""




