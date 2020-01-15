import os
import env
import pymongo

# Notice that all python constants are written in CAPITAL LETTERS with
# underscores separating the words


# Using the os library to set a constant called MONGODB_URI by using
# the .getenv() method to read in the enviroment variable we just set
MONGO_URI = os.getenv('MONGO_URI')

# Set another constant and give t the value of our databse name
DBS_NAME = "myTestDB"

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
    print("5. Show all documnets")
    print("6. Exit")
    print("")
    option = input("Enter option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("")
        print("Error accessing database")
    if not doc:
        print("Error! No Results found.")
    
    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob,  
                'gender': gender, 'hair_color': hair_color, 
                'occupation': occupation, 'nationality': nationality}
            
    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    # Define a variable, which gets the results of our get_record() function. 
    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            # Check is if the key is not equal to ID. "_id" id the default key that is created by Mongo.
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()

    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            # Check is if the key is not equal to ID. "_id" id the default key that is created by Mongo.
            if k != "_id":
                # Want the value to appear in these square brackets so that we can see what the current value
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    # If nothing is input, reset the value to it's current value
                    update_doc[k] = v
        
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N? > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.delete_one(doc)
                print("Document deleted!")
            except:
                print("Document not deleted.")


def show_all():
    try:
        documents = coll.find()
    except:
        print("")
        print("Error accessing database")
    if not documents:
        print("Error! No Results found.")

    for doc in documents:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            show_all()
        elif option == "6":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGO_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()