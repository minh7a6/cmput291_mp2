from pymongo import MongoClient
from bson.objectid import ObjectId

def disp_w_update(args, postColl):
    ans = postColl.find_one({"_id": ObjectId(args)})
    filter = {"_id": ObjectId(args)}
    cnt = ans["ViewCount"] + 1
    newvalues = { "$set": {'ViewCount': cnt} } 
    postColl.update_one(filter, newvalues)
    script = ""
    for j in ans:
        script += j + ": " + str(ans[j]) + "\r\n"
    print(script) 
    return ans["Id"]

def SearchQuestion(db):
    keyword_arr = input("Please enter your keywords for searching the Question: ")
    postColl = db["Posts"]
    x = postColl.find({"PostTypeId": "1", 
                        "$text": {"$search": str(keyword_arr), "$caseSensitive": False}}, 
                        {"_id": 1, "Id": 1, "Title": 1, "CreationDate": 1, "Score": 1, "AnswerCount": 1, 
                        "score": { "$meta": "textScore" }}).sort([("score", {"$meta": "textScore"})])
    y = list(x)
    temp_res = []
    print("No || Title || Creation Date || Score || Ans Count")
    index = 1
    while len(y) > 0:
        if len(y) > 25:
            if len(y[index - 1:]) > 25:
                for i in y[index - 1:index - 1 +25]:
                    script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                    script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                    temp_res.append(i["_id"])
                    print(script)
                    index += 1
                cont = input("Do you want to fetch more (y:yes) ? ")
                if cont == "y":
                    pass
                else:
                    while True:
                        choice = input("Please choose question {0} - {1}: ".format(index - 25, index - 1))
                        if choice.isnumeric():
                            if int(choice) >= index - 25 and int(choice) < index:
                                return disp_w_update(temp_res[int(choice) - 1], postColl)
                            else:
                                print("Wrong Option")
                        else:
                            print("Wrong Option") 
            else:
                start = index
                for i in y[index - 1:]:
                    script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                    script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                    print(script)
                    temp_res.append(i["_id"])
                    index += 1
                while True:
                    choice = input("Please choose question {0} - {1}: ".format(start, index - 1))
                    if choice.isnumeric():
                        if int(choice) >= start and int(choice) < index:
                            return disp_w_update(temp_res[int(choice) - 1], postColl)
                        else:
                            print("Wrong Option")
                    else:
                        print("Wrong Option") 
                
        else:
            for i in x:
                script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                print(script)
                temp_res.append(i["_id"])
                index += 1
                while True:
                    choice = input("Please choose question {0} - {1}: ".format(0, index - 1))
                    if choice.isnumeric():
                        if int(choice) >= 0 and int(choice) < index:
                            return disp_w_update(temp_res[int(choice) - 1], postColl)
                        else:
                            print("Wrong Option")
                    else:
                        print("Wrong Option") 
    print("No question found")

def func_test():
    url = "mongodb://localhost:" + str(50001)
    client = MongoClient(url)
    print(SearchQuestion(client["291db"]))
func_test()