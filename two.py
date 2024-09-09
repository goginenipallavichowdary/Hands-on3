import time
import numpy as np
import matplotlib.pyplot as plt

def increment_function(size):
    total = 1
    for outer in range(1, size + 1):
        for inner in range(1, size + 1):
            total += 1
    return total

test_sizes = np.arange(1, 101)
execution_times = np.zeros_like(test_sizes, dtype=float)

for index, n in enumerate(test_sizes):
    start_time = time.time()
    increment_function(n)
    execution_times[index] = time.time() - start_time

plt.plot(test_sizes, execution_times, 'bo', label='Measured Times')

curve_coefficients = np.polyfit(test_sizes, execution_times, 2)
fitted_curve = np.polyval(curve_coefficients, test_sizes)
plt.plot(test_sizes, fitted_curve, 'r-', linewidth=2, label='Quadratic Fit')

plt.legend()
plt.xlabel('n (Size of Input)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. Input Size')
plt.show()
