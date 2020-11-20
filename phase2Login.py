from pymongo import MongoClient
# def printMenu():
#         print("1: Post a Question")
#         print("2: Search for a Post")

def login(db):
    Uid = input("Please input your userId, if you do not wish to do so just press enter: ")
    if Uid !="":
        choice = input("Would you like a report for your session today (1:yes)?: ")
        if choice == "1":
            postsCollection = db["Posts"]
            questionCount = len(list(postsCollection.find({"OwnerUserId":Uid},{"PostTypeId": "1"})))
            print("Number of Questions: "+ str(questionCount))
            cur = postsCollection.find({ "$and" : [ {"OwnerUserId":Uid}, { "PostTypeId": "1"} ] })
            cumScore = 0
            for x in cur:
                cumScore = cumScore + int(x["Score"])
            print("Average Question Score: " + str(cumScore/questionCount))
            answerCount = len(list(postsCollection.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })))
            cur = db.Posts.find({ "$and" : [ {"OwnerUserId":Uid}, { "PostTypeId": "2"} ] })
            cumScore =0
            print("Number of Answers: "+ str(answerCount))
            for x in cur:
                cumScore = cumScore + int(x["Score"])
            print("Average Answer Score: " + str(cumScore/questionCount))
            votesCount = len(list(db.Votes.find({"Id":Uid})))
            print("Number of Votes registered for the user: " + str(votesCount))
    return Uid

def func_test():
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
    print(login(client["291db"]))
func_test()