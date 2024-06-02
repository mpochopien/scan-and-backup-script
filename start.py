import os
import requests
from datetime import datetime

from onedriveCloudProvider import sendBackupToCloud
from printMessage import printMessage
from scanPc import scanPc, offlineScanPc
from configReader import readConfig


def main():
    config = readConfig()
    downloadFromRepo(config)

    scanPc()

    backupFileName = generateOutputFileName(config)

    makeBackup(config, backupFileName)
    sendBackupToCloud(backupFileName)

    offlineScanPc()
    turnOffPc(config)

    printMessage("Backup finished!")


def makeBackup(config, backupFileName):
    printMessage("Starting backup")
    files = ' '.join(config["input"])
    os.system(f"7zr.exe a -t7z -spf -p{config['backupPassword']} {backupFileName} {files}")


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
