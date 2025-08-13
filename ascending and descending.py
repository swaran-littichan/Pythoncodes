def ascending_order(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
numbers=[30,1,20,12,54,5]
ascending_order(numbers)
print("ascending ordered numbers:",numbers)

def descending_order(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
numbers=[30,1,20,12,54,5]
descending_order(numbers)
print("descending ordered numbers:",numbers)