# Author: 林凡皓
# Date: 2024/3/2
# Purpose: 驗證Polynomial class中定義的加法、減法、乘法、取負號的功能正確性。

from Polynomial import Polynomial

# Create polynomial p1: x - 1
p1 = Polynomial([1, -1])
print("p1:", p1)

# Create polynomial p2: -2x^3 + x^2 - x
p2 = Polynomial([-2, 1, -1, 0])
print("p2:", p2)

# Create polynomial p3: x^4 - 6x - 1
p3 = Polynomial([0, 1, 0, 0, -6, -1])
print("p3:", p3)

# Create polynomial p4: 0.5
p4 = Polynomial([0.5])
print("p4:", p4)

p5 = -p2
print("p5  (-p2):", p5)

# Add p1 and p2
p6 = p1 + p2
print("p6  (p1 + p2):", p6)

p7 = p1 - p2
print("p7  (p1 - p2):", p7)

p8 = p1 * p2
print("p8  (p1 * p2):", p8)

p9 = p1 * p3
print("p9  (p1 * p3):", p9)

p10 = p6 - p3
print("p10 (p6 - p3):", p10)

p11 = p8 + p1
print("p11 (p8 + p1):", p11)

p12 = p9 * p4
print("p12 (p9 * p4):", p12)

p13 = p11 * p1
print("p13 (p11 * p1):", p13)

p14 = p12 + p4
print("p14 (p12 + p4):", p14)

p15 = - p4 + p5
print("p15 (-p4 + p5):", p15)


###### Below is my test code ######
print('###### My test ######')
x1 = Polynomial([0, 0, 0, 0, 1, 2])
x2 = Polynomial([0, 0, 0, 3, 4, 2])
x3 = Polynomial([0, 0, 0])
x4 = Polynomial([2, 4, -2])
x5 = Polynomial([0.33, 0.77, 0.0012])
print(f'x1 + x2 : {x1 + x2}')
print(f'x1 - x2 = {x1 - x2}')
print(f'x1 * x2 = {x1*x2}')
print(f'-x1 = {-x1}')
print(f'x1 + x3 = {x1 + x3}')
print(f'x1 - x3 = {x1 - x3}')
print(f'x1 * x3 = {x1*x3}')
print(f'-x3 = {-x3}')
print(f'x1 * x2 * x4 = {x1*x2*x4}')
print(f'x1 * x2 * (-x4) = {x1*x2*(-x4)}')
print(f'x1 + x5 : {x1 + x5}')
print(f'x1 - x5 = {x1 - x5}')
print(f'x1 * x5 = {x1*x5}')
print(f'-x5 = {-x5}')
print(f'x1 * x2 * x5 = {x1*x2*x5}')
print(f'x1 * x2 * (-x5) = {x1*x2*(-x5)}')
print(f'(x1 + x2) * (x2 + x4) = {(x1 + x2) * (x2 + x4)}')
