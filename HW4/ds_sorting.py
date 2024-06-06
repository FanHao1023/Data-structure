# Author: 林凡皓
# Date: 2024/5/11
# Purpose: Based on the rules of HW, choose three of the function below to implement.
#          All of the works are adjust the sorting algorithm teached in class, to make
#          improvement on the algorithm. 
#          The three sorting algorithm I chose was bubble_sort_biderection(), 
#          select_sort_stable(), quicksort_median().

from typing import Any

def bubble_sort_bidirection(a_list, descending=False):
    """
    Performs a bidirectional bubble sort on a given list. This sorting algorithm
    iterates over the list, comparing and swapping adjacent elements to sort them
    either in ascending or descending order. Unlike traditional bubble sort, which
    only passes through the list in one direction, this version alternates between
    forward and backward passes to potentially reduce sorting time.

    Parameters:
    a_list (list): The list to be sorted.
    descending (bool, optional): A flag indicating whether the list should be sorted
        in descending order. Defaults to False, sorting the list in ascending order.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    n = len(a_list)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if descending:
                if a_list[i] < a_list[i + 1]:  # Check for descending order
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    swapped = True
            else:
                if a_list[i] > a_list[i + 1]:  # Check for ascending order
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    swapped = True

        if not swapped:  # If no swap occurred, break the loop
            break

        swapped = False
        end -= 1

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if descending:
                if a_list[i] < a_list[i + 1]:  # Check for descending order
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    swapped = True
            else:
                if a_list[i] > a_list[i + 1]:  # Check for ascending order
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    swapped = True

        start += 1
        
            
def shell_sort_gap(a_list, gap_sequence=None, descending=False):
    """
    Performs Shell sort on a given list, an optimization over insertion sort by
    allowing the exchange of far apart elements. The function supports custom gap
    sequences and sorting in both ascending and descending order.

    Parameters:
    a_list (list): The list to be sorted.
    gap_sequence (list, optional): A custom sequence of gaps to use for sorting.
        If None, Shell's original sequence (halving the list size iteratively) is used.
        Defaults to None.
    descending (bool, optional): If set to True, sorts the list in descending order.
        Otherwise, sorts in ascending order. Defaults to False.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    pass
            
def select_sort_stable(a_list, key=0):
    """
    Performs a stable selection sort on a given list. If a key is provided,
    elements are compared based on the value of the key. The function may create a new
    sorted list and then copies the elements back to the original list to maintain stability.

    Parameters:
    a_list (list): The list to be sorted.
    key (function, optional): A function of one argument that is used to extract a
        comparison key from each list element.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    n = len(a_list)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if (a_list[j][key] < a_list[min_index][key]):
                min_index = j
        value = a_list[min_index]

        while (min_index > i) :
            a_list[min_index] = a_list[min_index-1]
            min_index -= 1

        a_list[i] = value


def merge_sort_noslice(a_list, start=0, end=None):
    """
    Performs a merge sort on a given list without using list slicing, to improve
    space efficiency. The function recursively divides the list into halves, sorts each half,
    and then merges them together in sorted order.

    Parameters:
    a_list (list): The list to be sorted.
    start (int, optional): The starting index of the sublist to sort. Defaults to 0.
    end (int, optional): The ending index of the sublist to sort. If None, the end
        of the list is used. Defaults to None.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    pass


#############################################################################################
#                     define function needed for quick_sort_median                          #
#############################################################################################

def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c

#A method to partition around the median
def partition_median(array, leftend, rightend):
    left = array[leftend]
    right = array[rightend-1]
    length = rightend - leftend

    if length % 2 == 0:
        middle = array[leftend + int(length/2 - 1)]
    else:
        middle = array[leftend + int(length/2)]
  
    pivot = median(left, right, middle)
    
    if pivot == left:
        pivotindex = leftend
    elif pivot == right:
        pivotindex = rightend-1
    else:
        if length % 2 == 0:
            pivotindex = leftend + int(length/2 - 1)
        else:
            pivotindex = leftend + int(length/2)
     
    # print(pivot)
    # pivotindex = array.index(pivot) #only works if all values in array unique
    # print(pivotindex)
    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    leftmark = leftend + 1
    rightmark = rightend-1
    done = False
    while not done:
        while leftmark <= rightmark and array[leftmark] <= pivot:
            leftmark += 1
        while leftmark <= rightmark and array[rightmark] >= pivot:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            array[leftmark], array[rightmark] = array[rightmark], array[leftmark]
    array[leftend], array[rightmark] = array[rightmark], array[leftend]

    return rightmark
    
def quicksort_median(array, leftindex, rightindex):
     if leftindex < rightindex:
         newpivotindex = partition_median(array, leftindex, rightindex)
         quicksort_median(array, leftindex, newpivotindex)
         quicksort_median(array, newpivotindex + 1, rightindex)

#############################################################################################
#                    end of defining fuction needed for quick_sort_median                   #
#############################################################################################

def quick_sort_median(a_list):
    """
    Implements the quick sort algorithm using the median-of-three method to choose
    the pivot. This method selects the median of the first, middle, and last elements
    of the list as the pivot to improve performance on sorted or nearly sorted lists.

    Parameters:
    a_list (list): The list to be sorted.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    quicksort_median(a_list, 0, len(a_list))
    


def quick_sort_limit(a_list, limit):
    """
    Performs quick sort on a given list with a threshold for switching to insertion
    sort for small sublists. This hybrid approach can improve performance by using
    insertion sort, which is faster on small lists, while still benefiting from
    quick sort's efficiency on larger lists.

    Parameters:
    a_list (list): The list to be sorted.
    limit (int): The threshold at which to switch from quick sort to insertion sort
        for sorting sublists.

    Returns:
    None: The function sorts the list in place and does not return a value.
    """
    pass
