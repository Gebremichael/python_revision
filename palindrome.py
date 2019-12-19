# Check if user input is a palindrome

# get string from user
word = input("Enter a word: ")

# Two possible solutions

# Solution 1 (simple)
print("SOLUTION 1\nThe word",word,['is not','is'][word == word[::-1]] ,"a palindrome")

# Solution 2
# Compares the letters, first with last until it reachs the centre
word_count = 0
for count, letter in enumerate(word,start=1):
    if count > len(word)//2:
        break
    if(letter == word[len(word) -count]):
        word_count+=1

if (word_count == len(word)//2):
    print(f"SOLUTION 2\nThe word {word} is a palindrome")
else:
    print(f"SOLUTION 2\nThe word {word} is not a palindrome")
