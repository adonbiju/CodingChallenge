# enter a number 123
# sum of
# 3 +2 +1 += 6

n=int(input("enter a number"))
sum=0
print("sum of")
while n>0:
    digit=n%10
    print(digit,"+",end="")
    sum=sum+digit
    n=n//10

print("=",sum)

