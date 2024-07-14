import cupy as cp

# Create a NumPy-like array on GPU
x_gpu = cp.array([1, 2, 3, 4, 5])

# Perform operations on GPU
result_gpu = cp.sqrt(x_gpu)

# Convert back to NumPy if needed
result_cpu = cp.asnumpy(result_gpu)

print(result_cpu)
