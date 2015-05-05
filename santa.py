import random
import os

def assign(players):
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


players = [player.strip() for player in open("players.txt")]
assignments = assign(players)
while True:
    player = input("What's your name?\n")
    if player == "q":
        exit()
    print("You're assigned to " + assignments[player])
    if input("\nPress enter to clear screen\n") == 'q':
        exit()
    os.system("clear")
