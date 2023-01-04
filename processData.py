import json
import numpy as np


# all notable events have ['id', 'index', 'period', 'timestamp', 'minute', 'second', 'type', 'possession', 'possession_team', 'play_pattern', 'team', 'player', 'position', 'location']


class Event():
    def __init__(self, event):
        self.event = event
        return

    def getTimeArray(self):
        dateTimeSplit = self.event['timestamp'].split('.')[0].split(':')
        self.time = [((self.event['period']-1)*45)+int(dateTimeSplit[1]), int(dateTimeSplit[-1]), int(self.event['timestamp'].split('.')[-1])]
        return

    def findEventLoc(self):
        if 'location' in self.event.keys():
            location = self.event['location']
        else:
            location = None
        self.loc = location
        return

    def sortEvent(self, threeSixty):
        self.getTimeArray()
        self.findEventLoc()
        view = [threeSixty[i] for i in range(len(threeSixty)) if threeSixty[i]['event_uuid'] == self.event['id']][0]
        print(view, '\n')
        self.eventType = self.event['type']['name']
        self.player = self.event['player']['name']
        self.eventTeam = self.event['team']['name']
        return

    def sortAttackandDefence(self, view):
        self.attackers = [player for player in view['freeze_frame'] if player['teammate'] == True]
        self.defenders = [player for player in view['freeze_frame'] if player['teammate'] == False]
        return


game = '3788747'

with open('open-data-master/data/three-sixty/' + game + '.json', encoding='utf-8') as f:
    threeSixty = json.load(f)

with open('open-data-master/data/events/' + game + '.json', encoding='utf-8') as f:
    eventData = json.load(f)


event = Event(eventData[15])
event.sortEvent(threeSixty)
event.sortAttackandDefence()

