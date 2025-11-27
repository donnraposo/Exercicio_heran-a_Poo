import json
import os

class BaseModel:

    def save(self, data):

        list = self.load_all()

        list.append(data)

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(list, f, indent=4, ensure_ascii=False)
    @classmethod
    def load_all(self):
        if not os.path.exists(self.file):
            return []
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)
        
        