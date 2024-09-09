import time
import numpy as np
import matplotlib.pyplot as plt

def nested_loop(input_size):
    count = 1
    for outer in range(1, input_size + 1):
        for inner in range(1, input_size + 1):
            count += 1
    return count

input_sizes = np.arange(1, 101)
execution_times = np.zeros_like(input_sizes, dtype=float)

for index, size in enumerate(input_sizes):
    start_time = time.time()
    nested_loop(size)
    execution_times[index] = time.time() - start_time

plt.plot(input_sizes, execution_times, 'bo', label='Measured Data')

quadratic_coeffs = np.polyfit(input_sizes, execution_times, 2)
quadratic_fit = np.polyval(quadratic_coeffs, input_sizes)

plt.plot(input_sizes, quadratic_fit, 'r-', linewidth=2, label='Quadratic Fit')

deviation_index = np.argmax(execution_times > quadratic_fit)

approx_deviation_input = input_sizes[deviation_index]
execution_time_at_deviation = execution_times[deviation_index]

print(f"Approximate Deviation Input (n_0): {approx_deviation_input}")
print(f"Execution Time at Deviation: {execution_time_at_deviation:.6f} seconds")

plt.axvline(x=approx_deviation_input, color='g', linestyle='--', label='Approx. n_0')

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Input Size with Deviation Point')
plt.legend()
plt.show()


'''Approximate Deviation Input (n_0): 1
Execution Time at Deviation: 0.000008 seconds'''
