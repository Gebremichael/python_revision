# List/Array Manipulation
list1 = [2, 3, 4, 1, 32, 4, 32, 32]
print("\tlist1:",list1)
list1.append(19)
print("list1.append(19):",list1)

# Returns the count for 4 (the number of 4's in the list)
print("\nlist1.count(4):", list1.count(4) )

list2 = [99, 54]
# Append the elements of another list2 to an existing list1
print(f"\nBefore: list1- {list1}, list2- {list2}")
list1.extend(list2)
print("list1.extend(list2):", list1)

# Returns the index of the first occurrence of element x in the list.
print("\nlist1.index(4):", list1.index(4))

# Inserts an element x at a given index.
list1.insert(1,25)
print("\nlist1.insert(1,25):", list1) # insert 25 at position index 1

# --------pop(i)--------
# Removes the element at the given position and returns it. 
print("\nlist1.pop(2):", list1.pop(2) )
# >>> "Pop  3"      # position 2 (not same as index, as position starts from 1 and not 0) 

# --------pop()--------
# Removes and returns the last element
print("\nlist1.pop():", list1.pop())

# ----remove(x)------
print("\nBefore remove:",list1)
list1.remove(32)
print("First instance remove(32):",list1) # Remove number 32 (First instance (only) of element x is removed)

for x in list1:
    if x == 32:
        list1.remove(32)
print("For loop used to Remove all 32:", list1)
del list1[1:3]
print("\nAfter del list1[1:3]:",list1)

# --------reverse()--------
list1.reverse()
print("\nlist1.reverse():",list1) # Reverse the list

# ------sort()------
list1.sort()
print("\nlist1.sort():",list1) 

# -------copy()----
listcopy = list1.copy()
print("\nlist1.copy:",listcopy)

# ---------clear()---
listcopy.clear()
print("\nlistcopy.clear():",listcopy)
