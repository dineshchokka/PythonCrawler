def SingleWordSearch(listofdocs,keyword):
    keyword = keyword.lower()
    dictionary = {}
    list1 = []
    index = 0
    for i in listofdocs:
        i = i.lower()
        list2 = i.split(" ")
        for k in list2:
            string2 = ""
            for l in k:
                if l.isalpha():
                    string2 += l
            if str(keyword) == string2:
                list1.append(index)
            break
        index += 1
    dictionary[keyword] = list1
    return dictionary

list1 = input("Enter the list of Documents/Strings: ").split(",")
keyword = input("Enter the Keyword: ")
print(SingleWordSearch(list1,keyword))


 