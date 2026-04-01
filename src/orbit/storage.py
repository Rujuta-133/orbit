class InMemoryStorage:
    def __init__(self):
        self.storage_list = []

    def load(self):
        return self.storage_list[:]
        
    def save(self, tasks):
        self.storage_list = tasks[:]
