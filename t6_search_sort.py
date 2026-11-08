import random
import time


# 1. LINEAR SEARCH


def linear_search(numbers, target):

    for i in range(len(numbers)):

        if numbers[i] == target:
            return i

    return -1



# 2. BINARY SEARCH


def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1



# 3. BUBBLE SORT


def bubble_sort(numbers):

    arr = numbers.copy()

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if swapped == False:
            break

    return arr



# 4. SELECTION SORT


def selection_sort(numbers):

    arr = numbers.copy()

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



# 5. SIEVE PRIME COUNT


def sieve_prime(limit):

    prime = [True] * limit

    prime[0] = False
    prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):

        if prime[i]:

            for j in range(i * i, limit, i):
                prime[j] = False

    return sum(prime)



# 6. NAIVE PRIME COUNT


def naive_prime(limit):

    count = 0

    for num in range(2, limit):

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count



# 7. GENERATE RANDOM NUMBERS


random.seed(42)

numbers = []

for i in range(10000):
    numbers.append(random.randint(1, 100000))


# Sorted list for binary search
# sorted() is only used for checking results

sorted_numbers = sorted(numbers)

target = numbers[-1]



# 8. LINEAR SEARCH TIME


start = time.perf_counter()

linear_result = linear_search(numbers, target)

linear_time = time.perf_counter() - start

linear_correct = (
    linear_result != -1
    and numbers[linear_result] == target
)



# 9. BINARY SEARCH TIME


start = time.perf_counter()

binary_result = binary_search(sorted_numbers, target)

binary_time = time.perf_counter() - start

binary_correct = (
    binary_result != -1
    and sorted_numbers[binary_result] == target
)



# 10. BUBBLE SORT TIME


start = time.perf_counter()

bubble_result = bubble_sort(numbers)

bubble_time = time.perf_counter() - start

bubble_correct = bubble_result == sorted_numbers



# 11. SELECTION SORT TIME


start = time.perf_counter()

selection_result = selection_sort(numbers)

selection_time = time.perf_counter() - start

selection_correct = selection_result == sorted_numbers



# 12. SIEVE TIME


start = time.perf_counter()

sieve_result = sieve_prime(100000)

sieve_time = time.perf_counter() - start



# 13. NAIVE PRIME TIME


start = time.perf_counter()

naive_result = naive_prime(100000)

naive_time = time.perf_counter() - start



# 14. PRINT RESULTS TABLE


print("\nSEARCH AND SORT BENCHMARK")
print("-" * 55)

print(f"{'Algorithm':<20}{'Time (s)':<15}{'Correct'}")

print("-" * 55)

print(f"{'Linear Search':<20}{linear_time:<15.6f}{'yes' if linear_correct else 'no'}")

print(f"{'Binary Search':<20}{binary_time:<15.6f}{'yes' if binary_correct else 'no'}")

print(f"{'Bubble Sort':<20}{bubble_time:<15.6f}{'yes' if bubble_correct else 'no'}")

print(f"{'Selection Sort':<20}{selection_time:<15.6f}{'yes' if selection_correct else 'no'}")

print(f"{'Sieve (<100k)':<20}{sieve_time:<15.6f}{sieve_result} primes")

print(f"{'Naive (<100k)':<20}{naive_time:<15.6f}{naive_result} primes")

print("-" * 55)

print("Prime Results Match:", sieve_result == naive_result)


# 15. BIG-O EXPLANATION


print("\nBIG-O EXPLANATION:")

print("1. Linear Search O(n) checks numbers one by one.")

print("2. Binary Search O(log n)  faster divides the search area in half.")

print("3. Bubble and Selection Sort O(n^2) slow for large lists.")

print("4. Sieve is faster than naive prime checking.")

print("\nAssignment Completed!")