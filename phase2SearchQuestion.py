from pymongo import MongoClient
import re
def removeDuplicates(titleSearch):
    noDuplicate =[]
    for i in range(len(titleSearch)):
        if titleSearch[i] not in titleSearch[i+1:]:
            noDuplicate.append(titleSearch[i])
    return noDuplicate
url = "mongodb://localhost:" + str(50001)
client = MongoClient(url)
db = client["291db"]
searchText = input("Please enter keyword(s) to being searching (please seperate each one by a space)")
searchArray = searchText.split()
titleSearch=[]
for keyword in searchArray:
    rgx = re.compile('.*'+keyword+'.*', re.IGNORECASE)  # compile the regex
    titleSearch = titleSearch + list(db.Posts.find({"$and": [{"PostTypeId":"1"},{"Title": rgx}]})) + list(db.Posts.find({"$and": [{"PostTypeId":"1"},{"Body": rgx}]})) +list(db.Posts.find({"$and": [{"PostTypeId":"1"},{"Tags": rgx}]}))
titleSearch = removeDuplicates(titleSearch)
print("Title || Creation Date || Score || Answer Count")
for row in titleSearch:
    print(row["Title"]+" || "+row["CreationDate"]+" || "+str(row["Score"])
    #+ " || "+str(row["AnswerCount"]) + " || "+row["Body"]+" || "+row["Tags"]
    )