import json
import numpy as np
import matplotlib.pyplot as plt


def getEventInfo(event):
    timeArray = [((event['period']-1)*45)+int(event['timestamp'].split('.')[0].split(':')[1]), int(event['timestamp'].split('.')[0].split(':')[-1]), int(event['timestamp'].split('.')[-1])]
    return


game = '3788747'


with open('open-data-master/data/three-sixty/' + game + '.json', encoding='utf-8') as f:
    threeSixty = json.load(f)

with open('open-data-master/data/events/' + game + '.json', encoding='utf-8') as f:
    eventData = json.load(f)


getEventInfo(eventData[-1])

