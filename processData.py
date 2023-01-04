import json
import numpy as np
import matplotlib.pyplot as plt


# all notable events have ['id', 'index', 'period', 'timestamp', 'minute', 'second', 'type', 'possession', 'possession_team', 'play_pattern', 'team', 'player', 'position', 'location']


class Event():
    def __init__(self, event):
        self.event = event
        return

    def theNolive(self):
        return


def getEventInfo(event, threeSixty):
    # find the time of the event in an array format
    timeArray = [((event['period']-1)*45)+int(event['timestamp'].split('.')[0].split(':')[1]), int(event['timestamp'].split('.')[0].split(':')[-1]), int(event['timestamp'].split('.')[-1])]

    # find the location of the event
    if 'location' in event.keys():
        location = event['location']
    else:
        location = None

    # find the corresponding 360 view of the event from the other file
    view = [threeSixty[i] for i in range(len(threeSixty)) if threeSixty[i]['event_uuid'] == event['id']][0]

    eventType = event['type']['name']
    player = event['player']['name']
    print(player)
    print(eventType)
    print(timeArray)
    print(location)
    print(view)
    return


game = '3788747'

with open('open-data-master/data/three-sixty/' + game + '.json', encoding='utf-8') as f:
    threeSixty = json.load(f)

with open('open-data-master/data/events/' + game + '.json', encoding='utf-8') as f:
    eventData = json.load(f)


getEventInfo(eventData[15], threeSixty)

