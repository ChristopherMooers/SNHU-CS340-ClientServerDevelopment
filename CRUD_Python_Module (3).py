# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize MongoDB client connection
        self.client = MongoClient(
            f'mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin'
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            # Use try/except handling to return a bool if data is inserted
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except:
                return False
        else: 
            return False 

    # Create method to implement the R in CRUD.
    def read(self, query: dict)->list:
        if query is not None:
            # Use MongoDB's find() to search for matching documents
            # This returns a cursor (not a list yet)
            try:
                data = self.database.animals.find(query)
                # Convert the cursor into a list so it can be returned
                return list(data)
            except Exception as e:
                # Print error message if something goes wrong
                print("Read error: ", e)
                # If an error occurs return an empty list
                return []
            else:
                # If no query was provided, return an empty list
                return []
        
    # Create method to implement the U in CRUD.
    def update(self, query: dict, new_values: dict)->int:
        if query is not None and new_values is not None:
            # Perform the update using MongoDB's update_many() method
            # "$set" ensures only the specified fields are updated
            try:
                result = self.database.animals.update_many(query, {"$set": new_values})
                    
                # Return the number of documents that were actually modified
                return result.modified_count
            except Exception as e:
                # Print error message if something goes wrong
                print(f"Update error: {e}")
                return 0
            else:
                # Return 0 if input arguments are invalid
                return 0
        
    # Create method to implement the D in CRUD.
    def delete(self, query: dict)->int:
        if query is not None:
            # Delete all matching documents
            try:
                result = self.database.animals.delete_many(query)
                    
                # Return the number of documents that were actually deleted
                return result.deleted_count
            except Exception as e:
                # Print error message if something goes wrong
                print(f"Delete error: {e}")
                return 0
            else:
                # Return 0 if input arguments are invalid
                return 0