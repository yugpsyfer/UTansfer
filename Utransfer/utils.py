from pymongo import MongoClient


def get_user_db_handle(connection_string = ""):

 client = MongoClient(connection_string)
 db_handle = client['']
 
 return db_handle


def get_db_handle_secondary(connection_string = ""):

 client = MongoClient(connection_string)
 db_handle = client['']
 
 return db_handle