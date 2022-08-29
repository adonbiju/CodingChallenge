# Find the average of largest and smallest numbers in an unsorted integer array?
# Eg. [1, 4, 3, 2] => average = (1+4)/2 = 2.5[1, 4, 3, 4] => average = (1+4+4)/3 = 3

def average_of_largest_and_smallest(arr):
    largest_value=max(arr)
    smallest_value=min(arr)
    largest_value_count=0
    smallest_value_count=0
    for i in range(len(arr)):
        if arr[i]==largest_value:
            largest_value_count=largest_value_count+1
    for i in range(len(arr)):
        if arr[i] == smallest_value:
            smallest_value_count = smallest_value_count + 1
    avg=((largest_value_count*largest_value)+(smallest_value_count*smallest_value))/(smallest_value_count+largest_value_count)

    print("average of largest and smallest number is",avg)
n = int(input("enter the limit of  array ="))
arr = []
for i in range(n):
    array_element = int(input("enter the array element ="))
    arr.append(array_element)
print("array elements are")
print(arr)
average=average_of_largest_and_smallest(arr)


# enter the limit of  array =4
# enter the array element =1
# enter the array element =4
# enter the array element =3
# enter the array element =4
# array elements are
# [1, 4, 3, 4]
# average of largest and smallest number is 3.0