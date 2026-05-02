import re
filename = "input.txt"
match_elements = []
reg_exp = input("Please enter the regular expression : ")
reg = re.compile(reg_exp)
with open(filename) as filer:
    for i in filer:
        line = reg.findall(i)
        for j in line:
            if j :
                match_elements.append(j)
print(match_elements)
print("The number of matches in the Text are : ", len(match_elements))


