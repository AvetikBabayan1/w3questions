list1 = set(["FCB", "RMA", "ATM", "MNU"])
list2 = set(["MNC", "PSG", "JUV", "FCB"])

for l in list1:
    if l not in list2:
        print("element is in list 1 and not in list 2: ", l)

for m in list2:
    if m not in list1:
        print("element is in list 2 and not in list 1: ", m)

