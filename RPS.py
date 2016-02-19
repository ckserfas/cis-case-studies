# authors: Cristi Serfass | Jeremy Dennen
# email: ckserfas@syr.edu | jcdennen@syr.edu

import random
from sys import exit
roundNum = 1
max_prob = 0.0
user_score = 0
bot_score = 0
ties = 0
uR = 0.0
uP = 0.0
uS = 0.0
pR = 0.0
pP = 0.0
pS = 0.0


possible_choices = ["Scissors", "Paper", "Rock"]
random_choice = random.choice(possible_choices)
smart_choice = "tbd"

# winning set
winning = {("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")}

while (roundNum < 12):
    player_input = raw_input("What's your choice (Scissors, Paper, or Rock)")
    while player_input not in possible_choices:
        print("Not a valid choice.")
        player_input = raw_input("What's your choice (Scissors, Paper, or Rock)")


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

    if player_input == smart_choice:
        ties += 1
        roundNum += 1
        print("You both choose %s, you tie!" % smart_choice)
        print("Bot: %d, You: %d" % (bot_score, user_score))
       #print("%s probability: %f" %(smart_choice, max_prob))

    elif (player_input, smart_choice) in winning:
        user_score += 1
        roundNum += 1
        print("You picked %s and the bot picked %s, you win!" % (player_input, smart_choice))
        print("Bot: %d, You: %d" % (bot_score, user_score))
        #print("%s probability: %f" %(smart_choice, max_prob))

    else:
        bot_score += 1
        roundNum += 1
        print("You picked %s and the bot picked %s, you lose!" % (player_input, smart_choice))
        print("Bot: %d, You: %d" % (bot_score, user_score))
        #print("%s probability: %f" %(smart_choice, max_prob))

print ("Good Game!\nTotal Rounds: %d \nFinal Score: Bot %d | You %d | Ties %d" % (roundNum-1, bot_score, user_score, ties))
exit(0)
