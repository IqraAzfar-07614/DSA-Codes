Bubble Sort
#Works by repeatedly swapping adjacent elements if they are in the wrong order

A = [4, 12, 2, 1, 2, 73]
def bubble_sort(A):
    for i in range(len(A)): #going through length of list -> all elements
        for j in range(len(A)-i-1): #last i elements will already be in place 
            if A[j] > A[j+1]: 
                A[j], A[j+1] = A[j+1], A[j] #swaps if element is greater than the element next to it #python exclusive feature
                #x, y = A[j], A[j+1] #these lines for codes other than in python
                #A[j+1], A[j] = x, y
    return A

print(bubble_sort(A))

--------------------------------------------------------------------------------------------------

Selection Sort
#Repeatedly finds the minimum element (ascending order) and putting it at the beginning of the list

A = [6, 2, 2, 15, 9, 13]

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i #set minimum index to i for reference
        for j in range(i, len(A)): #checks from i till lenght A, as the previous iterations will be sorted already
            if A[min_idx] > A[j]: 
                min_idx = j #updates the minimum index if the new index element is smaller than the previous element
        A[i], A[min_idx] = A[min_idx], A[i] #swaps the new minimum element with the first element
    return A

print(selection_sort(A))

-------------------------------------------------------------------------------------------------

Insertion Sort
#Goes through the list and inserts the unsorted element at its suitable position in each iteration
#Like sorting cards, assume first card is sorted, then the unsorted card is compared and inserted accordingly

A = [6, 2, 2, 9, 15, 1] 

def insertion_sort(A):
    for i in range(len(A)): #goes through the whole list
        j = i
        while j > 0 and A[j] < A[j-1]: 
            A[j-1], A[j] = A[j], A[j-1] #if the predecessor is larger, then swaps with its place and continues to do so till element reaches its suitable position
            #x, y = A[j], A[j-1]
            #A[j-1], A[j] = x, y
            j -= 1 #reduces value of j by 1 for next iteration and check the elements before
    return A

print(insertion_sort(A))


-------------------------------------------------------------------------------------------------

Merge Sort
#Merge sort is a divide and conquer algorithm
#It divides the problem into two halves, and calls itself for the two halves, and it is repeated using recursion 
#Then when the division is done and the parts are sorted, they are then merged.
#Complexity is O(n*log(n))

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2 #mid of the list
        left, right = lst[:mid], lst[mid:] #dividing the list into two halves
        merge_sort(right), merge_sort(left) #sorting the two halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst

arr = [12, 11, 13, 5, 6, 7]

print(merge_sort(arr))
