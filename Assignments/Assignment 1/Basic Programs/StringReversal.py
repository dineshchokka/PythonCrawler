def reverse(string1):
    string1 = string1[::-1]
    return string1

string = input("Please enter the string to be reversed : ")
print("The reversed string is :", reverse(string))




# Reversing a string
# Method1
#string1 = ''.join(reversed(string1))

# Method2
# string1 = "text"
# # w = ""
# # for i in string1:
# #     w = i + w
# # print(w)