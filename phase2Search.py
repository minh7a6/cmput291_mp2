from pymongo import MongoClient

def SearchQuestion(db):
    keyword_arr = input("Please enter your keywords for searching the Question: ")
    # keyword = keyword_arr.split(" ")
    postColl = db["Posts"]
    x = db.Posts.find({"PostTypeId": "1", 
                        "$text": {"$search": keyword_arr, "$caseSensitive": False}}, 
                        {"_id": 1, "Id": 1, "Title": 1, "CreationDate": 1, "Score": 1, "AnswerCount": 1, "score": { "$meta": "textScore" }})
    x.sort([("score", { "$meta": "textScore" })])
    y = list(x)
    temp_res = []
    print("No || Title || Creation Date || Score || Ans Count")
    index = 1
    while True:
        if len(y) > 25:
            if len(y[index:]) > 25:
                for i in y[index:index+25]:
                    script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                    script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                    temp_res.append(i["Id"])
                    print(script)
                    index += 1
                cont = input("Do you want to fetch more (1:yes) ? ")
                if cont == "1":
                    pass
                else:
                    choice = input("Please choose question {0} - {1}:".format(index - 25, index))
            else:
                start = index
                for i in y[index:]:
                    script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                    script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                    print(script)
                    temp_res.append(i["Id"])
                    index += 1
                choice = input("Please choose question {0} - {1}:".format(start, index - 1))
        else:
            for i in x:
                script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                print(script)
                temp_res.append(i["Id"])
                index += 1
                choice = input("Please choose question 0 - {0}:".format(index))


def func_test():
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
    SearchQuestion(client["291db"])
func_test()