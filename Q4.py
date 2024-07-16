""" Design a function that determines whether a given string is a pangram. A 
pangram is a sentence or phrase containing every letter of the alphabet at 
least once. Punctuation and case are typically ignored. For example, the 
string "The quick brown fox jumps over the lazy dog" is a pangram, while 
"Hello, world!" is not.
"""
def check(str):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        else:
            return True
str = input("Enter a sentence ")
if (check(str) ==True):
    print("The entered sentence is pangram")
if (check(str) ==False):
    print("The entered sentence is not a pangram")
   