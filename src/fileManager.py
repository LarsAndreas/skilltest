import os
from os import path

class fileManager:

    @staticmethod
    def getPath(nr):
        return f'./static/data/orgnr/{nr}'

    @staticmethod
    def removeNr(nr):
        #check that you have a saved version of that org number
        if os.path.exists(fileManager.getPath(nr)):
            #delete that file
            os.remove(fileManager.getPath(nr))

    @staticmethod
    def readInfo(nr):
        #check that you have a saved version of that org number
        if os.path.exists(fileManager.getPath(nr)):
            with open(fileManager.getPath(nr), 'r') as file:
                return file.read()
        return None

    @staticmethod
    def saveInfo(nr, information):
        with open(fileManager.getPath(nr), 'w') as file:
            file.write(information)

    @staticmethod
    def getAllOrgNr():
        return list(os.listdir("./static/data/orgnr"))