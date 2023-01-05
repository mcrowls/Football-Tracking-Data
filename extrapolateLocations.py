from processData import Event, loadInData
import numpy as np
import pandas as pd
import sys


class Player():
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.locs = []
        return


    def extrapolate(self, timeDiff, coords=None, maxSpeed=8):
        maxPossDist = maxSpeed * timeDiff
        if self.locs == [] or self.locs[-1] == [] or coords==None:
            self.locs.append([])
        else:
            possibleCoords = [coord for coord in coords if distance(coord, self.locs[-1]) < maxPossDist]
            print(self.locs[-1], possibleCoords, timeDiff)
        return


    def determineActor(self, event, timeDiff):
        if self.name == event.player:
            self.locs.append(event.loc)
        else:
            if self.team == event.eventTeam:
                if 'teammates' in event.__dict__.keys():
                    self.extrapolate(timeDiff, coords=event.teammates)
            else:
                if 'opponents' in event.__dict__.keys():
                    self.extrapolate(timeDiff, coords=event.opponents)
        return




# for each event, find the player that did it.

# add their location if they are the actor for the event

# for each other player, find the previous action and then find the most feasible location to this from their teams co-ordinates in the event. 

# find the location of the ball

# for each player, their first coordinates will appear once they have an affect on the game

# we can then loop through each player and find the resulting backwards locations before they first appeared in the 360 view

# add all to a pd df, then write code to fill in the blanks


def distance(arr1, arr2):
    return np.sqrt(((arr1[0] - arr2[0])**2 + (arr1[1] - arr2[1])**2))


def printName(word):
    try:
        print(word)
    except UnicodeEncodeError:
        if sys.version_info >= (3,):
            print(word.encode('utf8').decode(sys.stdout.encoding))
        else:
            print(word.encode('utf8'))
    return


def getTeams(team):
    LineUp = team['tactics']['lineup']
    players = []
    for player in LineUp:
        players.append(player['player']['name'])
    return players, team['team']['name']


def createTeam(squad, teamName):
    return [Player(name, teamName) for name in squad]


def calcSeconds(time):
    return time[0]*60 + time[1] + time[-1]/1000


game = '3788747'
eventData, threeSixty = loadInData(game)
homeSquad, homeName = getTeams(eventData[0])
awaySquad, awayName = getTeams(eventData[1])
home = createTeam(homeSquad, homeName)
away = createTeam(awaySquad, awayName)


oldTime = 0
for i in range(5, 30):
    event = Event(eventData[i])
    event.sortEvent(threeSixty)
    newTime = calcSeconds(event.time)
    timeDiff = newTime - oldTime
    for player in (home + away):
        player.determineActor(event, timeDiff)
    oldTime = newTime