# from pymongo import MongoClient
import pymongo
import datetime
from bson.objectid import ObjectId
def giveAns(uid, db, qid):
    post = db["Posts"]
    print("\r\n----------------------------------------- Give Answer -----------------------------------------\r\n")
    body = input("What is the body of the answer?: ")
    if uid != "":
        Answer = {
            "PostTypeId": "2",
            "CreationDate": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
            "ContentLicense": "CC BY-SA 2.5",
            "Body": body,
            "Score": 0,
            "CommentCount": 0,
            "ParentId": str(qid),
            "OwnerUserId": str(uid),
        }
    else:
        Answer = {
            "PostTypeId": "2",
            "CreationDate": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
            "ContentLicense": "CC BY-SA 2.5",
            "Body": body,
            "Score": 0,
            "CommentCount": 0,
            "ParentId": str(qid),
        }
    # print(Answer)
    x = post.insert_one(Answer)
    newId = str(x.inserted_id)
    filter = {"_id": ObjectId(newId)}
    newvalues = { "$set": { 'Id': newId } } 
    post.update_one(filter, newvalues)
    print("Success!")
    print("\r\n-------------------------------------------------------------------------------------------\r\n")

def func_test():
    url = "mongodb://localhost:50001"
    client = pymongo.MongoClient(url)
    giveAns(None,client["291db"], "1")
    
if __name__ == "__main__":
    func_test()