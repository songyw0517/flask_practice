import pymongo

def connect_db_return_scof_col():
    mongo = pymongo.MongoClient("mongodb://localhost:27017/") # mongodb의 port의 기본값은 27017
    mongo_tutorial_db = mongo["mongo_tutorial"]
    scof_col = mongo_tutorial_db["scof"]
    '''
    for i in scof_col.find():
        print("scof_doc = ", i)
    print("MongoDB database list : ", mongo.list_database_names())
    '''
    return scof_col