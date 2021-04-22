# finds largest and smallest element in unsorted array in O(n) time complexity.

def findSmallLarge(array):
    n =  len(array)
    small, large = array[0], array[0]
    for i in range(1, n):
        if large < array[i]:
            large = array[i]
        if small > array[i]:
            small = array[i]
    print("Largest element in array is {} and smallest element is {}.".format(large, small))
                      
if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n]
    findSmallLarge(array)


