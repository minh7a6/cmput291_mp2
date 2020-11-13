import json
from pymongo import MongoClient
from tqdm import tqdm
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
    if "Posts" in collist:
        db.Posts.drop()
    if "Tags" in collist:
        db.Tags.drop()
    if "Votes" in collist:
        db.Votes.drop()
    for i in args[1:]:
        collection = None
        arg = i.split("/")
        if arg[-1] == "Posts.json":
            collection = db["Posts"]
        elif arg[-1] == "Tags.json":
            collection = db["Tags"]
        elif arg[-1] == "Votes.json":
            collection = db["Votes"]
        with open(i) as file: 
            file_data = json.load(file)
            i = "demo"
            j = "demo"
            for i in file_data:
                break
            for j in file_data[i]:
                break
            progress = 0
            if(len(file_data[i][j]) < 500000):
                collection.insert(file_data[i][j])
            else:
                while(progress < len(file_data[i][j])):
                    if(progress > len(file_data[i][j]) - 500000):
                        k = file_data[i][j][progress:]
                    else:
                        k = file_data[i][j][progress:progress + 500000]
                    collection.insert(k)
                    progress = progress + 500000
if __name__ == "__main__":
    phase1(sys.argv)