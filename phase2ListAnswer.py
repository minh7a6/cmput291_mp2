import pymongo
import time

'''
truncate(args)
checking if the args are longer than 80 characters
'''
def truncate(args):
    if len(args) > 80:
        return args[:80] + "..."
    else: 
        return args
'''
checkNone(args)
This function is to check if argument is a None type or not, returning the args if it is not none, "None" otherwise
'''
def checkNone(args):
    if args is None:
        return "None"
    else:
        return args


'''
listAns(db, qid)
This function is designed to list the answer post regarding to that qid.
'''
def listAns(db, qid):
    postCol = db["Posts"]
    x = postCol.find_one({"Id": qid},{"AcceptedAnswerId": 1, "_id": 0})
    print("Listing Answers....")
    print("No || Body || CreationDate || Score")
    index = 1
    list = []
    id = None
    if len(x) != 0:
        id = str(x["AcceptedAnswerId"])
        acceptedAns = postCol.find_one({"Id": id},{"Id": 1, "CreationDate": 1, "Score": 1, "Body": 1})
        script = str(index) + " || " + truncate(checkNone(acceptedAns["Body"])) + " || " + checkNone(acceptedAns["CreationDate"]) + " || " + str(checkNone(acceptedAns["Score"])) + " *"
        print(script)
        list.append(acceptedAns["_id"])
        index += 1
    x = postCol.find({"ParentId": qid, "PostTypeId": "2"},{"Id": 1, "CreationDate": 1, "Score": 1, "Body": 1})
    for i in x:
        if id != None:
            if i["Id"] != id:
                script = str(index) + " || " + truncate(i["Body"]) + " || " + i["CreationDate"] + " || " + str(i["Score"])
                print(script)
                list.append(i["_id"])
                index += 1
        else: 
            script = str(index) + " || " + truncate(i["Body"]) + " || " + i["CreationDate"] + " || " + str(i["Score"])
            print(script)
            list.append(i["_id"])
            index += 1
    if len(list) == 0:
        return print("There are no answer for this question")
    while True:
        opt = input("Please choose which answer you would like to do next(1-{0}): ".format(len(list)))
        if opt.isnumeric():
            if(int(opt) > len(list)):
                print("Wrong Option")
            else:
                chosenId = list[int(opt) - 1]
                x = postCol.find_one({"_id": chosenId})
                for i in x:
                    print(i + ": " + str(x[i]))
                return x["Id"]
        else:
            print("Wrong Option")

def func_test():
    url = "mongodb://localhost:50001"
    client = pymongo.MongoClient(url)
    print(listAns(client["291db"], "1"))
if __name__ == "__main__":
    func_test()


