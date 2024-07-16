"""Design a function that reverses the digits of an integer. For example, 50 
should become 5 and -12 should become -21."""
num = int(input("Enter the integer: "))  

def reverse_signed(num):
  sum = 0
  sign = 1
  if num < 0:
    sign = -1
    num = num * -1
  while num > 0:
    rem = num % 10
    sum = sum * 10 + rem
    num //= 10
  if not -2147483648 < sum < 2147483648:
    return 0  
  return sign * sum

reversed_num = reverse_signed(num)  
print("Reversed number:", reversed_num) 
                