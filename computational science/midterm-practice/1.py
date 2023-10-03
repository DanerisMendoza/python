'''
    A palindromic number or numeral palindrome is a number that remains the 
    same when its digits are reversed.
    Examples: 121, 111, 10201, 16461, etc.
    Create a program that will accept integer input and check if the number is 
    Palindrome or not.
'''

input1 = str(int(input("input a integer: ")))
arr = []
for i in range(len(input1)-1,-1,-1):
    arr.append(input1[i])
result = ''.join(arr)
if(input1 == result):
    print("palindrome")
else:
    print("not palindrome")