# Find all pairs with a given sum in an array

def find_pairs(arr, target):
    pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))

    return pairs


# Input
array = [2, 4, 3, 5, 7, 8, 1]
target_sum = 7

# Function call
result = find_pairs(array, target_sum)

# Output
print("Pairs with given sum are:", result)
