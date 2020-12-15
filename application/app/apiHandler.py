from company import Company
from jsonHelper import jsonHelper
import requests

class apiHandler:

    @staticmethod
    def getRequest(url, param=""):
        mainRequest = requests.get(url + param)
        if(mainRequest):
            return mainRequest

    @staticmethod
    def getOrgInfo(nr):
        #Check if org on mainUrl
        mainRequest = apiHandler.getRequest(URL.mainUrl, nr)
        if(mainRequest):
            return mainRequest

        #Check if org on subUrl
        subRequest = apiHandler.getRequest(URL.subUrl, nr)
        if(subRequest):
            return subRequest

        return None

    @staticmethod
    def getNames(nrs):
        names = []
        for nr in nrs:
            infoDictionary = apiHandler.getDictionary(nr)
            names.append(infoDictionary["Navn"])
        return names

    @staticmethod
    def getPostNumbers(postNr):
        apiUrl = URL.postNrUrl + postNr
        apiUrlRequest = requests.get(apiUrl)
        if(apiUrlRequest):
            jsonDictionary = apiUrlRequest.json()
            if("_embedded" in jsonDictionary):
                companies = [ (company["organisasjonsnummer"], company["navn"]) for company in jsonDictionary["_embedded"]['enheter']]
                return companies
        return []

    @staticmethod
    def getCoordinates(nr):
        response = apiHandler.getOrgInfo(nr)
        if not response:
            return []
        else:
            adresses = response.json()["forretningsadresse"]["adresse"]
        
            coordinates = []
            for adress in adresses:
                #geonorge.no api
                apiUrlRequest = apiHandler.getRequest(URL.coordinatesUrl, adress)
                if(apiUrlRequest):
                    jsonDictionary = apiUrlRequest.json()
                    if(jsonDictionary["adresser"]):
                        #There is only one adress (We can therefore pick out the first element)
                        adressInfo = jsonDictionary["adresser"][0]
                        latitude = adressInfo["representasjonspunkt"]["lat"]
                        longitude = adressInfo["representasjonspunkt"]["lon"]
                        coordinates.append([adress, latitude, longitude])
            return coordinates


    @staticmethod
    def getDictionary(nr):
        orgJson = apiHandler.getOrgInfo(nr)
        if orgJson:
            return Company.getDictionary(orgJson.json())
        else:
            return Company.getDictionary({})

class URL:
    #from brreg api
    apiLink = "https://data.brreg.no/enhetsregisteret/api/"
    mainUrl = "https://data.brreg.no/enhetsregisteret/api/enheter/"
    subUrl = "https://data.brreg.no/enhetsregisteret/api/underenheter/"
    postNrUrl = "https://data.brreg.no/enhetsregisteret/api/enheter/?forretningsadresse.postnummer="

    #from geonorge.no api
    coordinatesUrl = "https://ws.geonorge.no/adresser/v1/sok?adressetekst="