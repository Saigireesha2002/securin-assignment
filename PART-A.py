# Define the faces of the dice
die_faces = [1, 2, 3, 4, 5, 6]

# Calculate the total combinations
total_combinations = len(die_faces) * len(die_faces)
print("Total combinations possible:", total_combinations)

# Create and initialize the matrix
mat = [[0] * 6 for _ in range(6)]

# Populate the matrix and print the sums
for i in range(1, 7):
    for j in range(1, 7):
        mat[i-1][j-1] = i + j
        print(i + j, end=" ")
    print()

# Calculate and print the probabilities
for k in range(2, 13):
    count = sum(1 for row in mat for value in row if value == k)
    print(f"P(S={k}) = {count}/{total_combinations}")
