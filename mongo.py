import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabase"]
'''print(myclient.list_database_names())
dblist=myclient.list_database_names()
if "mydatabase" in dblist:
    print('the database exists')
else:
    print("database doesnot exists")'''

'''collist=mydb.list_collection_names()
if "mycollection" in collist:
    print("the collection exists")
else:
    print("Collection doesnot exists")'''

mycol=mydb["mycollection"]
#mydict={"name":"mahender","address":"dharamaram 50277" }

#x=mycol.insert_one(mydict)
'''mylist = [
{ "name": "Amy", "address": "Apple st 652"},
{ "name": "Hannah", "address": "Mountain 21"},
{ "name": "Michael", "address": "Valley 345"},
{ "name": "Sandy", "address": "Ocean blvd 2"},
{ "name": "Betty", "address": "Green Grass 1"},
{ "name": "Richard", "address": "Sky st 331"},
{ "name": "Susan", "address": "One way 98"},
{ "name": "Vicky", "address": "Yellow Garden 2"},
{ "name": "Ben", "address": "Park Lane 38"},
{ "name": "William", "address": "Central st 954"},
{ "name": "Chuck", "address": "Main Road 989"},
{ "name": "Viola", "address": "Sideway 1633"}
]
x=mycol.insert_many(mylist)
print(x.inserted_ids)'''
for x in mycol.find():
    print(x)