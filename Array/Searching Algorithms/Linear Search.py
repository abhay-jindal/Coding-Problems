"""
LINEAR SEARCH ALGORITHM

https://www.geeksforgeeks.org/linear-search/

The linear search algorithm transverses an array and return the index when element is found.
Linear search is rarely used practically because other search algorithms such as the binary search 
algorithm and hash tables allow significantly faster-searching comparison to Linear search.

The time complexity of the above algorithm is O(n). 
"""

def linearSearch(array, searchElement):
   for i in range(len(array)):
      if array[i] == searchElement:
         return "Element found at {} index".format(i)
   return "Element cannot be found in array."

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
searchElement = int(input('Element to search: '))
print(linearSearch(array, searchElement))
