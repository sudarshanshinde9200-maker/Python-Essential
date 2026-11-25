import numpy as np
import matplotlib.pyplot as plt

# Generate a 10x10 random matrix
matrix = np.random.randint(0, 256, size=(10, 10))

print("Original Matrix:")
print(matrix)

# Normalize values between 0 and 1
normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("\nNormalized Matrix:")
print(normalized_matrix)

# Visualize as heatmap
plt.imshow(normalized_matrix, cmap='viridis')
plt.colorbar()
plt.title("Normalized Matrix Heatmap")
plt.show()