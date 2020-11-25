from pymongo import MongoClient
from bson.objectid import ObjectId
import re
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
    keyword_arr = input("Please enter your keywords for searching the Question (Please seperate them by space): ")
    keyword = keyword_arr.split(" ")
    postColl = db["Posts"]
    key = ""
    for i in keyword[:len(keyword) - 1]:
        key += i + "|"
    key += keyword[len(keyword) - 1]
    regex = key
    print(regex)
    x = postColl.find({"PostTypeId": "1", "$or": [{"Body": {"$regex": regex, "$options": "i"}}, {"Tags": {"$regex": regex, "$options": "i"}}, {"Title": {"$regex": regex, "$options": "i"}}]}, 
                        {"_id": 1, "Id": 1, "Title": 1, "CreationDate": 1, "Score": 1, "AnswerCount": 1})
    # regex = []
    # for i in keyword:
    #     regex.append(re.compile(i))
    # x = postColl.find({"PostTypeId": "1", "$or": [{"Body": {"$in": regex}}, {"Body": {"$in": regex}}, {"Body": {"$in": regex}}]}, 
    #                     {"_id": 1, "Id": 1, "Title": 1, "CreationDate": 1, "Score": 1, "AnswerCount": 1})
    y = list(x)
    temp_res = []
    print("Please wait...")
    print("{0} results found".format(len(y)))
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