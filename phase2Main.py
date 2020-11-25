from pymongo import MongoClient
from phase2Login import login
from phase2PostQuestion import postQuestion
from phase2Search import SearchQuestion
from phase2Answer import giveAns
from phase2ListAnswer import listAns
from phase2QuestionAnswerVote import vote
'''
AnswerScreen(aid, uid, db)
This is the answer post screen
'''
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

'''
Question(qid, uid, db)
This is the question post screen
'''
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

'''
main_menu()
This is the main menu screen
'''

def main_menu():
    port = input("Please input your port number, we will try to connect using 'mongodb://localhost:port': ")
    url = "mongodb://localhost:" + str(port)
    client = MongoClient(url)
    db = client["291db"]
    collection = db["Posts"]
    print("Please wait, we are indexing post for searching...")
    collection.create_index([("Body", "text"), ("Tags", "text"), ("Title","text")])
    uid = login(db)
    while True:
        print("-------------------------- Main Menu -------------------------- ")
        print("Hello! What would you like to do today?")
        print("1: Post a Question")
        print("2: Search for Question")
        print("3: Exit")
        choice = input("Please choose an option: ")
        if choice == "1":
            postQuestion(uid, db)
        elif choice == "2":
            qid = SearchQuestion(db)
            if qid is not None:
                QuestionScreen(qid, uid, db)
        elif choice == "3":
            break
        else:
            print("wrong Option")



if __name__ == "__main__":
    main_menu()