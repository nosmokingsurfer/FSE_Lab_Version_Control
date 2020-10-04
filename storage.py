class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self):
        pass

    def set(self):
        pass

    def add(self):   #Катя
        key = key
        value = value

        if key in self.data.keys():
            raise Exception
        else:
            d = {key : value}
            self.data.update(d)
            print(self.data)
