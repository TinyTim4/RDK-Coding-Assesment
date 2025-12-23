
#I chose Merge Sort for my sorting algorithm
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    #Find the middle of the array to partition
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

#Merge the arrays back in a sorted manner
def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#Calculate the median of the array
def findMedian(arr):
    s = mergeSort(arr)
    l = len(s)
    if l % 2 == 0:
        return (s[l/2-1] + s[l/2])/2
    else:
        return s[int(l/2)]


arr = []
print("Enter numbers one by one to input it into the array. Type S when finished.")
while(True):
    x = input()
    if x == "S":
        break
    elif x.isnumeric():
        arr.append(x)
print(f"The array is {arr}.")
print(f"The median is {findMedian(arr)}.")