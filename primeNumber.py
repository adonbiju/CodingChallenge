# Program to check if a number is prime or not
n=int(input("Enter a number"))
# define a flag variable
flag = False
if n==0 or n==1:
    flag=True
if n> 2:
    for i in range(2, n):
        if (n% i) == 0:
            flag = True
            break
# check if flag is True
if flag:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")