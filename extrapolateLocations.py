from processData import Event, loadInData
import numpy as np
import pandas as pd


game = '3788747'
eventData, threeSixty = loadInData(game)
event = Event(eventData[15])
event.sortEvent(threeSixty)