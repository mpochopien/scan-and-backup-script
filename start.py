import os
import requests
import random
import string
from datetime import datetime

from printMessage import printMessage
from scanPc import scanPc, offlineScanPc
from configReader import readConfig
from updateSoftware import updateSoftware
from clearTmpDirectory import clearTmpDirectory


def main():
    config = readConfig()

    updateSoftware()

    clearTmpDirectory()

    downloadFromRepo(config)

    scanPc()

    backupFileName = generateOutputFileName(config)

    makeBackup(config, backupFileName)

    offlineScanPc()
    turnOffPc(config)

    printMessage("Backup finished!")


def makeBackup(config, backupFileName):
    printMessage("Starting backup")
    files = ' '.join(config["input"])
    randomPassword = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    os.system(f"7zr.exe a -t7z -spf -p{randomPassword} {backupFileName} {files}")


def turnOffPc(config):
    if config["turnOffPcAfterFinish"]:
        printMessage("Backup finished! Turning off PC in 30 seconds...")
        os.system("shutdown /s /t 30")


def generateOutputFileName(config):
    name = config["outputDir"] + "\\" + config['outputName']
    if config['addDateToOutputName']:
        name += "_" + datetime.now().strftime("%Y-%m-%d")

    return name + ".zip"


def downloadFromRepo(config):
    for repo in config['repos']:
        printMessage(f"Downloading {repo['name']}")
        file = requests.get(repo['url'], allow_redirects=True)
        open(repo['name'], 'wb').write(file.content)


if __name__ == '__main__':
    main()
