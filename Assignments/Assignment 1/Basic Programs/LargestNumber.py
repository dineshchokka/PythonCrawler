def max(a,b):
    if a > b:
        largest = a
    elif a == b:
        largest = 'NULL'
    else:
        largest = b
    return largest


x = int(input("enter the first number"))
y = int(input("enter the second number"))
# x,y = input().split()

if max(x,y) == 'NULL':
    print("Both the input numbers are equal")
else:
    print("The largest number of the two is", max(x,y))