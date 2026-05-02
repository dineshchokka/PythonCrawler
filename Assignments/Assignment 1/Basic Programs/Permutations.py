from itertools import permutations

def permutate(string):
    permlist = permutations(string)
    for i in permlist:
        print(" ".join(i))

if __name__ == "__main__" :
    string1 = input("Enter the string : ")
    permutate(string1)