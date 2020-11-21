from pymongo import MongoClient

def SearchQuestion(db):
    keyword_arr = input("Please enter your keywords for searching the Question: ")
    # keyword = keyword_arr.split(" ")
    postColl = db["Posts"]
    x = db.Posts.find({"PostTypeId": "1", "$text": {"$search": keyword_arr}}, {"_id": 0, "Title": 1, "CreationDate": 1, "Score": 1, "AnswerCount": 1})
    for i in x:
        print(i)
    print("No || Title || Creation Date || Score || Ans Count")


def func_test():
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
    SearchQuestion(client["291db"])
func_test()