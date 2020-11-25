from pymongo import MongoClient
from bson.objectid import ObjectId


'''
disp_w_update(args, postColl)
The function is to update the post Column and display the post
'''
def disp_w_update(args, postColl):
    ans = postColl.find_one({"_id": ObjectId(args)})
    filter = {"_id": ObjectId(args)}
    cnt = ans["ViewCount"] + 1
    newvalues = { "$set": {'ViewCount': cnt} } 
    postColl.update_one(filter, newvalues)
    ans = postColl.find_one({"_id": ObjectId(args)})
    script = ""
    for j in ans:
        script += j + ": " + str(ans[j]) + "\r\n"
    print(script) 
    return ans["Id"]

'''
SearchQuestion(db)
The function is to search a question using the full text search from MongoDB
'''

def SearchQuestion(db):
    print("\r\n------------------------------------------------- Search Menu -------------------------------------------------\r\n")
    keyword_arr = input("Please enter your keywords for searching the Question: ")
    postColl = db["Posts"]
    print("Please wait...")
    x = postColl.find({"PostTypeId": "1", 
                        "$text": {"$search": str(keyword_arr), "$caseSensitive": False}}, 
                        {"_id": 1, "Id": 1, "Title": 1, "CreationDate": 1, "Score": 1, "AnswerCount": 1, 
                        "score": { "$meta": "textScore" }}).sort([("score", {"$meta": "textScore"})])
    y = list(x)
    temp_res = []

    print("{0} results found".format(len(y)))
    print("No || Title || Creation Date || Score || Ans Count")
    index = 1
    while len(y) > 0:
        if len(y) > 25:
            if len(y[index - 1:]) > 25:
                start = index - 1
                end = index - 1 + 25
                for i in y[start:end]:
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
                        choice = input("Please choose question {0} - {1}: ".format(1, index - 1))
                        if choice.isnumeric():
                            if int(choice) >= 1 and int(choice) < index:
                                return disp_w_update(temp_res[int(choice) - 1], postColl)
                            else:
                                print("Wrong Option")
                        else:
                            print("Wrong Option") 
            else:
                start = index
                for i in y[start - 1:]:
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
            for i in y:
                script = str(index) + " || " + str(i["Title"]) + " || " + i["CreationDate"]
                script += " || " + str(i["Score"]) + " || " + str(i["AnswerCount"])
                print(script)
                temp_res.append(i["_id"])
                index += 1
            while True:
                choice = input("Please choose question {0} - {1}: ".format(1, index - 1))
                if choice.isnumeric():
                    if int(choice) >= 1 and int(choice) < index:
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
    
if __name__ == "__main__":
    func_test()