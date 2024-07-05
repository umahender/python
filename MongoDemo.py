import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())
mydb=myclient["cmrec"]
'''mydblist=myclient.list_database_names()
if "cmrec1" in mydblist:
    print("database is exists")
else:
    print("does'nt exists")
'''
mycol=mydb["csea"]
'''
mylist=mydb.list_collection_names()
if "csea" in mylist:
    print("is exists")
else:
    print("Does'nt exists")
'''
#mydict={"name":"mahender","Rollno":"158rapr5a4"}
mydict=[
    {"name":"mahender","Rollno":"158rapr5a4"},
{"name":"virat","Rollno":"158rapr5a4"},
{"name":"dhoni","Rollno":"158rapr5a4"},
{"name":"Rohith","Rollno":"158rapr5a4"}
]
#x=mycol.insert_one(mydict)
x=mycol.insert_many(mydict)