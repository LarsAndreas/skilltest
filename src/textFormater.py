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