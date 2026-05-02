def Word_freq(List):
    freq_dict = {}
    for i in List:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict


String1 = input("Please enter the List of words:")
List = String1.split(" ")
print(Word_freq(List))


