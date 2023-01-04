from processData import Event, loadInData
import numpy as np
import pandas as pd
import sys


class Player():
    def __init__(self, name, team, locs=[]):
        return


# for each event, find the player that did it.

# add their location if they are the actor for the event

# for each other player, find the previous action and then find the most feasible location to this from their teams co-ordinates in the event. 

# find the location of the ball

# for each player, their first coordinates will appear once they have an affect on the game



# we can then loop through each player and find the resulting backwards locations before they first appeared in the 360 view

# add all to a pd df, then write code to fill in the blanks


def printName(word):
    try:
        print(word)
    except UnicodeEncodeError:
        if sys.version_info >= (3,):
            print(word.encode('utf8').decode(sys.stdout.encoding))
        else:
            print(word.encode('utf8'))
    return


game = '3788747'
eventData, threeSixty = loadInData(game)
for i in range(len(eventData)):
    event = Event(eventData[i])
    event.sortEvent(threeSixty)
    if 'actorLoc' in event.__dict__.keys():
        string = str(event.player) + ' ' + str(event.actorLoc) + ' ' + str(event.eventTeam) + '\n'
        printName(string)




