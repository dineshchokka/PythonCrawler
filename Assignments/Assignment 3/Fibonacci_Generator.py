def Generator(Max):

    Max_value = Max
    a = 0
    b = 1

    while a < Max_value:
        yield a
        a,b = b,b+a

def main():
    Max_number = int(input("Enter the Maximum number for Fib Series : "))
    myiterator = Generator(Max_number)
    for value in myiterator:
        print(value)

if __name__ == "__main__":
    main()













