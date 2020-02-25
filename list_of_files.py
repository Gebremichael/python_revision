import os
import glob

arr = os.listdir()
print(arr)

print('\n\n')

# Common files
pyfiles = []
for file in glob.glob("*.py"):
    pyfiles.append(file)
print(pyfiles)
