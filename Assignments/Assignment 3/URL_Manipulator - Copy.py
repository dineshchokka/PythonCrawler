import urllib.request

req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
print(the_page)


def remove_html_tags(text):
   """Remove html tags from a string"""
   import re
   clean = re.compile('<.*?>')
   return re.sub(clean, '', text)
