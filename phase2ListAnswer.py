import pymongo

def truncate(args):
    if len(args) > 80:
        return args[:80] + "..."
    else: 
        return args

def listAns(db, qid):
    postCol = db["Posts"]
    x = postCol.find_one({"Id": qid},{"AcceptedAnswerId": 1})
    print("No || Body || CreationDate || Score")
    index = 1
    id = str(x["AcceptedAnswerId"])
    list = []
    if id is not None:
        acceptedAns = postCol.find_one({"Id": id},{"Id": 1, "CreationDate": 1, "Score": 1, "Body": 1})
        script = str(index) + " || " + truncate(acceptedAns["Body"]) + " || " + acceptedAns["CreationDate"] + " || " + str(acceptedAns["Score"]) + " *"
        print(script)
        list.append(acceptedAns["Id"])
        index += 1
    x = postCol.find({"ParentId": qid, "PostTypeId": "2"},{"Id": 1, "CreationDate": 1, "Score": 1, "Body": 1})
    for i in x:
        if i["Id"] != id:
            script = str(index) + " || " + truncate(i["Body"]) + " || " + i["CreationDate"] + " || " + str(i["Score"])
            print(script)
            list.append(i["Id"])
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
                x = postCol.find_one({"Id": chosenId})
                for i in x:
                    print(i + ": " + str(x[i])) 
                return chosenId
        else:
            print("Wrong Option")

def func_test():
    url = "mongodb://localhost:50001"
    client = pymongo.MongoClient(url)
    print(listAns(client["291db"], "1"))
func_test()