# check whether the given token number is valid or not if sum of last 2 digit of the token is 7 or 13. otherwise it is not a valid token
#example ===>75658
#5+8=12 so 75658 is a valid token

n=int(input("Enter a token Number:"))
token=n
arr=[]
while n>0:
    digit=n%10
    arr.append(digit)
    n=n//10
if arr[0]+arr[1]==7 or arr[0]+arr[1]==13:
    print(token, "is a valid token number")
else:
    print(token, "is not a valid token number")
# ========================OUTPUT========================
# Enter a token Number:75658
# 75658 is a valid token number