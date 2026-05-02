import re

def SpellingCorrector(string):
    t= re.sub('\s{2,}', ' ', S)
    t = re.sub(r"(\.)([A-Z])",r"\1 \2", t)
    return(t)

S =  input("Enter the String to be spell Checked : ")
print("The corrected string is : ",SpellingCorrector(S))