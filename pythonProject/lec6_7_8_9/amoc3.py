import json


with open('data.json', 'r') as f:
    res = json.load(f)

# print(res['cnt'])
# print(res['list'][0]['main']['feels_like'])

while isinstance(res, dict) or isinstance(res, list):

    if isinstance(res, dict):
        for each in res.keys():
            print(each)
        s = input("input s: ")
        print(res[s])
        res = res[s]
    elif isinstance(res, list):
        for each in res:
            print(each)
        n = int(input("input n: "))
        print(res[n])
        res = res[n]


# for each in res['person']['friends']
# print(res['person']["favoriteFruit"]:
#     print(each['name'])
# opt = input("შეიყანეთ სასურველი სიტყვა:")
# try:
#     print(res['person'][opt])
# except KeyError:
#     print('აღნიშნული მონაცემი არ არსებობს')