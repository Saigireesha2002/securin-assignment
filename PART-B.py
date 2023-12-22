def undoom_dice(Die_A, Die_B):
    # Initialize new dice configurations
    New_Die_A = [0] * 6
    New_Die_B = [0] * 6
    
    # Calculate the original distribution matrix for reference
    original_distribution = [[0] * 6 for _ in range(6)]
    for face_a in Die_A:
        for face_b in Die_B:
            original_distribution[face_a - 1][face_b - 1] += 1
    
    # Iterate through possible sums and update new dice configurations
    for k in range(2, 13):
        count = 0
        # Count occurrences of the sum in the original distribution
        for i in range(6):
            for j in range(6):
                if original_distribution[i][j] == k:
                    count += 1
        
        # Distribute the count to New_Die_A and New_Die_B
        for i in range(6):
            if New_Die_A[i] + 1 <= 4:
                New_Die_A[i] += min(count, 4 - New_Die_A[i])
                count -= min(count, 4 - New_Die_A[i])
            if count > 0:
                New_Die_B[i] += count

    return New_Die_A, New_Die_B

# Example usage with the provided input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

# Print the results
print("New_Die_A:", New_Die_A)
print("New_Die_B:", New_Die_B)