import random
import os
import sys


def assign(players, gifts):
    """
    Assigns each player to a Secret Santa.
    """
    secret_santas = {}
    already_assigned = []
    for player in players:
        assignee = random.choice([p for p in players if p != player and p not in already_assigned])
        secret_santas[player] = assignee
        already_assigned.append(assignee)

    # Write to file so that you don't forget who is assigned to who
    with open('secret_santas.txt', 'w') as f:
        f.writelines('{}: {}\n'.format(k,v) for k, v in secret_santas.items())
    return secret_santas

# Begin main function    

players = [player.split(":",1)[0].lower() for player in open("players.txt")]
gifts = [player.split(":",1)[1].strip().lower() for player in open("players.txt")]
participant_dictionary = {}

i=0
for player in players:
    participant_dictionary[player] = gifts[i]
    i+=1
try:
    assignments = assign(players, gifts)
    while True:
        player = raw_input("What's your name?\n").lower()
        while player not in players:
            player = raw_input("You misspelled your name lol. Try again.\n").lower()

        print("You're assigned to " + assignments[player].capitalize() + " and he/she/xhe wants " + participant_dictionary[assignments[player]] +".")
        if raw_input("\nPress enter to clear screen for the next person or q to quit.\n") == 'q':
            print "Have fun!"
            exit()
        os.system("clear")
except IndexError:
    pass

