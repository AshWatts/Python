# Input
n = int(input("Enter number of Elements : "))
l = []
for i in range(n):
    ele = float(input("Element : "))
    l.append(ele)
print("Given List : ", l)


# Quick Sort using Functions

# Function to find the partition position
def partition(l, low, high):
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= pivot:
            i = i + 1
            (l[i], l[j]) = (l[j], l[i])

    (l[i + 1], l[high]) = (l[high], l[i + 1])
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


if __name__ == '__main__':

    # Function call
    quicksort(l, 0, n - 1)
    print('Quick Sorted List : ',l)