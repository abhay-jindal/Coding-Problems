"""
Time complexity is O(nk) as we have to iterate over elements once and for finding max 
time complexity is length of dict i.e. k
"""

def closestNumbers(array, number, k):
    n = len(array)

    # if range of numbers to return i.e. k is greater than the length of array itself then return array
    # as we already have required number of elements or less.
    if n < k:
        return array

    # further verions of python 3.6+ already have dicts in order i.e. as in the order the keys have been inserted in dictionary.
    # Using OrderedDict so that output array can be easily return in the order itself.
    from collections import OrderedDict 

    # OrderedDict comprehension where key is array index and value as difference to given number.
    data = OrderedDict((i, abs(array[i] - number)) for i in range(k)) 
    maximum =  max(data.values())
    for i in range(k, n):  # iterating over remaining elements of array
        diff = abs(array[i] - number)
        if diff < maximum:
            data.pop(max(data, key=data.get))  # get key of maximum value
            data[i] = diff
            maximum = max(data.values())
    return [array[i] for i in data.keys()]

if __name__ =="__main__":
    number = int(input("Enter the number to find closest numbers of: "))
    k = int(input("Enter the number of closest numbers to return: "))
    n = int(input('Number of elements in an array: '))
    array = list(map(int,input("\nEnter space separated elements: ").strip().split()))[:n] 
    # array = [22,15,13,11,9,8,4,2,1] 
    print(closestNumbers(array, number, k))
