# Author: 林凡皓
# Date: 2024/3/6
# Purpose: 透過timeit來驗證Big O分析的結果。

import time
from timeit import Timer
from Polynomial import Polynomial
import matplotlib.pyplot as plt 

#####################################################################################################
# benchmark for __init__
print(f"************************************************")
print(f"************************************************")
print(f"Benchmark for __init__")

initialize = Timer("Polynomial(coefficient)", "from __main__ import Polynomial, coefficient")
print(f"{'n':10s}{'Polynomial()':>15s}")

coefficient = list(range(5))
time_list_init = []    # for visualization
for i in range(0, 10000, 1000):
    coefficient.insert(0, 0)  
    initialize_t = initialize.timeit(number=1000)
    print(f"{i:<10d}{initialize_t:>15.5f}")
    time_list_init.append(initialize_t)    # for visualization

print(f"************************************************")
print(f"************************************************")

"""
# visualize the result
plt.plot(range(0, 10000, 1000), time_list_init)
plt.xlabel('zero added')
plt.ylabel('time')
plt.show()
"""
#######################################################################################################



#######################################################################################################
print("   ")
print("   ")

# benchmark for __add__
print(f"************************************************")
print(f"************************************************")
print(f"Benchmark for __add__")

add = Timer("a + b", "from __main__ import Polynomial, a, b")
print(f"{'n':10s}{'a + b':>15s}")

# fixed lenght of a
print(f"fixed length of a")
time_list_add_a = []    # for visualization
for i in range(1000, 10001, 1000):
    a = Polynomial(list(range(5)))
    b = Polynomial(list(range(i)))  
    add_t = add.timeit(number=1000)
    print(f"{i:<10d}{add_t:>15.5f}")
    time_list_add_a.append(add_t)    # for visualization

print(f"************************************************")
print(f"fixed length of b")
# fixed lenght of b
time_list_add_b = []    # for visualization
for i in range(1000, 10001, 1000):
    b = Polynomial(list(range(5)))
    a = Polynomial(list(range(i)))  
    add_t = add.timeit(number=1000)
    print(f"{i:<10d}{add_t:>15.5f}")
    time_list_add_b.append(add_t)    # for visualization
print(f"************************************************")
print(f"************************************************")

"""
# visualize the result 
plt.subplot(121)
plt.plot(range(1000, 10001, 1000), time_list_add_a)
plt.title('time analysis of a + b, with len(a) fixed')
plt.xlabel('length of b')
plt.ylabel('time')

plt.subplot(122)
plt.plot(range(1000, 10001, 1000), time_list_add_b)
plt.title('time analysis of a + b, with len(b) fixed')
plt.xlabel('length of a')
plt.ylabel('time')

plt.show()
"""
#######################################################################################################



#######################################################################################################
print("   ")
print("   ")

# benchmark for __sub__
print(f"************************************************")
print(f"************************************************")
print(f"Benchmark for __sub__")

sub = Timer("a - b", "from __main__ import Polynomial, a, b")
print(f"{'n':10s}{'a - b':>15s}")

# fixed lenght of a
print(f"fixed length of a")
time_list_sub_a = []    # for visualization
for i in range(1000, 10001, 1000):
    a = Polynomial(list(range(5)))
    b = Polynomial(list(range(i)))  
    sub_t = sub.timeit(number=1000)
    print(f"{i:<10d}{sub_t:>15.5f}")
    time_list_sub_a.append(sub_t)    # for visualization

print(f"************************************************")
print(f"fixed length of b")
# fixed lenght of b
time_list_sub_b = []    # for visualization
for i in range(1000, 10001, 1000):
    b = Polynomial(list(range(5)))
    a = Polynomial(list(range(i)))  
    sub_t = sub.timeit(number=1000)
    print(f"{i:<10d}{sub_t:>15.5f}")
    time_list_sub_b.append(sub_t)    # for visualization
print(f"************************************************")
print(f"************************************************")

"""
# visualize the result 
plt.subplot(121)
plt.plot(range(1000, 10001, 1000), time_list_sub_a)
plt.title('time analysis of a - b, with len(a) fixed')
plt.xlabel('length of b')
plt.ylabel('time')

plt.subplot(122)
plt.plot(range(1000, 10001, 1000), time_list_sub_b)
plt.title('time analysis of a - b, with len(b) fixed')
plt.xlabel('length of a')
plt.ylabel('time')

plt.show()
"""
#######################################################################################################



#####################################################################################################
print("   ")
print("   ")

# benchmark for __mul__
print(f"************************************************")
print(f"************************************************")
print(f"Benchmark for __mul__")

mul = Timer("a*b", "from __main__ import Polynomial, a, b")
print(f"{'n, k':10s}{'a * b':>15s}")

time_list_mul = []    # for visualization
for i in range(10, 501, 50):
    b = Polynomial(list(range(i)))
    a = Polynomial(list(range(i)))  
    mul_t = mul.timeit(number=1000)
    print(f"{i:<10d}{mul_t:>15.5f}")
    time_list_mul.append(mul_t)

print(f"************************************************")
print(f"************************************************")

"""
# visualize the result
plt.plot(range(10, 501, 50), time_list_mul)
plt.title('time analysis of a * b')
plt.xlabel('lenght of a, b')
plt.ylabel('time')
plt.show()
"""
#######################################################################################################



#####################################################################################################
print("   ")
print("   ")

# benchmark for __neg__
print(f"************************************************")
print(f"************************************************")
print(f"Benchmark for __neg__")

neg = Timer("-a", "from __main__ import Polynomial, a")
print(f"{'n':10s}{'-a':>15s}")

time_list_neg = []    # for visualization
for i in range(100, 1001, 100): 
    a = Polynomial(list(range(i)))
    neg_t = neg.timeit(number=1000)
    print(f"{i:<10d}{neg_t:>15.5f}")
    time_list_neg.append(neg_t)    # for visualization

print(f"************************************************")
print(f"************************************************")

"""
# visualize the result
plt.plot(range(100, 1001, 100), time_list_neg)
plt.title('time analysis of -a')
plt.xlabel('length of a')
plt.ylabel('time')
plt.show()
"""
#######################################################################################################