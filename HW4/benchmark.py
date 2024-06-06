# Author: 林凡皓
# Date: 2024/5/11
# Purpose: Analysis benchmark of the sorting algorithm teached in class, and compare the time complexity result
#          discussed in class and the result of benchmark analysis.

from random import randint
from timeit import repeat
from typing import Callable, List
import sys
sys.path.append("../pythonds3/")
from pythonds3.sorting import *
import matplotlib.pyplot as plt
from ds_sorting import bubble_sort_bidirection, shell_sort_gap, select_sort_stable, merge_sort_noslice, quick_sort_median, quick_sort_limit

def run_sorting_algorithm(algorithm: Callable, array: List[int], *args, **kwargs):
    # Print message indicating which algorithm is starting its benchmark
    print(f"Running {algorithm.__name__} on array of size {len(array)}...")
    
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
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)
    print(f"Completed {algorithm.__name__}.")
    return min(times)


array_size_list = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

############################################################################################################################################
#                                                 Define Function to run Benchmark                                                         #
############################################################################################################################################

def Run_Benchmark(algorithm: Callable):
    time_sorted_list = []
    time_inverse_sorted_list = []
    time_random_list = []
    algorithm_name = algorithm.__name__

    for size in array_size_list:
        # initialize array
        sorted_array = sorted(range(size), reverse=False)
        inverse_sorted_array = sorted(range(size), reverse=True)
        random_array = [randint(0, 1000) for _ in range(size)]

        # check array intialization
        if (size == 10):
            print(sorted_array)
            print(inverse_sorted_array)
            print(random_array)

        # time for running on sorted array
        print('###################################################################################################################')
        print(f"sorting on array of size {size}")
        time_sorted = run_sorting_algorithm(algorithm, sorted_array)
        print(f"Time for sorting on a sorted array of size {size} using {algorithm_name} is {time_sorted} ")
        # time for running on inversed sorted array
        time_inverse_sorted = run_sorting_algorithm(algorithm, inverse_sorted_array) 
        print(f"Time for sorting on a inversed sorted array of size {size} using {algorithm_name} is {time_inverse_sorted} ")   
        # time for running on random array
        time_random = run_sorting_algorithm(algorithm, random_array)  
        print(f"Time for sorting on a random array of size {size} using {algorithm_name} is {time_random} ")

        time_sorted_list.append(time_sorted)
        time_inverse_sorted_list.append(time_inverse_sorted)
        time_random_list.append(time_random)
        print('###################################################################################################################\n\n')

    # visualize the result
    plt.subplot(1, 2, 1)
    plt.plot(array_size_list, time_sorted_list, label='time_sorted')
    plt.plot(array_size_list, time_inverse_sorted_list, label='time_inverse_sorted')
    plt.plot(array_size_list, time_random_list, label='time_random')
    plt.plot
    plt.title(f'Bench mark analysis of {algorithm_name}')
    plt.xlabel('Input array size')
    plt.ylabel('Time')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(array_size_list, time_sorted_list)
    plt.plot
    plt.title('Insight to benchmark of sorted array')
    plt.xlabel('Input array size')
    plt.ylabel('Time')
    
    plt.show() 


def Run_Benchmark_Quicksort(algorithm: Callable, type_array = 'random'):
    time_list = []
    algorithm_name = 'quick_sort_median'

    for size in array_size_list:
        # initialize array
        if (type_array == 'sorted'):
            array = sorted(range(size), reverse=False)
        elif (type_array == 'inverse_sorted'):
            array = sorted(range(size), reverse=True)
        elif (type_array == 'random'):
            array = [randint(0, 1000) for _ in range(size)]

        # time for running on sorted array
        print('###################################################################################################################')
        print(f"sorting on array of size {size}")
        sorting_time = run_sorting_algorithm(algorithm, array)
        print(f"Time for sorting on a {type_array} array of size {size} using {algorithm_name} is {sorting_time} ")
        
        time_list.append(sorting_time)
        
        print('###################################################################################################################\n\n')
    return time_list
    
############################################################################################################################################
#                                              Finish Define Function to run Benchmark                                                     #
############################################################################################################################################



############################################################################################################################################
#                                                 Run Benchmark on different algorithm                                                     #
############################################################################################################################################
# Run on algorithm once !

# Bubble sort
#Run_Benchmark(bubble_sort) 

# Shell sort
#Run_Benchmark(shell_sort)

# selection sort
#Run_Benchmark(select_sort)

# merge sort
#Run_Benchmark(merge_sort)

"""
# quick sort
#time_sorted_list = Run_Benchmark_Quicksort(quick_sort_median, 'sorted')
time_inverse_sorted_list = Run_Benchmark_Quicksort(quick_sort_median, 'inverse_sorted')
#time_random_list = Run_Benchmark_Quicksort(quick_sort_median, 'random')

# visualize the result of quick sort
#plt.plot(array_size_list, time_sorted_list, label='time_sorted')
plt.plot(array_size_list, time_inverse_sorted_list, label='time_inverse_sorted')
#plt.plot(array_size_list, time_random_list, label='time_random')
plt.plot
plt.title(f'Bench mark analysis of quick_sort_median')
plt.xlabel('Input array size')
plt.ylabel('Time')
plt.legend()

plt.show()
"""
############################################################################################################################################
#                                              Finish Runing Benchmark on different algorithm                                              #
############################################################################################################################################
