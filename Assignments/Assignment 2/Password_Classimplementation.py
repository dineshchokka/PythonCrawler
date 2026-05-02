class Password:

    def __init__(self):
        return self

    def InputPassword(self):

        Password = input("Please enter the password : ")
        return Password

    def PasswordStrength(self,Password,list):

        lower, upper, special, digit, strength = 0, 0, 0, 0, 0
        Allowable_SpecialCharacters = ['@','!','#','$','&','*']

        for i in list:
            if Password == i or Password == i[::-1]:
                print("INVALID PASSWORD", end = '\n')
                exit()

        if len(Password) < 8:
            print("INVALID PASSWORD : Password is less than 8 digits", end='\n')
            exit()

        """ The Valid password Logic consists of the below Valid character logics:
        Should have atleast one lower case letter
        Should have atleast one Upper case letter
        Should have atleast one Numeric 
        Should have atleast one Special character
        Only the above are allowed, rest characters should not make up the password
        """

        # if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1
        #         and lower + special + upper + digit == len(Password)):
        #     print("This is a Valid Password")



        if (len(Password) >= 8):
            for character in Password:
                if (character.islower()):
                    lower += 1
                if (character.isupper()):
                    upper += 1
                if (character.isdigit()):
                    digit += 1
                if (character in Allowable_SpecialCharacters):
                    special += 1

        if (lower >= 1 and upper >= 1):
            strength += 1
        if (special >= 1):
            strength += 1
        if (digit >= 1):
            strength += 1

        print("This is a valid Password")

        if strength == 3:
            print("Password Strength:: STRONG")
        elif strength == 2:
            print("Password Strength :: MEDIUM")
        else:
            print("Password Strength :: WEAK")


        # if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1
        #         and lower + special + upper + digit == len(Password)):
        #     print("This is a Valid Password")
        #     print("The strength of the Password is STRONG")



list = []
with (open("Passwords.txt","r")) as file:
    data = file.read()
    for i in data.split():
        list.append(i)
file.close()
print(list)
PasswordObject = Password
Password = PasswordObject.InputPassword(PasswordObject)
PasswordObject.PasswordStrength(PasswordObject,Password,list)
