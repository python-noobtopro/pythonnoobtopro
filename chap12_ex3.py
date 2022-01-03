'''
Chapter 12
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''

import urllib.request
count = 0
urlinp = input('Enter url:\n>>>')
document = urllib.request.urlopen(urlinp).read().decode()
print(document[:3001])
print('Length of characters received:',len(document[:3001]))
