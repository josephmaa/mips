def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def partition(arr, low, high):
    left = low
    right = high
    pivot = arr[low]
    while left < right:
        print(arr)
        while arr[right] > pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left < right:
            swap(arr, left, right)
    arr[low] = arr[right]
    arr[right] = pivot

    return right


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)


def main():
    arr = [8, 2, 7, 10, 5, 6, 3, 4, 9, 3, 1]
    quicksort(arr, 0, len(arr)-1)


if __name__ == '__main__':
    main()
