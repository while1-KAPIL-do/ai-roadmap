import json

product = {
    "id"        : 101,
    "name"      : "Protien Powder",
    "price"     : 1200,
    "in_stock"  : True
}

jsonData = json.dumps(product) # python-dict -> json-string
print(jsonData)
# print(jsonData['name'])

#######
jsonString = '{"id": 101, "name": "Protien Powder", "price": 1200, "in_stock": true}'
data = json.loads(jsonString) # json-string -> python-dict
print(data)
print(data['name'])


#######
pythonDict = {
    "id"        : 102,
    "name"      : "Cratine Powder",
    "price"     : 600,
    "in_stock"  : False
}
jsonDataStr = json.dumps(pythonDict)
print(jsonDataStr)
pythonDict = json.loads(jsonDataStr)
print(pythonDict)


####### Read the file
with open("/home/kapil/ai-roadmap/week2/product.json", "r") as file:
    product = json.load(file)
print(product)
print(product['price'])



####### Write the file
newProduct = {
    "id"        : 104,
    "name"      : "Coke Bottle",
    "price"     : 85,
    "in_stock"  : True
}

with open("/home/kapil/ai-roadmap/week2/new_product.json", "w") as file:
    json.dump(newProduct, file, indent=2)




######## IMP
# json.load(file)         -> read from files
# json.loads(jsonString)  -> read from string

# json.dump(newProduct, file, indent=2)   -> pythonDict to json file
# json.dumps(product)                     -> pythonDict to json string

