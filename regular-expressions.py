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
print(match.group())


