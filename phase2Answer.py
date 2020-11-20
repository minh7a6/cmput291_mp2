# from pymongo import MongoClient
import pymongo
import datetime


def giveAns(uid, db, qid):
    post = db["Posts"]
    x = post.find().sort([("Id", pymongo.DESCENDING)]).limit(1)
    Id = None
    for i in x:
       Id = i["Id"]
    newId = int(Id) + 1
    print(newId)
    body = input("What is the body of the answer?: ")
    Answer = {
        "Id": str(newId),
        "PostTypeId": "2",
        "CreationDate": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000"),
        "LastActivityDate": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000"),
        "ContentLicense": "CC BY-SA 2.5",
        "Body": body,
        "Score": 0,
        "CommentCount": 0,
        "ParentId": str(qid)
    }
    if uid is not None:
        Answer['OwnerUserId'] = str(uid)
    print(Answer)
    x = post.insert_one(Answer)
    print(x.inserted_id)


def func_test():
    url = "mongodb://localhost:50001"
    client = pymongo.MongoClient(url)
    giveAns(None,client["291db"], "1")
func_test()