# Create class Vehicle with properties name, engine, and price. Create vehicle object and convert it into JSON and vice-versa.

import json

class Vehicle:
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

v1 = Vehicle('shine','1-cylinder',75000)

with open('vehicleProperty.json','w') as obj:
    json.dump(v1.__dict__,obj)
    
with open('vehicleProperty.json','r') as obj:
    v2 = json.load(obj)
    
v3 = Vehicle(**v2)
print(v3.name)







# import json

# class Vehicle:
#     def __init__(self,name,engine,price):
#         self.name = name
#         self.engine = engine
#         self.price = price

# v1 = Vehicle('shine','1-cylinder',75000)
# print('class object: ',v1.__dict__,type(v1),v1.name)

# json_data = json.dumps(v1.__dict__)
# print('JSON data: ',json_data,type(json_data))

# v2 = json.loads(json_data,object_hook = lambda d : Vehicle(**d))

# print('Class Object: ',v2.__dict__,type(v2),v1.name)
