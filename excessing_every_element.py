import json

with open("QA_Pairs.json") as file:
    data = json.load(file)
    #Printing all the questions
    print("QUESTIONS")
    print("---------")
    for i in data:
        print(i["question"])
    
    #Printing all the answers
    print()
    print("ANSWERS:")
    print("-------")
    for i in data:
        print(i["answer"])
        
