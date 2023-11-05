import json
import os


def readConfig():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    configFile = open(os.path.join(__location__, "settings.json"))
    return json.load(configFile)
