def overlapping(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return "True"
    return "False"

list1 = input("Enter the First list : ").split(" ")
list2 = input("Enter the Second list : ").split(" ")

if overlapping(list1,list2) == "True":
    print("The input lists are overlapping")
else :
    print("The input lists are not overlapping")