class TextProcessing:
    #list = []
    #text = " "

    def __init__(self,list):
        self.list = list


    def FirstSearchMatch(self,SearchPattern):
        text = SearchPattern
        match = 0
        for j in list:
            if text in j:
                match = 1
                print("The first Search pattern matched data in the File is : " + j)
                break
        if match == 0:
            print("No Such text in the file that matches the Search pattern")


    def ReplacePatternMatch(self,SearchPattern,ReplacePattern):
        text = SearchPattern
        ReplacedList = []
        ReplacedData = " "
        for j in list:
            if text in j:
                j = j.replace(SearchPattern,ReplacePattern)
                ReplacedList.append(j)
            else:
                ReplacedList.append(j)
        print("\n")
        print("File data post replacing the data : ", end="\n")
        print(ReplacedData.join(ReplacedList))


    def DuplicateStringRemoval(self):
        UniqueList = []
        UniqueString = " "
        for i in list:
            if i in UniqueList:
                pass
            else:
                UniqueList.append(i)
        print("\n")
        print("The File Data after eliminating Duplicate strings is as below : ", end= "\n")
        print(UniqueString.join(UniqueList))


    def CountOfCharacters(self,lineslist):
        linesCount = lineslist
        WordCount = 0
        CharCount = 0
        for i in list:
            WordCount += 1
            for j in i:
                CharCount += 1
        print("\n")
        print("Number of Lines/Words/Characters is as below : ", end= "\n")
        print("Number of Lines : " + str(linesCount))
        print("Number of Words : " + str(WordCount))
        print("Number of Characters : " + str(CharCount))


list = []
lineslist = []
with (open("TextFile.txt","r")) as file:
    data = file.read()
    lineslist = len(data.split('\n'))
    for i in data.split():
        list.append(i)

searchpattern = input("Enter the Search Pattern : ")
replacepattern = input("Enter the Replace Pattern : ")

obj = TextProcessing(list)
obj.FirstSearchMatch(searchpattern)
obj.DuplicateStringRemoval()
obj.CountOfCharacters(lineslist)
obj.ReplacePatternMatch(searchpattern,replacepattern)

file.close()
