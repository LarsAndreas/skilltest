from src.company import Company
import requests

class apiHandler:

    mainUrl = "https://data.brreg.no/enhetsregisteret/api/enheter/"
    subUrl = "https://data.brreg.no/enhetsregisteret/api/underenheter/"

    def __init__(self, nr):
        self.nr = nr
        self.requestModule = self.getOrgInfo()

    def getRequest(self, url):
        mainRequest = requests.get(url + self.nr)
        if(mainRequest):
            return mainRequest

    def getOrgInfo(self):
        mainRequest = self.getRequest(apiHandler.mainUrl)
        if(mainRequest):
            return mainRequest

        subRequest = self.getRequest(apiHandler.subUrl)
        if(subRequest):
            return subRequest

        return None

    @staticmethod
    def getNames(nrs):
        names = []
        for nr in nrs:
            apiHandle = apiHandler(nr)
            infoDictionary = apiHandle.getDictionary()
            names.append(infoDictionary["Navn"])
        return names


    def getDictionary(self):
        if self.requestModule:
            companyObject = Company(self.requestModule.json())
        else:
            companyObject = Company({})
        return companyObject.getDictionary()