#code to compute the eigenvalue of the transition matrix
import numpy as np

# Define the transition matrix
P = np.array([
    [0.276, 0.308, 0.415],
    [0.237, 0.272, 0.491],
    [0.191, 0.261, 0.548]
])


'''P = np.array([
    [0.9, 0.075, 0.025],
    [0.15, 0.8, 0.05],
    [0.25, 0.25, 0.5]
])'''

# Compute the eigenvalues
eigenvalues, _ = np.linalg.eig(P)

# Check if all eigenvalues are less than one in absolute value
is_convergent = np.all(np.abs(eigenvalues) < 1)

print("Eigenvalues:", eigenvalues)
print("Does the matrix converge?", is_convergent)