import json
from pymongo import MongoClient
import sys
def phase1(args):
    if len(args) < 4:
        sys.exit("Need all 3 of the files")
    port = input("Please input your port number, we will try to connect using 'mongodb://localhost:port': ")
    url = "mongodb://localhost:" + str(port)
    client = MongoClient(url)
    db = client["291db"]
    collist = db.list_collection_names()
    if "Posts" in collist:
        db.Posts.drop()
    if "Tags" in collist:
        db.Tags.drop()
    if "Votes" in collist:
        db.Votes.drop()
    for i in args[1:]:
        collection = None
        if i == "Posts.json":
            collection = db["Posts"]
        elif i == "Tags.json":
            collection = db["Tags"]
        elif i == "Votes.json":
            collection = db["Votes"]
        with open(i) as file: 
            file_data = json.load(file)
            i = "demo"
            j = "demo"
            for i in file_data:
                break
            for j in file_data[i]:
                break
            for k in file_data[i][j]:
                collection.insert_one(k)
if __name__ == "__main__":
    phase1(sys.argv)