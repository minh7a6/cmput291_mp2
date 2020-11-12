from pymongo import MongoClient
from datetime import date
import pymongo
uid = "11" #change it later
url = "mongodb://localhost:" + str(50001)
client = MongoClient(url)
db = client["291db"]
print("\r\n------------------------------------------------Post Page------------------------------------------------")
title = input("PLease input a title: ")
body =  input("Please input the body:  ")
tags = input("Please input tags (please serpate each tag by a space): ")
tagsArray = tags.split(" ")
tagString = "<"+"><".join(tagsArray)+">"
postTypeId = 1
today = str(date.today())
Id = str(int(db.Posts.find_one(sort=[("Id",pymongo.DESCENDING)])['Id'])+1)
print(db.Posts.find_one(sort=[("Id",pymongo.DESCENDING)]))
question =  {
        "Id": Id,
        "PostTypeId": "1",
        "AcceptedAnswerId": "0",
        "CreationDate": today,
        "Score": 0,
        "ViewCount": 0,
        "Body": body,
        "OwnerUserId": uid,
        "LastEditorUserId": uid,
        "LastEditDate": today,
        "LastActivityDate":today,
        "Title": title,
        "Tags": tagString,
        "AnswerCount": 0,
        "CommentCount": 0,
        "FavoriteCount": 0,
        "ContentLicense": "CC BY-SA 2.5"
      }
postsCollection = db["Posts"]
postsCollection.insert_one(question)
print(db.Posts.find_one(sort=[("Id",pymongo.DESCENDING)]))



