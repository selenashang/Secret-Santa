import random
import os

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
    return secret_santas

players = [player.split(":",1)[0].lower() for player in open("players.txt")]
gifts = [player.split(":",1)[1].strip().lower() for player in open("players.txt")]
participant_dictionary = {}

i=0
for player in players:
    participant_dictionary[player] = gifts[i]
    i+=1

assignments = assign(players, gifts)
while True:
    player = raw_input("What's your name?\n").lower()
    if player == "q":
        exit()
    print("You're assigned to " + assignments[player].capitalize() + " and she wants " + participant_dictionary[assignments[player]] +".")
    if raw_input("\nPress enter to clear screen or 'q' to quit\n") == 'q':
        exit()
    os.system("clear")



