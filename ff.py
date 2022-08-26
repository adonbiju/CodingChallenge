
def reciprocalString(word):
    ch = ''
    arr=[]
    for i in range(len(word)):
            ch = chr(ord('z') -
                     ord(word[i]) + ord('a'))
            arr.append(ch)
    print(arr)
    str1=''
    for ele in arr:
        str1 += ele
    print(str1)


# Driver Code
if __name__ == "__main__":
    s = "doselect"
    print("The reciprocal of", s, "is - ")
    reciprocalString(s)
