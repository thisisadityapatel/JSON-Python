import json

f = open("QA_Pairs.json")

data = json.load(f)

print(len(data))

f.close()