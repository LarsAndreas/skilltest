import os
from os import path

class fileManager:

    basePath = "./app/static/data/orgnr/"

    @staticmethod
    def getPath(nr):
        return fileManager.basePath + nr

    @staticmethod
    def removeNr(nr):
        if os.path.exists(fileManager.getPath(nr)):
            os.remove(fileManager.getPath(nr))

    @staticmethod
    def readInfo(nr):
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
        return list(os.listdir(fileManager.basePath))