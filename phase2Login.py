from pymongo import MongoClient
# def printMenu():
#         print("1: Post a Question")
#         print("2: Search for a Post")

def login(db):
    Uid = input("Please input your userId, if you do not wish to do so just press enter ")
    #print(list(db.Posts.find({"OwnerUserId":Uid},{"PostTypeId": "1"})))
    if Uid !="":
        questionCount = len(list(db.Posts.find({"OwnerUserId":Uid},{"PostTypeId": "1"})))
        print("Number of questions "+ str(questionCount))
        cur = db.Posts.find({ "$and" : [ {"OwnerUserId":Uid}, { "PostTypeId": "1"} ] })
        #print(list(cur))
        cumScore =0
        for x in cur:
            cumScore = cumScore + int(x["Score"])
        if(questionCount == 0):
            print("Average Question Score: " + str(0))
        else:
            print("Average Question Score: " + str(cumScore/questionCount))
        answerCount = len(list(db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })))
        cur = db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })
        cumScore =0
        print("Number of Answer "+ str(answerCount))
        for x in cur:
            cumScore = cumScore + int(x["Score"])
        if questionCount == 0:
            print("Average Answer Score: " + str(0))
        else:
            print("Average Answer Score: " + str(cumScore/questionCount))
        votesCount = len(list(db.Votes.find({"UserId":Uid})))
        print("Number of votes registered for the user "+str(votesCount))
    return Uid

def func_test():
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
    print(login(client["291db"]))
# func_test()