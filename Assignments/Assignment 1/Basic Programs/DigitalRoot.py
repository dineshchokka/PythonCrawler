def digitalroot(number):
    sum = 0

    while(number > 0 or sum > 9):
        if (number == 0):
            number = sum
            sum = 0
        sum += number % 10
        number //= 10
    return sum

Num = int(input("Enter the Number :  "))
print(digitalroot(Num))