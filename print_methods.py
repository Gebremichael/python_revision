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
