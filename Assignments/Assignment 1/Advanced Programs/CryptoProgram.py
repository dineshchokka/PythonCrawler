##### ROT13 Ciphering and Deciphering

dictionary = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r',
       'f':'s', 'g':'t', 'h':'u',  'i':'v', 'j':'w',
       'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b',
       'p':'c',  'q':'d', 'r':'e', 's':'f', 't':'g',
       'u':'h', 'v':'i', 'w':'j', 'x':'k',  'y':'l',
       'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
       'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V',
       'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F',
       'T':'G', 'U':'H', 'V':'I','W':'J', 'X':'K',
       'Y':'L', 'Z':'M'}


def encrypt(message):
    encrypted_string = ''
    for i in message:
        if  i.isalpha():
            i = dictionary[i]
        encrypted_string += i
    return encrypted_string

# The below logic is to fetch keys from values and then convert the string.
# def decrypt(message):
#     decrypted_string = ''
#     for i in message:
#         if  i.isalpha():
#             for key,value in dictionary.items():
#                 if value == i:
#                     i = key
#                     break
#         decrypted_string += i
#     return decrypted_string

string = input("Please enter the string to be converted : ")
print(" Converted string is :",encrypt(string))
# print(" Converted string is :",decrypt(string))