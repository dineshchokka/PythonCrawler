
def isogram(word):
    '''
    ##### ISOGRAM function ########
    ##### This function takes word as input and finds the number of occurences of each character of the word in the word itself
    ##### and sends 1 as return if it is not an isogram'''
    for i in list(word):
        if word.count(i) > 1:
            return '1'
# print(isogram.__doc__)

string = input("Enter the word :  ")
if isogram(string) == '1':
    print(" The input string is not an isogram")
else:
    print("The input string is an isogram")
