from configReader import readConfig
from printMessage import printMessage
import os


def updateSoftware():
    config = readConfig()

    if config["updateSoftwareByWinget"]:
        printMessage("Updating software")
        os.system("winget upgrade --all --silent --verbose")
        printMessage("Updates finished")
