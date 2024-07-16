"""Design a function that takes a string or sequence of characters as input and 
returns the character that appears most frequently.
//Eg 11189 => '1'
//hello => l"""
my_string = input("Enter a string: ")
my_counter = {}  

for letter in my_string:
    my_counter[letter] = my_counter.get(letter, 0) + 1 

max_frequency = max(my_counter.values())  
highest_frequency_chars = [char for char, count in my_counter.items() if count == max_frequency]

if highest_frequency_chars: 
    if len(highest_frequency_chars) == 1:
        print(f"Character: '{highest_frequency_chars[0]}' has the highest frequency of {max_frequency}")
    else:
        print(f"Characters: {' '.join(highest_frequency_chars)} have the highest frequency of {max_frequency} (tie)")
else:
    print("The string has no characters or all characters have the same frequency.")