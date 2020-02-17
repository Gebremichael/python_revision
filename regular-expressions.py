import re

sentence = 'this is an example'
match = re.search(r'exam\w\w',sentence)
if match:
    ## On success, match.group() is matched text.
    print('found word: ',match.group())
else:
    print('did not find')

# . = any char but \n
# \d = digit char 
# \w = word char

# g+ = one or more g's, as many as possible
# \s* = zero or more whitespace chars
# ^ = matches the start of string

match = re.search(r'^y\w\s*\d.', 'yu   56t')
if match:
    print(match.group())

# Sqaure Brackets and Group Extraction
example1 = 'tower daniel-g@google.com house'
match = re.search('([\w.-]+)@([\w.-]+)', example1)
if match:
    print(match.group())   # whole match
    print(match.group(1))  # the username, group 1
    print(match.group(2))  # the host, group 2

# Findall
example2 = 'Daniel@gmail.com Mark@cheese.com John@paint.ie'
emails = re.findall(r'[\w\.-]+@[\w\.-]+',example2)
for email in emails:
        print(email)
