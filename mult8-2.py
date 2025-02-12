import numpy as np

# Read data from file 2
data2 = np.genfromtxt('file2', delimiter=' ', dtype=float)
data2_2d = data2.reshape((8, 3))

for i in range(1, 5):
    # Read data from file 1
    data1 = np.genfromtxt(f'file1_{i}', delimiter=r'\s+')
    data1_3d = data1.reshape((8, 3, 3))

    # Initialize an empty list to store the product of each set
    product = []

    # Perform matrix multiplication for each set
    for j in range(8):
        result = np.dot(data1_3d[j], data2_2d[j])
        result_2d = result.flatten()
        product.append(result_2d)

    # Convert the list of products into a 2D array
    product = np.array(product)

    # Sum all the x-components of the product matrices
    x_components_sum = np.sum(product[:, ::3])

    # Sum all the y-components of the product matrices
    y_components_sum = np.sum(product[:, 1::3])

    # Sum all the z-components of the product matrices
    z_components_sum = np.sum(product[:, 2::3])

    # Save the sums to a file named 'dipole_i' (where i is the file number)
    np.savetxt(f'dipole_{i}', [x_components_sum, y_components_sum, z_components_sum])

    print(f"Sums of x, y, z components for file{i} saved to 'dipole_{i}' file.")

