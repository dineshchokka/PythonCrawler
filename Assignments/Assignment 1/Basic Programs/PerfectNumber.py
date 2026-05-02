def perfect(number):
    x = 1
    for i in range(2,number):
        if(number % i == 0):
            x += number//i
    if x == number:
        return 0

Num = int(input("Enter the Number :"))

if perfect(Num) == 0:
    print("The input is a perfect Number")
else :
    print("Not a perfect Number")