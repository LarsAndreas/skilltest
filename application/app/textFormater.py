class textFormater:

    @staticmethod
    def format(text):
        text = textFormater.removeWhiteSpace(text)
        text = textFormater.removeDots(text)
        return text

    @staticmethod
    def removeWhiteSpace(text):
        return text.replace(" ", "")

    @staticmethod
    def removeDots(text):
        return text.replace(".", "")

    @staticmethod
    def validOrgNr(nr):
        return nr.isdigit() and len(nr)==9

    @staticmethod
    def validPostNr(nr):
        return nr.isdigit() and len(nr)==4