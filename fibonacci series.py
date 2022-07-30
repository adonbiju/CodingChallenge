limit=int(input("enter the limit"))
first=0
second=1
third=first+second
print("Fibonacci Series",first,second)
for i in range(3,limit+1,1):
    print(third)
    first=second
    second=third
    third=first+second