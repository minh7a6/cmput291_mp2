from pymongo import MongoClient
from phase2Login import login
from phase2PostQuestion import postQuestion
from phase2Search import SearchQuestion
from phase2Answer import giveAns
from phase2ListAnswer import listAns
from phase2QuestionAnswerVote import vote

# def printMenue():
#         print("1: Post a Question")
#         print("2: Search for a Post")

# url = "mongodb://localhost:" + str(50001)
# client = MongoClient(url)
# db = client["291db"]
# postsCollection = db["Posts"]
# Uid = input("Please input your userId, if you do not wish to do so just press enter ")
# #print(list(db.Posts.find({"OwnerUserId":Uid},{"PostTypeId": "1"})))
# if Uid !="":
#     questionCount = len(list(db.Posts.find({"OwnerUserId":Uid},{"PostTypeId": "1"})))
#     print("Number of questions "+ str(questionCount))
#     cur = db.Posts.find({ "$and" : [ {"OwnerUserId":Uid}, { "PostTypeId": "1"} ] })
#     #print(list(cur))
#     cumScore =0
#     for x in cur:
#         cumScore = cumScore + int(x["Score"])
#     if(questionCount == 0):
#         print("Average Question Score: " + str(0))
#     else:
#         print("Average Question Score: " + str(cumScore/questionCount))
#     answerCount = len(list(db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })))
#     cur = db.Posts.find({ "$and" : [ {"Id":Uid}, { "PostTypeId": "2"} ] })
#     cumScore =0
#     print("Number of Answer "+ str(answerCount))
#     for x in cur:
#         cumScore = cumScore + int(x["Score"])
#     if questionCount == 0:
#         print("Average Answer Score: " + str(0))
#     else:
#         print("Average Answer Score: " + str(cumScore/questionCount))
#     votesCount = len(list(db.Votes.find({"UserId":Uid})))
#     print("Number of votes registered for the user "+str(votesCount))
# printMenue()
# nextStep = input("Please select what you would like to do next: ")
# if nextStep == "1":
#     postQuestion(Uid,db)
# #if nextStep == "2": 



def AnswerScreen(aid, uid, db):
    while True:
        print("-------------------------- Answer Screen -------------------------- ")
        print("What would you like to do with the answer?")
        print("1: Vote")
        print("2: Go Back to Question")
        choice = input("Please choose an option: ")
        if choice == "1":
            vote(db, aid, uid)
        elif choice == "2":
            break
        else:
            print("Wrong Option")
def QuestionScreen(qid, uid, db):
    while True:
        print("-------------------------- Question Screen -------------------------- ")
        print("What would you like to do with the question?")
        print("1: Answer")
        print("2: List Answer")
        print("3: Vote")
        print("4: Go Back")
        choice = input("Please choose an option: ")
        if choice == "1":
            giveAns(uid, db, qid)
        elif choice == "2":
            aid = listAns(db, qid)
            if aid is not None:
                AnswerScreen(aid, uid, db)
        elif choice == "3":
            vote(db, qid, uid)
        elif choice == "4":
            break
        else: 
            print("Wrong option")



def main_menu():
    port = input("Please input your port number, we will try to connect using 'mongodb://localhost:port': ")
    url = "mongodb://localhost:" + str(port)
    client = MongoClient(url)
    db = client["291db"]
    uid = login(db)
    while True:
        print("-------------------------- Main Menu -------------------------- ")
        print("Hello! What would you like to do today?")
        print("1: Post a Question")
        print("2: Seach for Question")
        print("3: Exit")
        choice = input("Please choose an option: ")
        if choice == "1":
            postQuestion(uid, db)
        elif choice == "2":
            qid = SearchQuestion(db)
            QuestionScreen(qid, uid, db)
        elif choice == "3":
            break
        else:
            print("wrong Option")



if __name__ == "__main__":
    main_menu()