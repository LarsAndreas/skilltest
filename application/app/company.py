from jsonHelper import jsonHelper

class Company:

    def getDictionary(json):
        return {
            "Organisasjonsnummeret": jsonHelper.getIfExists(json, ["organisasjonsnummer"]),
            "Navn": jsonHelper.getIfExists(json, ["navn"]),
            "Antall ansatte": jsonHelper.getIfExists(json, ["antallAnsatte"]),
            "Organisasjonsform": jsonHelper.getIfExists(json, ["organisasjonsform", "beskrivelse"]),
            "Hjemmeside": jsonHelper.getIfExists(json, ["hjemmeside"]),
            "Forretningsadresse": jsonHelper.listToString(jsonHelper.getIfExists(json, ["forretningsadresse", "adresse"])),
            "Postnummer (forretningsadresse)": jsonHelper.getIfExists(json, ["forretningsadresse", "postnummer"]),
            "Postadresse": jsonHelper.getIfExists(json, ["postadresse", "adresse"]),
            "Postnummer (postadresse)": jsonHelper.getIfExists(json, ["postadresse", "postnummer"]),
            "Konkurs": jsonHelper.getIfExists(json, ["konkurs"]),
            "Målform": jsonHelper.getIfExists(json, ["maalform"])
        }