import time
import random

# -------------------------------
# Bubble Sort (with early stop)
# -------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if any swaps happen
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Stop if list is already sorted
    return arr

# -------------------------------
# Merge Sort (with insertion sort for small subarrays)
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 10:  # Use insertion sort for small chunks
        return insertion_sort(arr)
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------------------
# In-place Quick Sort (space efficient)
# -------------------------------
def quick_sort_in_place(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pick last element as pivot
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# -------------------------------
# Performance Comparison
# -------------------------------
def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", lambda x: bubble_sort(x.copy())),
        ("Merge Sort (Hybrid)", lambda x: merge_sort(x.copy())),
        ("Quick Sort (In-Place)", lambda x: quick_sort_in_place(x, 0, len(x) - 1) or x)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        result = func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# -------------------------------
# Main
# -------------------------------
def main():
    print("--- Testing All Sorts ---")
    
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test_arr)
    
    print("\nBubble Sort:", bubble_sort(test_arr.copy()))
    print("Merge Sort (Hybrid):", merge_sort(test_arr.copy()))
    
    quick_arr = test_arr.copy()
    quick_sort_in_place(quick_arr, 0, len(quick_arr) - 1)
    print("Quick Sort (In-Place):", quick_arr)
    
    print("\n--- Performance Test ---")
    large_arr = [random.randint(1, 1000) for _ in range(1000)]
    compare_sorting_algorithms(large_arr)

if __name__ == "__main__":
    main()
