def quicksort(arr):
    sort(arr, 0, len(arr) - 1)

def sort(arr, low, high):
    if low >= high: return
    pivot = partition(arr, low, high)
    sort(arr, low, pivot - 1)
    sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = low
    left = pivot + 1
    right = high
    while left < right:
        while left < right and arr[left] < arr[pivot]:
            left += 1
        while left < right and arr[right] >= arr[pivot]:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    if arr[pivot] < arr[right]:
        arr[pivot], arr[right-1] = arr[right-1], arr[pivot]
        pivot = right - 1
    else:
        arr[pivot], arr[right] = arr[right], arr[pivot]
        pivot = right

    return pivot

arr = [1,4,2,3,5,4,6]
quicksort(arr)
print(arr)


