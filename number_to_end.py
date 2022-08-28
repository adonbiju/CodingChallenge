#Move all values equal to target to the end of the Array
def number_to_end(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        while i < j and arr[j] == target:
            j = j - 1
        if arr[i] == target:
            arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
    return arr

n = int(input("enter the limit of  array ="))
arr = []
for i in range(n):
    array_element = int(input("enter array element ="))
    arr.append(array_element)
print("array elements are")
print(arr)
target = int(input("enter a target ="))
new_arr = number_to_end(arr, target)
print("the array after sorted")
print(new_arr)
