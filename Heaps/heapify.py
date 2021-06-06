def heapify(data):
    n = len(data)
    for i in reversed(range(n//2)):
        _max_heap(data, i)

def _max_heap(heap, pos):
    root = pos
    left_pos = 2*pos+1
    right_pos = left_pos+1
    n = len(heap)

    if left_pos < n and heap[left_pos] > heap[pos]:
        pos = left_pos

    if right_pos < n and heap[right_pos] > heap[pos]:
        pos = right_pos

    if pos != root:
        heap[pos], heap[root] = heap[root], heap[pos]
        _max_heap(heap, pos)

def _min_heap(heap, pos):
    root = pos
    left_pos = 2*pos+1
    right_pos = left_pos+1

    if left_pos < n and heap[pos] > heap[left_pos]:
        pos = left_pos

    if right_pos < n and heap[right_pos] < heap[pos]:
        pos = right_pos

    if pos != root:
        heap[pos], heap[root] = heap[root], heap[pos]
        _min_heap(heap, pos)

if __name__ == "__main__":
    n = int(input('Number of elements for heap: '))
    array = list(map(int,input("\nEnter the elements to build an heap: ").strip().split()))[:n]
    heapify(array)
