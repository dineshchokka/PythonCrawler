def palindromePhrase(string1):
    string2 = ""
    for i in string1:
        if i.isalpha():
            string2 += i
    string3 = string2[::-1]
    if string2.lower() == string3.lower():
        return "True"
    else:
        return "False"

String1 = input("Please enter the phrase to be checked:  ")

if  palindromePhrase(String1) == "True":
    print("This is a Palindrome Phrase")
else:
    print("This is not a Palindrome Phrase")

