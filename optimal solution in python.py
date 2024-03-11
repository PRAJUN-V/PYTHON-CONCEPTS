# Here are two simple Python programs to find the sum of numbers up to 1 billion.
# The first code utilizes the built-in `sum()` function, which performs well but
# may take some time to process due to its inherent efficiency. On the other hand,
# the second code employs the numpy module, known for its speed in handling large datasets.
# However, this approach has a drawback as it attempts to allocate 1 billion units
# of memory simultaneously, posing a risk of crashing the entire system before producing the result.
# While alternative methods exist for calculating the sum, it is crucial to prioritize optimal
# solutions when dealing with substantial datasets.

import time
start_time = time.time()

a = sum(range(1000000))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")
print(a)
# __________________________________________________________________
# __________________________________________________________________
start_time = time.time()
import numpy as np

# Create a NumPy array
my_array = np.array(range(1000000))

# Use numpy.sum() to calculate the sum
result = np.sum(my_array)

print(result)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")
print(result)


