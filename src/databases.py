
from pymongo import MongoClient
default_mongodb_schema = {
    "Company":{
        "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "country", "city"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "city": {
                        "bsonType": "string",
                        "description": "must be an string and is required"
                    },
                    "country": {
                        "bsonType": "string",
                        "description": "must be an string and is required"
                    }
                }
            }
    },
    "Employee":{
        "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "age", "company"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "age": {
                        "bsonType": "number",
                        "description": "must be an number and is required"
                    },
                    "company": {
                        "bsonType": "objectId",
                        "description": "must be an objectId and is required"
                    }
                }
            }
    }
}
class MongoDB:
    def __init__(self, db_name = "10AcademyNetAnalysis", con_string = "mongodb://localhost:27017/", schemas = default_mongodb_schema) -> None:
        self.client = MongoClient(con_string)
        self.db = self.client[db_name]
        #create the collections in the database using the schema provided
        for coll_name, coll_validator in schemas.items():
            try:
                self.db.create_collection(coll_name)
            except Exception as e:
                print(e)
            self.db.command("collMod", coll_name, validator=coll_validator)

    def list_collections(self):
        return self.db.list_collection_names()
    
    def get_validation(self, collection_name: str) -> dict:
        self.check_if_collection_exist(collection_name)
        return self.db.get_collection(collection_name).options() # type: ignore
    
    def check_if_collection_exist(self, collection_name: str):
        if not self.list_collections().__contains__(collection_name):
            raise Exception(f"Collection, {collection_name} not found.")

    def insert_to_collection(self, collection_name, data):
        self.check_if_collection_exist(collection_name)
        collection = self.db[collection_name]
        return collection.insert_one(data)

    def insert_many_to_collection(self, collection_name, data):
        self.check_if_collection_exist(collection_name)
        result = self.db[collection_name].insert_many(data)
        return result.inserted_ids

    def find_all(self, collection_name):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find()

    def find(self, collection_name, key, value):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find({key: value})
    
    def find_by_id(self, collection_name, _id):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find

    def find_one(self, collection_name, key, value):
        self.check_if_collection_exist(collection_name)
        return self.db[collection_name].find_one({key: value})