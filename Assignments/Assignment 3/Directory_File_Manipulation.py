import os
import random
import glob
from os import path

def TokenizeFileContent(List):
    Token_List = []
    for i in List:
        filepointer = open(i, 'r+')
        datalines = filepointer.readlines()
        for i in datalines:
            Token_List.extend(i.split(" "))

    Mod_Token_List = []
    for i in Token_List:
        if i == '\n':
            pass
        else:
            i = i.rstrip()
            Mod_Token_List.append(i)
    return Mod_Token_List

def EvenOddLength(Token_List):
    EvenList = []
    OddList = []
    for i in Token_List:
        if len(i) % 2 == 0:
            EvenList.append(i)
        else:
            OddList.append(i)
    return EvenList, OddList


def ReadTextFilesInDir():
    Text_Files = glob.glob('*.txt')
    return Text_Files


def Display(Token_List):
    for i in Token_List:
        if i == ' ' or i =='\n':
            pass
        else:
            print(i)

def main():

    FileName = input("Please enter the FileName : ")
    count = 0
    try:
        if (str(path.exists(FileName) and path.isfile(FileName))):
            source = str(FileName)
            sourcelist = []
            sourcelist = source.split(".")
            destination = sourcelist[0] + '_Old' + '.txt'
            os.rename(source, destination)

    except FileNotFoundError:
        print("File not found - So Creating the new file")

    except FileExistsError:
        count = random.randint(0,1000000)
        source = str(FileName)
        sourcelist = []
        sourcelist = source.split(".")
        destination = sourcelist[0] + '_Old' + str(count) + '.txt'
        os.rename(source, destination)

    filepointer = open(FileName, 'w+')
    TextFiles = ReadTextFilesInDir()
    Token_List = TokenizeFileContent(TextFiles)
    print("The Token List is as below : ")
    Display(Token_List)
    EvenList, OddList = EvenOddLength(Token_List)
    print("\n")
    print("The Even Token List is as below : ")
    Display(EvenList)
    print("\n")
    print("The Odd Token List is as below : ")
    Display(OddList)
    Modified_Data = " ".join(OddList)
    filepointer.write(Modified_Data)
    filepointer.close()


if __name__== "__main__":
   main()