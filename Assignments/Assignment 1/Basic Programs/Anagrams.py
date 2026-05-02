def anagram(word, list1):
    list2 = []
    for i in list1:
        if (sorted(i) == sorted(word)):
            list2.append(i)
    return list2


Word = str(input("Please enter the Word : "))
ListOfWords = input("Please enter the List of words separated by space : ")
ListOfWords1 = ListOfWords.split(" ")

anagramlist = anagram(Word,ListOfWords1)
print("The anagram list is", anagramlist)