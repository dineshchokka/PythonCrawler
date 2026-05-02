def elementwise_greater_than(mylist, threshold):
    elementlist = []
    for i in mylist:
        if int(i) > int(threshold):
            elementlist.append("True")
        else:
            elementlist.append("False")
    return(elementlist)
MyList = input("Enter the list of numbers separated by space : ")
MyList = MyList.split(" ")
threshold = int(input("Enter the threshold value : "))
print("Element wise greater than List : ", elementwise_greater_than(MyList,threshold))