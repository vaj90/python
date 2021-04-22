list1 = ["allan", "john", "jorge", "juan", "teo"]
list2 = ["teo", "jake", "pia", "allan"]
for l1 in list1:
    for l2 in list2:
        if l1.upper() == l2.upper() or l1.lower() == l2.lower():
            print(l1)

