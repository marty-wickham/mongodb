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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        # e is the error message
        print("Could not be connected to MongoDB: %S") % e 

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try: 
        doc = coll.find({'first': first.lower(), 'last': last.lower()})
    except: 
        print("")
        print("Error accessing database")
    if not doc:
        print("Error! No Results found.")
    
    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter lat name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first.lower(), "last": last.lower, 'dob': dob, 'gender': gender, 'hair_color': hair_color, 
                'occupation': occupation, 'nationality': nationality}
            
    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")

    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def main_loop():
    # while True sets the loop to run forever
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
