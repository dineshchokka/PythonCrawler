import sys
import argparse
import urllib.request
import re

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('<Method>',  help='<0 : HTML Tag Extractor/1 : Tag Replacer>')
    args = parser.parse_args()

def HtmlTagExtractor(PageData):
    Tagger = re.compile('<.*?>')
    print(Tagger)

# def TagReplacer(PageData):
#     d



req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
   the_page = response.read()


if sys.argv[1] == 0:
    HtmlTagExtractor(the_page)

elif sys.argv[1] ==1:
    TagReplacer(the_page)



if __name__ == '__main__':
    arguments()
