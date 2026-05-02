def WordToLengthMapping(list1):
    list2 = []
    for i in list1:
        list2.append(len(str(i)))
    return list2

list1 = input("Enter the list of words : ").split(" ")
print("The Converted list is", WordToLengthMapping(list1))