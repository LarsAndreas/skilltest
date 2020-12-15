class jsonHelper:

    unknown = "Ukjent"
    true = "Ja"
    false = "Nei"

    @staticmethod
    def getAndFormat(inp, keys):
        for key in keys:

            if inp is None:
                return jsonHelper.unknown

            if not key in inp:
                return jsonHelper.unknown

            inp = inp[key]

        if isinstance(inp, bool):
            return jsonHelper.boolFormat(inp)

        if isinstance(inp, list):
            return jsonHelper.listFormat(inp)

        if isinstance(inp, str):
            return inp

        if isinstance(inp, int):
            return inp

    @staticmethod
    def boolFormat(inp):
        if inp:
            return jsonHelper.true
        else:
            return jsonHelper.false

    @staticmethod
    def listFormat(inp):
        return ", ".join(inp)