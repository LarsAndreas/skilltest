from jsonHelper import jsonHelper

class Company:

    brrgDictionary = {
            "Organisasjonsnummeret": ["organisasjonsnummer"],
            "Navn": ["navn"],
            "Antall ansatte": ["antallAnsatte"],
            "Organisasjonsform": ["organisasjonsform", "beskrivelse"],
            "Hjemmeside": ["hjemmeside"],
            "Forretningsadresse": ["forretningsadresse", "adresse"],
            "Postnummer (forretningsadresse)": ["forretningsadresse", "postnummer"],
            "Postadresse": ["postadresse", "adresse"],
            "Postnummer (postadresse)": ["postadresse", "postnummer"],
            "Konkurs": ["konkurs"],
            "Målform": ["maalform"]
        }

    def getDictionary(json):
        return {k: jsonHelper.getAndFormat(json, v) for k, v in Company.brrgDictionary.items()}