from pymongo import MongoClient
def printMenue():
        print("1: Post a Question")
        print("2: Search for a Post")

url = "mongodb://localhost:" + str(50001)
client = MongoClient(url)
db = client["291db"]
postsCollection = db["Posts"]
Uid = input("Please input your userId, if you do not wish to do so just press enter ")
if Uid !="":
    questionCount = len(list(db.Posts.find({"Id":Uid},{"PostTypeId": "1"})))
    print("Number of questions "+ str(questionCount))
    cur = db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "1"} ] })
    cumScore =0
    for x in cur:
        cumScore = cumScore + int(x["Score"])
    print("Average Question Score: " + str(cumScore/questionCount))
    answerCount = len(list(db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })))
    cur = db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })
    cumScore =0
    print("Number of Answer "+ str(answerCount))
    for x in cur:
        cumScore = cumScore + int(x["Score"])
    print("Average Answer Score: " + str(cumScore/questionCount))
    votesCount = len(list(db.Votes.find({"Id":Uid})))
    print("Number of votes registered for the user "+str(votesCount))
printMenue()
nextStep = input("Please select what you would like to do next: ")
#if nextStep == "1":
#if nextStep == "2":  