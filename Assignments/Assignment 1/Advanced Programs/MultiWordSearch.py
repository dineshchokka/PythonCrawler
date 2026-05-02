def MultiWordSearch(listofdocs,keywords):
    dictionary = {}
    list1 = []
    index = 0
    for m in keywords:
        for i in listofdocs:
            i = i.lower()
            print(i)
            list2 = i.split(" ")
            print(list2)
            for k in list2:
                string2 = ""
                for l in k:
                    if l.isalpha():
                        string2 += l
                print(string2)
                print(m)
            if str(m) == string2:
                list1.append(index)
            break
        index += 1
        dictionary[m] = list1
    return dictionary

list1 = input("Enter the list of Documents/Strings separated by a comma: ").split(" ")
keywords = input("Enter the list of Keywords : ").split(" ")
print(MultiWordSearch(list1,keywords))


