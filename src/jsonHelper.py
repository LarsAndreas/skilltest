class jsonHelper:

    @staticmethod
    def getIfExists(json, key):
        if key in json:
            return json[key]
        return "Unknown"