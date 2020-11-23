from pymongo import MongoClient
import datetime 
import pymongo
def createId(db):
  empty = False
  counter =1
  while(empty == False):
    if(db.Posts.find_one({"Id":str(counter)}) == None):
      empty =True
      break
    counter = counter +1
  return counter
def createIdTag(db):
  empty = False
  counter =1
  while(empty == False):
    if(db.Tags.find_one({"Id":str(counter)}) == None):
      empty =True
      break
    counter = counter +1
  return counter

def postQuestion(uid,db):
  #uid = "11" #change it later
  #url = "mongodb://localhost:" + str(50001)
  #client = MongoClient(url)
  #db = client["291db"]
  print("\r\n------------------------------------------------Post Page------------------------------------------------")
  title = input("PLease input a title: ")
  body =  input("Please input the body:  ")
  tags = input("Please input tags (please serpate each tag by a space): ")
  tagsArray = tags.split(" ")
  tagString = "<"+"><".join(tagsArray)+">"
  postTypeId = 1
  today = str(datetime.datetime.now())
  today = today[:-3]
  today ='T'.join(today.split())
  #Id = str(int(db.Posts.find_one(sort=[("Id",pymongo.DESCENDING)])['Id'])+1)
  Id = str(createId(db))
  #print("The id is" + Id)
  if uid =="":
    question =  {
          "Id": Id,
          "PostTypeId": "1",
          "AcceptedAnswerId": "0",
          "CreationDate": today,
          "Score": 0,
          "ViewCount": 0,
          "Body": body,
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
  else:
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
  postsCollection.insert(question)
  #print(db.Posts.find_one({"Id":str(Id)}))
  for tag in tagsArray:
    checkTag = db.Tags.find_one({"TagName":tag}) == None # true if tag does not exist
    print(db.Tags.find_one({"TagName":tag}))
    if(checkTag == True):
      tagId = createIdTag(db)
      tags={
        "Id": str(tagId),
        "TagName": tag,
        "Count": 1,
        "ExcerptPostId": "332392", #dont know wat to fill
        "WikiPostId": "332391" #dont know wat to fill
      }
      TagsCollection = db["Tags"]
      TagsCollection.insert(tags)
     # print("Inserted tag =: ")
      #print(db.Tags.find_one({"Id":str(tagId)}))
    else:
      count = db.Tags.find_one({"TagName":tag})["Count"]+1
      #print(count)
      db.Tags.update({"TagName":tag},{"$set":{"Count":count}})
      #print(db.Tags.find_one({"TagName":tag}))




