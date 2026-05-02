def char_freq(string1):
    freq_dict = {}
    for i in string1:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict


String1 = input("Please enter the string:  ")
print(char_freq(String1))


