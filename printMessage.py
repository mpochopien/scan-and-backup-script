from datetime import datetime

def printMessage(message):
    print("[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] " + message)