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

    def set(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError(f'Key {key} is absent')
                    
    def add(self, key, value):

        if key in self.data:
            raise Exception
        else:
            d = {key : value}
            self.data.update(d)
            print(self.data)