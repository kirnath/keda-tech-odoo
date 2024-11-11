import requests
import json


print("Testing started")

print("Get All Materials")
url = 'http://localhost:8069/materials'
session = requests.Session()
session.get(url)
materials = json.loads(session.get(url).text)
# print(materials)
if len(materials) >= 1:
    print("Test Passed")

print("Create Material => VALID DATA")
create_url = 'http://localhost:8069/materials/create'
data = {
        'name': 'test create',
        'code': 'TCRT-001',
        'type': 'fabric',
        'buy_price': 10000,
        'related_supplier': 1
}
res = session.post(create_url, data=data).text
ress = json.loads(res)
if ress['success'] == True:
    print(res)
    print("Test Passed")
else:
    print(res)
    print("Test Failed")


print("Create Material => INVALID DATA")
create_url = 'http://localhost:8069/materials/create'
data = {
        'name': 'test create',
        # 'code': 'TCRT-001', # MISSING CODE
        # 'type': 'fabric', # MISSING TYPE
        'buy_price': 10000,
        'related_supplier': 1
}
res = session.post(create_url, data=data).text
ress = json.loads(res)
if ress['success'] == False:
    print(res)
    print("Test Passed")
else:
    print("Test Failed")    


print("Update Material => VALID DATA")
update_url = 'http://localhost:8069/materials/update'
data = {
    'id': 8, # ADJUST WITH VALID ID
    'name': 'test update',
    'code': 'UUPDT-001',
    'type': 'fabric',
    'buy_price': 10000,
    'related_supplier': 1
}
res = session.post(update_url, data=data)
print(res.text)

print("Update Material => INVALID")
update_url = 'http://localhost:8069/materials/update'
data = {
    'id': 7,
    'name': 'test update',
    # 'code': 'UUPDT-001', # MISSING CODE
    # 'type': 'fabric', # MISSING TYPE
    'buy_price': 10000,
    'related_supplier': 1
}
res = session.post(update_url, data=data).text
ress = json.loads(res)
if ress['success'] == False:
    print(res)
    print("Test Passed")
else:
    print("Test Failed")


print("Delete Material Data => VALID ID")
delete_url = 'http://localhost:8069/materials/delete'
data = {
    'id': 8 # ADJUST WITH VALID ID
}
res = session.delete(delete_url, data=data).text
ress = json.loads(res)
if ress['success'] == True:
    print(res)
    print("Test Passed")
else:
    print("Test Failed")



print("Delete Material Data => INVALID ID")
delete_url = 'http://localhost:8069/materials/delete'
data = {
    'id': 999 # INVALID ID / NOT EXISTS
}
res = session.delete(delete_url, data=data).text
ress = json.loads(res)
if ress['success'] == False:
    print(res)
    print("Test Passed")
else:
    print("Test Failed")


print("Delete Material Data => UNDEFINED ID")
delete_url = 'http://localhost:8069/materials/delete'
data = {
    'id': '' # ID NOT DEFINED
}
res = session.delete(delete_url, data=data).text
ress = json.loads(res)
if ress['success'] == False:
    print(res)
    print("Test Passed")
else:
    print("Test Failed")

print("8/8 Test Completed")