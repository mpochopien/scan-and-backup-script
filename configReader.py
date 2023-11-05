import json


def readConfig():
    configFile = open('settings.json')
    return json.load(configFile)
