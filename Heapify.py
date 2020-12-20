def buildHeap(array, n):
    startIndex = n//2-1
    for i in range(startIndex, -1, -1):
        maxHeapify(array, i, n)
    return array

def maxHeapify(array, index, n):
    root = index
    lIndex = 2*index + 1
    rIndex = 2*index + 2
    if lIndex < n and array[lIndex] > array[root]:
        root = lIndex

    if rIndex < n and array[rIndex] > array[root]:
        root = rIndex

    if root != index:
        array[root], array[index] = array[index], array[root]
        maxHeapify(array, root)


if __name__ == "__main__":
    n = int(input('Number of elements for heap: '))
    array = list(map(int,input("\nEnter the elements to build an heap: ").strip().split()))[:n]
    print(buildHeap(array, n))
    



