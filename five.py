# Will this increate how long it takes the algorithm to run (e.x. you are timing the function like in #2)?

import time
import numpy as np
import matplotlib.pyplot as plt

def original_function(size):
    counter = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            counter += 1
    return counter

def modified_function(size):
    counter = 1
    sum_value = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            counter += 1
            sum_value = outer + inner
    return counter

input_sizes = np.arange(1, 10)
original_times = np.zeros_like(input_sizes, dtype=float)
modified_times = np.zeros_like(input_sizes, dtype=float)

for index, size in enumerate(input_sizes):
    start_time = time.time()
    original_function(size)
    original_times[index] = time.time() - start_time

    start_time = time.time()
    modified_function(size)
    modified_times[index] = time.time() - start_time

    print(f'Input Size = {size}: Original Time = {original_times[index]:.6f}s, Modified Time = {modified_times[index]:.6f}s')

plt.plot(input_sizes, original_times, 'bo', label='Original Function')
plt.plot(input_sizes, modified_times, 'go', label='Modified Function')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time: Original vs Modified Function')
plt.legend()
plt.show()


'''Input Size = 1: Original Time = 0.000007s, Modified Time = 0.000002s
Input Size = 2: Original Time = 0.000006s, Modified Time = 0.000004s
Input Size = 3: Original Time = 0.000005s, Modified Time = 0.000004s
Input Size = 4: Original Time = 0.000006s, Modified Time = 0.000005s
Input Size = 5: Original Time = 0.000007s, Modified Time = 0.000007s
Input Size = 6: Original Time = 0.000008s, Modified Time = 0.000009s
Input Size = 7: Original Time = 0.000009s, Modified Time = 0.000011s
Input Size = 8: Original Time = 0.000010s, Modified Time = 0.000013s
Input Size = 9: Original Time = 0.000013s, Modified Time = 0.000016s'''


