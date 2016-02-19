# authors: Cristi Serfass | Jeremy Dennen
# email: ckserfas@syr.edu | jcdennen@syr.edu

import random
from sys import exit

bot1_score = 0
bot2_score = 0
bot1_choice = ""
bot2_choice = ""
ties = 0
roundNum = 1

winning = {("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")}
possible_choices = ["Scissors", "Paper", "Rock"]
random_choice = random.choice(possible_choices)
random_pick = random.randint(1,2)

def rps1(str):

    if roundNum == 1:
        return str

    uR = 0.0
    uP = 0.0
    uS = 0.0

    player_input = str

    if player_input == "Rock":
        uR += 1
    elif player_input == "Paper":
        uP += 1
    else:
        uS += 1

    pR = float(uR/roundNum)
    pP = float(uP/roundNum)
    pS = float(uS/roundNum)

    max_prob = max(pR, pP, pS)

    if max_prob == pR:
        smart_choice = "Paper"
    elif max_prob == pP:
        smart_choice = "Scissors"
    elif max_prob == pS:
        smart_choice = "Rock"
    else:
        smart_choice = random_choice

    return smart_choice

def rps2(str):
    # currntly random selection generated for each round
    # does not attempt to 'learn' from its opponent
    my_choice = random.choice(possible_choices)
    return my_choice

while (roundNum < 12):
    if random_pick == 1:
        if ((roundNum%2)!=0):
          bot1_choice = rps1(random_choice)
          bot2_choice = rps2(bot1_choice)
        else:
          bot2_choice = rps2(random_choice)
          bot1_choice = rps1(bot2_choice)
    else:
        if ((roundNum%2)!=0):
            bot2_choice = rps2(random_choice)
            bot1_choice = rps1(bot2_choice)
        else:
            bot1_choice = rps1(random_choice)
            bot2_choice = rps2(bot1_choice)


    if bot1_choice == bot2_choice:
        ties += 1
        print("They both choose %s, it's a tie!" % bot1_choice)
        print("Bot1: %d, Bot2: %d" % (bot1_score, bot2_score))

    elif (bot2_choice, bot1_choice) in winning:
        bot2_score += 1
        print("Bot1 picked %s and Bot2 picked %s, Bot2 wins!" % (bot1_choice, bot2_choice))
        print("Bot1: %d, Bot2: %d" % (bot1_score, bot2_score))
        #print("%s probability: %f" %(smart_choice, max_prob))

    else:
        bot1_score += 1
        print("Bot1 picked %s and Bot2 picked %s, Bot1 wins!" % (bot1_choice, bot2_choice))
        print("Bot1: %d, Bot2: %d" % (bot1_score, bot2_score))
        #print("%s probability: %f" %(smart_choice, max_prob))

    roundNum += 1

print ("Good Game!\nTotal Rounds: %d \nFinal Score: Bot1 %d | Bot2 %d | Ties %d" % (roundNum-1, bot1_score, bot2_score, ties))
exit(0)
