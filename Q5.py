"""Design a function that takes a list of integers as input. The function should 
return True if the list contains two consecutive threes (3 next to a 3) anywhere 
within the list. Otherwise, it should return False. For example, the function 
should return True for [1, 3, 3] and False for [1, 3, 1, 3]."""
def has_consecutive_threes(num_list):
  for i in range(len(num_list) - 1):
    if num_list[i] == 3 and num_list[i + 1] == 3:
      return True
  return False

def get_integer_list():
 
  while True:
    try:
      numbers_str = input("Enter a list of integers separated by spaces: ")
      num_list = [int(num) for num in numbers_str.split()]
      return num_list
    except ValueError:
      print("Invalid input. Please enter only integers separated by spaces.")

user_list = get_integer_list()

# Check for consecutive threes and print result
if has_consecutive_threes(user_list):
  print("The list contains two consecutive threes.")
else:
  print("The list does not contain two consecutive threes.")
