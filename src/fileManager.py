import os
from os import path

class fileManager:

    @staticmethod
    def removeNr(nr):
        #get file path for nr
        path = f'./static/data/orgnr/{nr}'

        #check that you have a saved version of that org number
        if os.path.exists(path):
            #delete that file
            os.remove(path)

    @staticmethod
    def readInfo(nr):
        #get file path for nr
        path = f'./static/data/orgnr/{nr}'

        #check that you have a saved version of that org number
        if os.path.exists(path):
            with open(path, 'r') as file:
                return file.read()
        return None

    @staticmethod
    def saveInfo(nr, information):
        with open(f'static/data/orgnr/{nr}', 'w') as file:
            file.write(information)

    @staticmethod
    def getAllOrgNr():
        return list(os.listdir("./static/data/orgnr"))