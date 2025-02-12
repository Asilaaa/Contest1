import json
class Game:
    def __init__(self, values):
        self.values = values

    def typeBasedTransformer(self):
        res = {}

        for value in self.values:
            try:
                value = json.loads(value)
            except:
                pass

            if isinstance(value, bool):
                res[value] = not value
            elif isinstance(value, int) or isinstance(value, float):
                res[value] = value ** 2
            elif isinstance(value, str):
                res[value] = value[::-1]
            elif isinstance(value, (list, tuple)):
                res[tuple(value)] = list(value[::-1])
            elif isinstance(value, dict):
                res[tuple(value.items())] = {v: k for k, v in value.items()}
            else:
                res[value] = value

        return res