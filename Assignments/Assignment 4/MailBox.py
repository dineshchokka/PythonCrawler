import re
hand = open('MailBox.txt', 'r')
split_list = []
for line in hand:
    line = line.rstrip()
    if re.search('^From', line):
        split_list = line.split(" ")
print(split_list)
mat = re.match(r'(.*)\.(.*)@(.*)', split_list[1])
print("The Name of the Mail sender is " + mat.group(1) +" " +  mat.group(2))
print(mat.groups())  #prints all the groups... each () is a group in re.match.



#re.search(pattern, string)
#re.match(pattern, string)
#re.findall(pattern, string)
#re.compile()

#re.match(pattern, string).groupdict()