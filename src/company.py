from src.jsonHelper import jsonHelper

class Company:

    def __init__(self, json):
        self.json = json

    def getDictionary(self):
        return {
            "Organisasjonsnummeret": jsonHelper.getIfExists(self.json, "organisasjonsnummer"),
            "Navn": jsonHelper.getIfExists(self.json, "navn"),
            "Organisasjonsform": jsonHelper.getIfExists(self.json, "organisasjonsform"),
            "Hjemmeside": jsonHelper.getIfExists(self.json, "hjemmeside"),
            "Forretningsadresse": ",".join(jsonHelper.getIfExists(self.json, "forretningsadresse")),
            "Konkurs": jsonHelper.getIfExists(self.json, "konkurs"),
            "Målform": jsonHelper.getIfExists(self.json, "maalform")
        }