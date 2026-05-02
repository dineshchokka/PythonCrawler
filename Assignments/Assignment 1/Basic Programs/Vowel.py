def is_vowel(ch):
    if ch in ['a','e','i','o','u']:
        return 'True'
    else:
        return 'False'

ch = input("Please enter the character :  ")
if is_vowel(ch) == 'True':
    print("Input character is a Vowel")
else:
    print("Input character is not a Vowel")