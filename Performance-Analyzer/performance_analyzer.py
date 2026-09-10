"""
Algorithm Performance Analyzer
Compares theoretical vs experimental time complexity of sorting algorithms
by measuring actual execution time across different input sizes.
"""

import time
import random
import csv
import matplotlib.pyplot as plt


# ---------- Sorting Algorithms ----------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


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
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
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


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = _partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------- Performance Measurement ----------

ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

INPUT_SIZES = [100, 500, 1000, 2000, 3000, 5000]


def measure_time(sort_func, arr):
    """Runs sort_func on a copy of arr and returns time taken in seconds."""
    data = arr.copy()
    start = time.perf_counter()
    sort_func(data)
    end = time.perf_counter()
    return end - start


def run_analysis():
    results = {name: [] for name in ALGORITHMS}

    for size in INPUT_SIZES:
        print(f"\nTesting input size: {size}")
        base_arr = [random.randint(0, 100000) for _ in range(size)]

        for name, func in ALGORITHMS.items():
            elapsed = measure_time(func, base_arr)
            results[name].append(elapsed)
            print(f"  {name:20s}: {elapsed:.6f} sec")

    return results


def save_results_csv(results, filename="performance_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Input Size"] + list(results.keys()))
        for i, size in enumerate(INPUT_SIZES):
            row = [size] + [results[name][i] for name in results]
            writer.writerow(row)
    print(f"\nResults saved to {filename}")


def plot_results(results, filename="performance_graph.png"):
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(INPUT_SIZES, times, marker="o", label=name)

    plt.title("Sorting Algorithm Performance: Time vs Input Size")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    print(f"Graph saved to {filename}")
    plt.show()


def main():
    print("=" * 50)
    print("ALGORITHM PERFORMANCE ANALYZER")
    print("=" * 50)

    results = run_analysis()
    save_results_csv(results)
    plot_results(results)


if __name__ == "__main__":
    main()