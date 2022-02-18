Q1) Binary Search Iterative Method
def binary_search_iterative(lst, item):
    low, high = 0, len(lst) - 1 

    while low <= high:
        mid = (low+high) // 2 
        curr = lst[mid]
        if curr == item: 
            return(mid)
        elif curr > item:
            high = mid - 1
        elif curr < item:
            low = mid + 1
    return -1

-------------------------------------------------------------------------------------------------------------------------------------------------

Q2) Binary Search Iterative Modified - inserts item at the proper place and returns its index

def binary_search_iterative_modified(lst, item):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low+high) // 2 
        curr = lst[mid]
        if curr == item: 
            return(mid)
        elif curr > item:
            high = mid - 1
        elif curr < item:
            low = mid + 1
    lst.insert(low, item)
    return low

-------------------------------------------------------------------------------------------------------------------------------------------------

Q3) Binary Search Recursive

def binary_search_recursive(lst, item, low, high): 
    while low <= high:
        mid = (low+high) // 2 
        curr = lst[mid]
        if curr == item: 
            return(mid)
        elif curr > item:
            return binary_search_recursive(lst, item, low, mid - 1)
        elif curr < item:
            return binary_search_recursive(lst, item, mid + 1, high)
    return -1

-------------------------------------------------------------------------------------------------------------------------------------------------

Q4) Binary Search Recursive modified - inserts item at the proper place and returns its index 

def binary_search_recursive_modified(lst, item, low, high): 
    while low <= high:
        mid = (low+high) // 2 
        curr = lst[mid]
        if curr == item: 
            return(mid)
        elif curr > item:
            return binary_search_recursive_modified(lst, item, low, mid - 1)
        elif curr < item:
            return binary_search_recursive_modified(lst, item, mid + 1, high)
    lst.insert(low, item)
    return low

-------------------------------------------------------------------------------------------------------------------------------------------------

Q5) Update Student Records - takes tuples inside lists



-------------------------------------------------------------------------------------------------------------------------------------------------

Q6) Length of the line - Takes 3 two end points of a segment of a line in nested lists, and uses binary search to see if the lenght is present or not

def length_of_line(points_list, length):
    low, high = 0, len(points_list) - 1
    while low <= high:
        mid = (low + high) // 2
        point = points_list[mid]
        curr = round((((int(point[0][0]) - int(point[1][0]))**2 + (int(point[0][1]) - int(point[1][1]))**2)**0.5), 2)
        if curr == length:
            return mid
        elif curr > length:
            high = mid - 1
        elif curr < length:
            low = mid + 1
    return -1

-------------------------------------------------------------------------------------------------------------------------------------------------

Q7) Finding multiples - uses binary and linear approaches to return all index of the item in a list

def finding_multiple(lst, item):
    indices = []
    low, high = 0, len(lst) - 1 
    while low <= high:
        mid = (low+high) // 2 
        curr = lst[mid]
        if curr == item:
            # indices.append(mid) 
            while True:
                mid -= 1
                if mid < 0:
                    break
                else:
                    left_check = lst[mid]
                    if left_check == curr:
                        if mid not in indices:
                            indices.insert(0, mid)
                    else:
                        break
            while True:
                mid += 1
                if mid > len(lst) - 1:
                    break
                else:
                    right_check = lst[mid]
                    if right_check == curr:
                        if mid not in indices:
                            indices.append(mid)
                    else:
                        break
            return indices
        elif curr > item:
            high = mid - 1
        elif curr < item:
            low = mid + 1
    return []
