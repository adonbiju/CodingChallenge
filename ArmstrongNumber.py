# Python program to check if the number is an Armstrong number or not for 3 digit

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while num > 0:
   digit = num % 10
   #print(digit)
   sum += digit ** 3
   num= num// 10
   #print(num)

# display the result
if temp == sum:
   print(temp,"is an Armstrong number")
else:
   print(temp,"is not an Armstrong number")