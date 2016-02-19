# authors: Cristi Serfass | Jeremy Dennen
# email: ckserfas@syr.edu | jcdennen@syr.edu

import random
from sys import exit
# initializing variables associated with gameplay and score-keeping
bot1_score = 0
bot2_score = 0
bot1_choice = ""
bot2_choice = ""
ties = 0
roundNum = 1

# winning set + set of choices
winning = {("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")}
possible_choices = ["Scissors", "Paper", "Rock"]
random_choice = random.choice(possible_choices)
random_pick = random.randint(1,2)

# first of the Rock-Paper-Scissors programs, this one uses conditional probability to determine what call to make based on the 
# "other player's" previous moves have been
def rps1(str):

    if roundNum == 1:
        return str
    # variables for keeping track of the number of times the "user" picks each of the possible throws
    uR = 0.0
    uP = 0.0
    uS = 0.0

    player_input = str
    
    # updating the counts for each throw
    if player_input == "Rock":
        uR += 1
    elif player_input == "Paper":
        uP += 1
    else:
        uS += 1
    
    # calculating the probability of each throw
    pR = float(uR/roundNum)
    pP = float(uP/roundNum)
    pS = float(uS/roundNum)
    
    # the largest probability is the one determined to be the "user's" most likely pick
    max_prob = max(pR, pP, pS)
    
    # thus, the program chooses what it calculates to be the move that counters what the 
    # user is likely to pick based on previous rounds
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
    # currently random selection generated for each round
    # does not attempt to 'learn' from its opponent
    my_choice = random.choice(possible_choices)
    return my_choice

# through 11 rounds of gameplay the bots "play" against eachother
# one relies on pure chance and the other one attempts to establish a pattern
# in order to "learn from" its opponent
while (roundNum < 12):
    # either bot can get the first "pick", depending on the value of random_pick
    if random_pick == 1:
        # the rest of the rounds are played such that in each round each bot /technically/
        # switches whether it "picks" first or second to add an extra layer of variability
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

    # simple score keeping w/ printouts after each round
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
# after 11 rounds the game exits after giving a final score report
print ("Good Game!\nTotal Rounds: %d \nFinal Score: Bot1 %d | Bot2 %d | Ties %d" % (roundNum-1, bot1_score, bot2_score, ties))
exit(0)
