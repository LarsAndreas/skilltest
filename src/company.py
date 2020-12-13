from src.jsonHelper import jsonHelper

class Company:

    def __init__(self, json):
        self.json = json

    def getDictionary(self):
        return {
            "Organisasjonsnummeret": jsonHelper.getIfExists(self.json, ["organisasjonsnummer"]),
            "Navn": jsonHelper.getIfExists(self.json, ["navn"]),
            "Antall ansatte": jsonHelper.getIfExists(self.json, ["antallAnsatte"]),
            "Organisasjonsform": jsonHelper.getIfExists(self.json, ["organisasjonsform", "beskrivelse"]),
            "Hjemmeside": jsonHelper.getIfExists(self.json, ["hjemmeside"]),
            "Forretningsadresse": jsonHelper.listToString(jsonHelper.getIfExists(self.json, ["forretningsadresse", "adresse"])),
            "Postnummer (forretningsadresse)": jsonHelper.getIfExists(self.json, ["forretningsadresse", "postnummer"]),
            "Postadresse": jsonHelper.getIfExists(self.json, ["postadresse", "adresse"]),
            "Postnummer (postadresse)": jsonHelper.getIfExists(self.json, ["postadresse", "postnummer"]),
            "Konkurs": jsonHelper.getIfExists(self.json, ["konkurs"]),
            "Målform": jsonHelper.getIfExists(self.json, ["maalform"])
        }