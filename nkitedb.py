import json
import os

class NKiteDB:
    def __init__(self, filename="database.json"):
        self.filename = filename
        self.data = self._load_data()
    
    def _load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    
    def _save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
    
    def insert(self, collection, document):
        if collection not in self.data:
            self.data[collection] = []
        self.data[collection].append(document)
        self._save_data()
    
    def find(self, collection, query=None):
        if collection not in self.data:
            return []
        if query is None:
            return self.data[collection]
        return [doc for doc in self.data[collection] if all(doc.get(k) == v for k, v in query.items())]
    
    def get_first(self, collection, query):
        results = self.find(collection, query)
        return results[0] if results else None
    
    def update(self, collection, query, update_data):
        if collection not in self.data:
            return False
        updated = False
        for doc in self.data[collection]:
            if all(doc.get(k) == v for k, v in query.items()):
                doc.update(update_data)
                updated = True
        if updated:
            self._save_data()
        return updated
    
    def delete(self, collection, query):
        if collection not in self.data:
            return False
        initial_length = len(self.data[collection])
        self.data[collection] = [doc for doc in self.data[collection] if not all(doc.get(k) == v for k, v in query.items())]
        if len(self.data[collection]) < initial_length:
            self._save_data()
            return True
        return False
    
    def get_all(self, collection):
        return self.data.get(collection, [])
