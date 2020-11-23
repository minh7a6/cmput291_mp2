import json
from pymongo import MongoClient
import sys
from os import path
def phase1(args):
    if len(args) != 4:
        sys.exit("Need all 3 of the files")
    for i in args[1:]:
        if not path.isfile(i):
            ret = "{0} is not a file".format(i)
            sys.exit(ret)
    port = input("Please input your port number, we will try to connect using 'mongodb://localhost:port': ")
    url = "mongodb://localhost:" + str(port)
    client = MongoClient(url)
    db = client["291db"]
    collist = db.list_collection_names()
    for i in args[1:]:
        collection = None
        arg = i.split("/")
        if arg[-1] == "Posts.json":
            if "Posts" in collist:
                db.Posts.drop()
            collection = db["Posts"]
            print("Inserting to Posts...")
        elif arg[-1] == "Tags.json":
            if "Tags" in collist:
                db.Tags.drop()
            collection = db["Tags"]
            print("Inserting to Tags...")
        elif arg[-1] == "Votes.json":
            if "Votes" in collist:
                db.Votes.drop()
            collection = db["Votes"]
            print("Inserting to Votes...")
        with open(i) as file: 
            file_data = json.load(file)
            i = "demo"
            j = "demo"
            for i in file_data:
                break
            for j in file_data[i]:
                break
            collection.insert_many(file_data[i][j])
            if(collection == db["Posts"]):
                print("Text Indexing Post")
                collection.create_index([("Body", "text"), ("Tags", "text"), ("Title","text")])
if __name__ == "__main__":
    phase1(sys.argv)