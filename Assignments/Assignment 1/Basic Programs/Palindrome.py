def is_palindrome(string):
    string1 = string[::-1]
    if string1 == string:
        return True
    else:
        return False


PalString = input("Enter the string : ")
if is_palindrome(PalString):
    print("The String is a palindrome")
else:
    print("The string is not a Palindrome")

