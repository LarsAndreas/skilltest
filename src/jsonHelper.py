class jsonHelper:

    @staticmethod
    def getIfExists(json, keys):
        for key in keys:
            if not key in json:
                return "Unknown"
            json = json[key]
        return json

    @staticmethod
    def listToString(li):
        if isinstance(li, list):
            return ",".join(li)
        return li