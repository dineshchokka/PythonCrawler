class MyReverseList:

    def __init__(self,listElements):
        self.listElements = listElements
        self.a = 0
        self.a = len(listElements) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.a < 0:
            raise StopIteration
        else:
            value = listElements[self.a]
            self.a -= 1
            return(value)


listElements = []
stringElements = input("Enter the elements : ")
listElements = list(stringElements.split(" "))
ReverseList = MyReverseList(listElements)
for i in ReverseList:
    print(i)
