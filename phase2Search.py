from pymongo import MongoClient

def SearchQuestion(db):
    keyword_arr = input("Please enter your keywords for searching the Question: ")
    # keyword = keyword_arr.split(" ")
    postColl = db["Posts"]
    postColl.create_index(["", ])
    regexStr = 
    db.Posts.find({"PostTypeId": "1"}, {"Title": ""})
    print("No || Title || Creation Date || Score || Ans Count")


def func_test():
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
func_test()