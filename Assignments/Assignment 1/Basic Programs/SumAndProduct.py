def Sum(list1):
    sum1 = 0
    for i in list1:
        i = int(i)
        sum1 += i
    return sum1

def Product(list1):
    Mult1 = 1
    for i in list1:
        i = int(i)
        Mult1 *= i
    return Mult1

list1 = list(input("Enter the list of numbers: ").split())
print("The sum of the numbers is :" , Sum(list1))
print("The product of the numbers is :" , Product(list1))
