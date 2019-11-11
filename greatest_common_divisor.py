# Greatest Common Divisor, 2 solutions

# Solution 1 (using inbuilt function from math module)
import math
first_int = int(input("Enter first positive whole number: "))
second_int = int(input("Enter second positive whole number: "))
gcd = math.gcd(first_int,second_int)
print("SOLUTION 1\nGreatest Common Divisor is",gcd)

# Solution 2
check_int = first_int if first_int < second_int else second_int
gcd2=1
while check_int>1:
    if first_int % check_int ==0 and second_int % check_int == 0:
        gcd2 = check_int
        break
    check_int -=1
print("SOLUTION 2\nGreatest Common Divisor is",gcd2)
