import math

# 1. Linear Search: Return all indices where the target appears
def linear_search_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

# 2. Binary Search: Find the correct insertion point in a sorted list
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # This is the index where the target should go

# 3. Linear Search: Count number of comparisons
def linear_search_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# 3. Binary Search: Count number of comparisons
def binary_search_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# 4. Jump Search: Search using block jumps (works only on sorted lists)
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # How many items to jump each time
    prev = 0

    # Jump until we find a block where target could be
    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Do a simple linear search within that block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# MAIN: Test everything together
def main():
    print("\nLinear Search All Indices")
    test_list = [3, 1, 4, 1, 5, 9, 1, 6]
    print("List:", test_list)
    print("All indices of 1:", linear_search_all(test_list, 1))

    print("\nBinary Search Insertion Point")
    sorted_list = [1, 3, 5, 7, 9]
    print("Sorted list:", sorted_list)
    print("Insert 6 at index:", binary_search_insertion_point(sorted_list, 6))

    print("\nCount Comparisons")
    sorted_list = list(range(0, 20, 2))  # [0, 2, 4, ..., 18]
    target = 10
    index_l, comp_l = linear_search_count(sorted_list, target)
    index_b, comp_b = binary_search_count(sorted_list, target)
    print(f"Linear Search -> Index: {index_l}, Comparisons: {comp_l}")
    print(f"Binary Search -> Index: {index_b}, Comparisons: {comp_b}")

    print("\nJump Search")
    sorted_list = list(range(0, 100, 3))  # [0, 3, 6, ..., 99]
    target = 45
    print("Sorted list:", sorted_list)
    print("Jump Search index of 45:", jump_search(sorted_list, target))

if __name__ == "__main__":
    main()
