# function returns the first duplicate value found, not helpful in case of multiple duplicates.
def findDuplicate(array):
    for i in range(1, len(array)):
        if array[i] ^ array[i-1]:
            continue
        else:
            return array[i]
    return -1

# finds largest and smallest element in unsorted array in O(log n) time complexity.
def findSmallLarge(array):
    small, large, start, end = float("inf"), 0, 0 , len(array)-1
    while start < end:
        if array[start] > array[end]:
            large = array[start] if array[start] > large else large
            small = array[end] if array[end] < small else small
        else:
            large = array[end] if array[end] > large else large
            small = array[start] if array[start] < small else small
        start += 1
        end -= 1
    if start == end:
        if array[end] > large:
            large = array[end]
        elif array[end] < small:
            small = array[end]
    print("Largest element in array is {} and smallest element is {}.".format(large, small))
                      
if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n]
    findSmallLarge(array)


