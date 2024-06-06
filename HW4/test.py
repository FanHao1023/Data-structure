# Author: 林凡皓
# Date: 2024/5/11
# Purpose: Test if the sorting algorithm implemented in ds_sorting.py can work well.
#          Also check if the new algoithm can fix the problem of original algorithm.

import random
from timeit import repeat
import sys
sys.path.append("../pythonds3/")
from pythonds3.sorting import merge_sort, quick_sort, select_sort
from ds_sorting import bubble_sort_bidirection, shell_sort_gap, select_sort_stable, merge_sort_noslice, quick_sort_median, quick_sort_limit
from benchmark import run_sorting_algorithm
"""
# Refer to https://realpython.com/sorting-algorithms-python/#timing-your-code
def run_sorting_algorithm(algorithm, array, *args, **kwargs):
    # Convert all arguments into string representation
    args_repr = [repr(arg) for arg in args]  # Positional arguments
    kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]  # Keyword arguments
    all_args_repr = ", ".join(args_repr + kwargs_repr)  # Combine all argument representations

    # Prepare the setup code and statement for timeit
    setup_code = f"from __main__ import {algorithm.__name__}"
    
    if all_args_repr:  # Check if there are additional arguments
        stmt = f"{algorithm.__name__}({array}, {all_args_repr})"
    else:
        stmt = f"{algorithm.__name__}({array})"

    # Execute the code multiple times and return the minimum time in seconds
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=5)
    return min(times)
"""
    
   
# You can test the correctness and speed of your function here
# A-1 Test bubble_sort_bidirection
a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
a_list1 = a_list.copy()
a_list2 = a_list.copy()
bubble_sort_bidirection(a_list1)
bubble_sort_bidirection(a_list2, descending=True)

# checking the implementation of bubble_sort_bidirection
if (a_list1 == [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]):
    print("bubble_sort_bidirection ascending correct ! ")
else:
    print("bubble_sort_bidirection ascending failed !")

if (a_list2 == [110, 100, 90, 80, 70, 60, 50, 40, 30, 20]):
    print("bubble_sort_bidirection descending correct !")
else:
    print("bubble_sort_bidirection descending failed")


"""
# A-2 Test shell_sort_gap
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort_gap(a_list.copy(), gap_sequence=[5, 3, 1])
shell_sort_gap(a_list.copy(), gap_sequence=None)
shell_sort_gap(a_list.copy(), gap_sequence=None, descending=True)
"""


# B-1 Test select_sort_stable
items1 = [(5, 'A'),  (3, 'A'), (2, 'A'), (4, 'A'), (6, 'A'), (1, 'A'), (2, 'B')]
items2 = [(5, 'A'),  (3, 'A'), (2, 'A'), (4, 'A'), (6, 'A'), (1, 'A'), (2, 'B')]
items3 = [(5, 'A'),  (3, 'A'), (2, 'A'), (4, 'A'), (6, 'A'), (1, 'A'), (2, 'B')]
items4 = [(5, 'A'),  (3, 'A'), (2, 'A'), (4, 'A'), (6, 'A'), (1, 'A'), (2, 'B')]
print(f"Original list : {items1}\n")

select_sort_stable(items1, key=0)
select_sort_stable(items2, key=1)
select_sort(items3, key=0)
select_sort(items4, key=1)

print(f"Result of select_sort_stable")
print(f"key = 0 : {items1}")
print(f"key = 1 : {items2}\n")
print(f"Result of select_sort")
print(f"key = 0 : {items3}")
print(f"key = 1 : {items4}")

"""
# B-2 Test merge_sort_noslice
array = [random.randint(0, 200000) for _ in range(200000)]
time1 = run_sorting_algorithm(merge_sort, array)
time2 = run_sorting_algorithm(merge_sort_noslice, array)
"""

# C-1 Test quick_sort_median
array = [random.randint(0, 200000) for _ in range(50000)]
sorted_array = sorted(array)
# run_sorting_algorithm(quick_sort, sorted_array) # This may encounter error
time = run_sorting_algorithm(quick_sort_median, sorted_array)
print(f"Time for running quick_sort_median {time}")
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_median(a_list)
print(a_list)

"""
# C-2 Test quick_sort_limit
array = [random.randint(0, 200000) for _ in range(50000)]
sorted_array = sorted(array)
run_sorting_algorithm(quick_sort, sorted_array) # This may encounter erroe
run_sorting_algorithm(quick_sort_limit, sorted_array, 5000)
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_limit(a_list, 5)
"""
