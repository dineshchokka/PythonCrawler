def is_member(character,list1):
    for i in list1:
        if i == character:
            return "True"
    return "False"

list1 = input("Please enter the list of characters : ")
character = input("Please enter the character to be searched : ")

if is_member(character,list1) == "True":
    print ("The character",character," is part of the List")
else:
    print("The character",character," is not part of the List")