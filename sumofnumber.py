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


# enter a number :4
# 1*1 + 2*2 +3*3 + 4*4
# 30
n=int(input("enter a number"))
sum=0
for i in range(0,n+1):
    sum=sum+(i*i)
print(sum)


n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    print(i,"*",i,end=")")
    sum=sum+(i*i)
    print("+",end="(")
print("=",sum)



arr=[6,4,5,7,3]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr),1):
        if arr[i]+arr[j]==10:
            print(arr[i],'+',arr[j],'= 10')

# arr=[6,4,5,7,3]
# 6 + 4 = 10
# 7 + 3 = 10