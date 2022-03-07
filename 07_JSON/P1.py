# Create class Vehicle with properties name, engine, and price. Create vehicle object and convert it into JSON and vice-versa.

import json

class Vehicle:
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

v1 = Vehicle('shine','1-cylinder',75000)
print(json.dumps(v1.__dict__))
