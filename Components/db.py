class Database:
    _instance = None

    def __init__(self):
        self.db={};

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def add_item(self, name, value):
        self.db[name] = value

    def get_value(self, name):
        return self.db[name]

    def get_keys(self):
        return self.db.keys()
