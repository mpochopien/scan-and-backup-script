from configReader import readConfig
from printMessage import printMessage
import os


def scanPc():
    config = readConfig()

    if config["scanPc"]:
        printMessage("Starting scan")
        os.system("adwcleaner.exe /clean /noreboot")
        os.system("cd /d C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\4* && MpCmdRun.exe -scan -scantype 2")
        printMessage("Scanning finished")


def offlineScanPc():
    config = readConfig()

    if config["offlineScan"]:
        printMessage("Starting offline scan")
        os.system("Start-MpWDOScan")
        return 0
