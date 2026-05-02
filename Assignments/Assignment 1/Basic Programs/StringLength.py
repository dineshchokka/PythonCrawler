def length(string):
    count = 0
    for i in string:
        count += 1
    return count

string1 = input("Please enter the string :  ")
print("The length of the string is : ", length(string1))