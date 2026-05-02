def LongestWord(list1):
    list2 = []
    for i in list1:
        list2.append(len(str(i)))
    list2.sort()
    return list2.pop()

list1 = input("Enter the list of words : ").split(" ")
print("The Longest Word is of length", LongestWord(list1))


##finding shortest word#
shortest = min(text.split(), key=len)
longest = max(text.split(), key=len)