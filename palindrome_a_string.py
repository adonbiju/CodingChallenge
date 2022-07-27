string = str(input("enter a word"))

rev=string[::-1]

if rev == string:
    print(string+" is palindrome")
else:
    print(string + " not is palindrome")