import json


with open('open-data-master/data/events/3788747.json', encoding='utf-8') as f:
    eventData = json.load(f)


events = []
keys = []
for event in eventData:
    if event['type']['name'] not in events:
        events.append(event['type']['name'])
        keys.append(event.keys())


for i in range(len(events)):
    print(events[i])
    print(keys[i], '\n')

