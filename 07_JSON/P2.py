# Write a code to load a .json file and print JSON data. Display error if a file is empty or data is not in a json format.  

import json

try:
    open_json_file = open('/home/wot-aksh/Desktop/Python_Training/07_JSON/EmployeeData.json')
    data = json.load(open_json_file)
    for item in data:
        print(item['name'])
except Exception as e:
    print(type(e).__name__,e) 
