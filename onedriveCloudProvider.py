from graph_onedrive import OneDrive
from graph_onedrive import OneDriveManager

from configReader import readConfig
from printMessage import printMessage
import os


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def sendBackupToCloud(backupFileName):
    config = readConfig()

    if config["sendBackupToCloud"]:
        printMessage("Sending backup to cloud")

        authorizeToOneDrive()
        with OneDriveManager(config_path=os.path.join(__location__, "settings.json"), config_key="onedrive") as my_drive:
            items = my_drive.list_directory()

            dest_folder_id = None
            for item in items:
                if "folder" in item and item.get("name") == config["cloudBackupDir"]:
                    dest_folder_id = item["id"]
                    break

            if dest_folder_id is None:
                raise Exception(
                    f"Could not find a folder named {config["cloudBackupDir"]} in the root of the OneDrive"
                )

            my_drive.upload_file(
                file_path=backupFileName, parent_folder_id=dest_folder_id, verbose=True
            )
    else:
        return


def authorizeToOneDrive():
    config_file_name = os.path.join(__location__, "settings.json")
    directory_of_this_file = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(directory_of_this_file, config_file_name)

    config_key = "onedrive"

    my_drive = OneDrive.from_file(config_path, config_key)
    my_drive.to_file(config_path, config_key)