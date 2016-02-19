# authors: Cristi Serfass | Jeremy Dennen
# email: ckserfas@syr.edu | jcdennen@syr.edu

import random
from sys import exit

# initializing score-keeping and probability computation variables
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

# establishing accepted values and generating a random first move for the bot
possible_choices = ["Scissors", "Paper", "Rock"]
random_choice = random.choice(possible_choices)
smart_choice = ""

# winning set
winning = {("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")}

# heart of the game, plays 11 rounds with regular score updates
while (roundNum < 12):
    # prompts the user for input, will only accept answer exactly as written
    player_input = raw_input("What's your choice (Scissors, Paper, or Rock): ")
    while player_input not in possible_choices:
        print("Not a valid choice.")
        player_input = raw_input("What's your choice (Scissors, Paper, or Rock)")

    # updating counts for what the user has picked throughout the game
    if player_input == "Rock":
        uR += 1
    elif player_input == "Paper":
        uP += 1
    else:
        uS += 1
    
    # updating conditional probability for each choice
    pR = float(uR/roundNum)
    pP = float(uP/roundNum)
    pS = float(uS/roundNum)
    
    # identifies the largest probability in order to identify what the user's likely next pick is
    max_prob = max(pR, pP, pS)

    # based on max_prob, the program chooses what would be the appropriate counter-move for what it
    # expects the player's input to be
    if max_prob == pR:
        smart_choice = "Paper"
    elif max_prob == pP:
        smart_choice = "Scissors"
    elif max_prob == pS:
        smart_choice = "Rock"
    else:
        smart_choice = random_choice

    # score-keeping & printouts
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

# after 11 rounds the game gives a final score report before exiting
print ("Good Game!\nTotal Rounds: %d \nFinal Score: Bot %d | You %d | Ties %d" % (roundNum-1, bot_score, user_score, ties))
exit(0)
