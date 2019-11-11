# Check if user input string is a palindrome

# get string from user
word = str(input("Enter a word: "))

# Two possible solutions

# Solution 1 (simple)
if (word == word[::-1]):
    print(f"SOLUTION 1\nThe word \"{word}\" is a palindrome")
else:
    print(f"SOLUTION 1\nThe word \"{word}\" is not a palindrome")

# Solution 2
#for x in range(0,len(user_input_word):
word_count = 0
for count, letter in enumerate(word,start=1):
    if(letter == word[len(word) -count]):
        word_count+=1
if (word_count == len(word)):
    print(f"SOLUTION 2\nThe word \"{word}\" is a palindrome")
else:
    print(f"SOLUTION 2\nThe word \"{word}\" is not a palindrome")
