def PinCode(number):
    if number.isdigit():
        if len(number) == 6:
            return "True"
    return "False"

String = input("Please enter the pincode : ")

if PinCode(String) == "True":
    print(String,"is a Valid PinCode")
else:
    print(String,"is not a valid PinCode")