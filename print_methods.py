# print function and data types

print(2)        # int

print(1.23)     # float

print(2 + 4j)   # complex

print(True)     # bool

print("Daniel") # string

print((1,2,3))  # tuple

print([1,2,3])  # list

print({'ab','cd','ef'}) # set

print({"name":"James Bond","age":45})   # dict

print(None)     # None constant - used to indicate absence of a value

name = "Daniel"
age = 29

print("My name is",name,"and I am",age,"years old") # print() is concatenating and inserting single space between arguments. Also calls str() on all arguments

print("Next year, I will be "+ str(age+1)) # must be a str to be concatenated

print('adc', 'def', sep='\n\t') # sep the arguments with newline and tab

print(*[name,'is', age, 'years old']) # (*)star operator lets print() handle type casting

print("title",end='\n\t * ')   #
print("sub 1",end='\n\t * ')   #
print("sub 2")    #

# ---- flush  If True, the stream is forcibly flushed. Default value: False
import time
num_seconds = 3
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...',flush=True)
        time.sleep(1)
    else:
        print('Go!')

# ---- file  messages go straight to it, defualt is sys.stdout
import io
file_obj = io.StringIO()
print("Using file ", file=file_obj)
print(file_obj.getvalue())

# ---- Pretty Printing
#   pprint() calls repr() instead of the usual str() for type casting, so that you may evaluate its output as Python code
from pprint import pprint
pprint('pretty print')

cities = {'USA': {'Texas': {'Dallas': ['Irving']}}}
pprint(cities, depth=3) # limit a deeply nested hierarchy

items = [1, 2, 3]
items.append(items)
pprint(items)   # unique identity of a self-referencing object
print(id(items))

# ---- Printing JSON
import json
data = {'firstname':'Daniel', 'lastname':'Gebremichael'}
plain = json.dumps(data)
pretty = json.dumps(data, indent=4, sort_keys=True)
print(plain)
print(pretty)

# ---- Printing with colour using ANSI escape codes
def esc(code):
    return f'\033[{code}m'
print(esc('31;1;4') + 'really' + esc(0) + ' important')

# ---- Spinning Wheel Animation
from itertools import cycle
from time import sleep

duration = 0
for frame in cycle(r'-\|/-\|/'):
    print('\r', frame,'preparing',frame, sep='\t', end='', flush=True)
    sleep(0.2)
    if duration >= 20:
        break
    else:
        duration= duration+1

# ---- Loading Animation
def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)
