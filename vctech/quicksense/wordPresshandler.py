import json
import os
from vctech.logger import Logger

current_directory = os.getcwd()
folder_name = "dataStore"
folder_path = os.path.join(current_directory, folder_name)

class WordPressHandler():
    def save_json(data, file_path):
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def createContent(response,id):
        Logger.log("createcontent called")
        save_path = os.path.join(folder_path, str(id)+".json")
        WordPressHandler.save_json(response, save_path)
        Logger.log("json stored sucessfully")

    def getContent(id):
        file_path = os.path.join(folder_path, str(id)+".json")
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
