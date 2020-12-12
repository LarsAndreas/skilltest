import requests

class apiHandler:
    def __init__(self, url):
        self.url = url

    def convertKeysToValue(self, key, json):

        # if entry is a dictionary
        if isinstance(key, dict):
            #get key of dictionary
            firstJsonKey = list(key.keys())[0]
            
            #check if key in json
            if firstJsonKey in json:
                
                #check if subEntry also is a dictioanry
                if isinstance(json[firstJsonKey], dict):
                    #map the keys to values, and concatinates with "," seperator if list
                    mappedKeys = [str(json[firstJsonKey][subKey]) if not isinstance(json[firstJsonKey][subKey], list) else ",".join(json[firstJsonKey][subKey]) for subKey in key[firstJsonKey]]
                    return " ".join(mappedKeys)
        else:
            # check if key in json
            if key in json:
                return json[key]
        #return an empty string if missing value in json
        return ""

    
    def getJsonFromApi(self):
        requestModule = requests.get(self.url)
        print(requestModule)
        return requestModule.json()

    def isError(self):
        requestModule = requests.get(self.url)
        return requestModule.status_code != 200

class brregApiHandler(apiHandler):

    def __init__(self, nr):
        self.nr = nr
        super().__init__(f"https://data.brreg.no/enhetsregisteret/api/enheter/{self.nr}")

    basisopplMappingNameToKey = {
        "Navn": "navn",
        "Organisasjonsnummer": "organisasjonsnummer",
        "Næringskode(r)": {"naeringskode1": ["kode", "beskrivelse"]},
        "Institusjonell sektorkode": {"institusjonellSektorkode": ["kode", "beskrivelse"]},
        "Siste innsendte årsregnskap": "sisteInnsendteAarsregnskap",
        "Målform": "maalform"
    }

    addresserMappingNameToKey = {
        "Forretningsadresse": {"forretningsadresse": ["adresse", "postnummer","kommune", "kommunenummer", "kommune", "land",]},
        "Hjemmeside": "hjemmeside"
    }

    def getopplMappingNameToValue(self):
        #get json from api based on orgnr
        jsonOrgInfo = self.getJsonFromApi()

        #map dictionary values keys to the values given by json
        basisOpplMappingNameToKey = {k: self.convertKeysToValue(v, jsonOrgInfo) for k, v in brregApiHandler.basisopplMappingNameToKey.items()}
        adresseMappingNameToKey = {k: self.convertKeysToValue(v, jsonOrgInfo) for k, v in brregApiHandler.addresserMappingNameToKey.items()}

        #combine information snippets
        opplMappingNameToKey = {}
        opplMappingNameToKey.update(basisOpplMappingNameToKey)
        opplMappingNameToKey.update(adresseMappingNameToKey)

        #return the api converted dictionary
        return opplMappingNameToKey