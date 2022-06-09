import json

with open('questions.json', 'r') as f:
    res = json.load(f)

print(type(res))
print(res['university'])
print(res['quiz']['sport']['q1']['question'])
print(res['quiz']['sport']['q1']['answer'])
print()

print(res['quiz']['maths']['q1']['question'])

for i in range(4):
    print(res['quiz']['maths']['q1']['options'][i])

ans = int(input("shemoitanet tqveni pasuxi: "))
k = int(res['quiz']['maths']['q1']['answer'])

if k == ans:
    print("sworia")
else:
    print("arasworia")
