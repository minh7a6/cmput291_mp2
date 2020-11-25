from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
# def createId(db):
#     empty = False
#     counter =1
#     while(empty == False):
#         if(db.Votes.find_one({"Id":str(counter)}) == None):
#             empty =True
#             break
#         counter = counter +1
#     return counter
#Function: vote
#args: db (291 database) , pid (post id), uid (user id)
#Description: allow users to vote on question / answer
def vote(db,pid,uid):
    print("Vote page")
    checkVote = False
    if uid != "":
        checkVote = db.Votes.find_one({"$and": [{"VoteTypeId":"2"},{"UserId": uid},{"PostId":pid}]}) == None # true if user has not voted on post
        #print(db.Votes.find_one({"$and": [{"VoteTypeId":"2"},{"UserId": uid},{"PostId":pid}]}) == None)
    if(checkVote == True  or uid ==""):
        today = str(datetime.datetime.now())
        today = today[:-3]
        today ='T'.join(today.split())
        vote = {}
        if(uid ==""):
            vote = {
            "PostId": pid,
            "VoteTypeId": "2",
            "CreationDate": today
        }
        else:
            vote = {
                "PostId": pid,
                "VoteTypeId": "2",
                "UserId": uid,
                "CreationDate": today
            }
        votesCollection = db["Votes"]
        x = votesCollection.insert_one(vote)
        newId = str(x.inserted_id)
        filter = {"_id": ObjectId(newId)}
        newvalues = { "$set": { 'Id': newId } } 
        votesCollection.update_one(filter, newvalues)
        #print(db.Votes.find_one({"$and": [{"Id":id}]}))
        #db.Votes.find_one({"Id":pid})
        score = db.Posts.find_one({"Id":pid})["Score"]+1
        #print(db.Posts.find_one({"Id":pid})["Score"])
        db.Posts.update({"Id":pid},{"$set":{"Score":score}})
        print("Success!")
        #print(db.Posts.find_one({"Id":pid}))
    else:
        print("You have already voted for this post")

if __name__ == "__main__":
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
    db = client["291db"]
    pid = "132"
    uid = "1"
    vote(db,pid,uid)