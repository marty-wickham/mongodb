import os
import env
import pymongo

# Notice that all python constants are written in CAPITAL LETTERS with underscores separating the words


# Using the os library to set a constant called MONGODB_URI by using the .getnenv() method to read in the enviroment variable we just set
MONGO_URI = os.getenv('MONGO_URI')  

# Set another constant and give t the value of our databse name
DBS_NAME =  "myTestDB" 

# The nameof our MongoDB collection
COLLECTION_NAME = "myFirstMDB" 

print("Your Mongo URI is " + str(MONGO_URI))


# Create our Mongo connect function
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        # e is the error message
        print("Could not connect to MongoDB: %s") % e

# This will call our mongo connection
conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]


# Return everything
"""
documents = coll.find()

# The line above will return an object that needs to be iterated through

for doc in documents:
    print(doc)
"""

# Insert a new record
"""
new_doc = {'first': 'Douglas', 'last': 'Adams', 'dob': '11/03/1952', 
            'gender': 'm', 'hair_color': 'gray', 'occupation': 'writer', 'nationality': 'english'}

coll.insert_one(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
"""

# Insert multiple records. Send in an array of dcitionaries
"""
new_docs = [{'first': 'Terry', 'last': 'Pratchett', 'dob': '28/04/1948', 
            'gender': 'm', 'hair_color': 'not much', 'occupation': 'writer', 'nationality': 'english'},     
            {'first': 'George', 'last': 'RR Martin', 'dob': '20/09/19948', 
            'gender': 'm', 'hair_color': 'white', 'occupation': 'writer', 'nationality': 'american'}]

coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)
"""

# Find specific data
"""
documents = coll.find({'first': 'Douglas'})

for doc in documents:
    print(doc)
"""

# Delete an entry
"""
coll.remove({'first': 'Douglas', 'last': 'Adams'})

documents = coll.find()

for doc in documents:
    print(doc)
"""

# Update an entry
"""
coll.update_one({'nationality': 'american'}, {'$set': {'hair_color': 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
"""

# Update many entries

coll.update_many({'nationality': 'american'}, {'$set': {'hair_color': 'silver'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
