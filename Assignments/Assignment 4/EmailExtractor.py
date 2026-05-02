import re
filename = "email.txt"
fp = open(filename, 'r+')
data = fp.read()
Email_List = re.findall('\S+@\S+', data)
print(Email_List)
