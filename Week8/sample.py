import random
cnt = 10
num = []
isComplete = False
print(cnt)
while len(num) != cnt and not isComplete:
    ranNum = random.randint(0, cnt-1);
    if len(num) != cnt and ranNum not in num:
        num.append(ranNum)
        print("not complete", ranNum)
    elif len(num) == cnt:
        print("complete", ranNum)
        isComplete = True

print(sorted(num))