from configReader import readConfig
from printMessage import printMessage
import os


def clearTmpDirectory():
    config = readConfig()

    if config["clearTmpFolder"]:
        printMessage("Clearing temporary files")
        os.system("del /S /q C:\\Users\\%USERNAME%\\AppData\\Local\\Temp\\*")
        printMessage("Temporary files cleared")