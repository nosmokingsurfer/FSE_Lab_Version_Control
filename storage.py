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

    def remove(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError("Key \"%s\" does not exist" % key)

    def set(self):
        pass
    
    def add(self):
        pass