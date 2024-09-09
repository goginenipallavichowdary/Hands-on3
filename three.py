import time
import numpy as np
import matplotlib.pyplot as plt

def nested_loops(input_size):
    total = 1
    for outer_loop in range(1, input_size + 1):
        for inner_loop in range(1, input_size + 1):
            total += 1
    return total

input_sizes = np.arange(1, 101)
execution_times = np.zeros_like(input_sizes, dtype=float)

for idx, size in enumerate(input_sizes):
    start_time = time.time()
    nested_loops(size)
    execution_times[idx] = time.time() - start_time

quadratic_coefficients = np.polyfit(input_sizes, execution_times, 2)
fitted_quadratic_curve = np.polyval(quadratic_coefficients, input_sizes)

cubic_coefficients = np.polyfit(input_sizes, execution_times, 3)
upper_bound_curve = np.polyval(cubic_coefficients, input_sizes)
upper_bound_expression = np.poly1d(cubic_coefficients)

linear_coefficients = np.polyfit(input_sizes, execution_times, 1)
lower_bound_curve = np.polyval(linear_coefficients, input_sizes)
lower_bound_expression = np.poly1d(linear_coefficients)

print("Fitted Quadratic Curve:", np.poly1d(quadratic_coefficients))
print("Upper Bound (Cubic Big-O):", upper_bound_expression)
print("Lower Bound (Linear Big-Omega):", lower_bound_expression)

plt.figure()
plt.plot(input_sizes, execution_times, 'bo', label='Measured Data')
plt.plot(input_sizes, fitted_quadratic_curve, 'r-', linewidth=2, label='Quadratic Fit')
plt.plot(input_sizes, upper_bound_curve, 'g--', linewidth=2, label='Cubic Upper Bound')
plt.plot(input_sizes, lower_bound_curve, 'm--', linewidth=2, label='Linear Lower Bound')
plt.legend()

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Input Size with Bounds')
plt.show()



'''Fitted Quadratic Curve:             2
-1.835e-08 x + 1.266e-05 x - 0.0001285
Upper Bound (Cubic Big-O):             3             2
-4.867e-10 x + 5.539e-08 x + 9.661e-06 x - 0.0001027
Lower Bound (Linear Big-Omega):  
1.08e-05 x - 9.702e-05'''
