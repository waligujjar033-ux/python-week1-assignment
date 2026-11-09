import random
import time

# ----------------------------------
# 1. GENERATE 10,000 RANDOM NUMBERS
# ----------------------------------

random.seed(42)

numbers = []

for i in range(10000):
    numbers.append(random.randint(1, 100000))

# Sorted list for checking results
correct_list = sorted(numbers)

target = numbers[-1]


# ----------------------------------
# 2. LINEAR SEARCH
# ----------------------------------

start = time.perf_counter()

linear_result = -1

for i in range(len(numbers)):

    if numbers[i] == target:
        linear_result = i
        break

linear_time = time.perf_counter() - start

linear_correct = (
    linear_result != -1
    and numbers[linear_result] == target
)


# ----------------------------------
# 3. BINARY SEARCH
# ----------------------------------

start = time.perf_counter()

left = 0
right = len(correct_list) - 1

binary_result = -1

while left <= right:

    mid = (left + right) // 2

    if correct_list[mid] == target:
        binary_result = mid
        break

    elif correct_list[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

binary_time = time.perf_counter() - start

binary_correct = (
    binary_result != -1
    and correct_list[binary_result] == target
)


# ----------------------------------
# 4. BUBBLE SORT
# ----------------------------------

bubble_list = numbers.copy()

start = time.perf_counter()

n = len(bubble_list)

for i in range(n):

    swapped = False

    for j in range(n - i - 1):

        if bubble_list[j] > bubble_list[j + 1]:

            bubble_list[j], bubble_list[j + 1] = (
                bubble_list[j + 1],
                bubble_list[j]
            )

            swapped = True

    if swapped == False:
        break

bubble_time = time.perf_counter() - start

bubble_correct = bubble_list == correct_list


# ----------------------------------
# 5. SELECTION SORT
# ----------------------------------

selection_list = numbers.copy()

start = time.perf_counter()

n = len(selection_list)

for i in range(n):

    min_index = i

    for j in range(i + 1, n):

        if selection_list[j] < selection_list[min_index]:
            min_index = j

    selection_list[i], selection_list[min_index] = (
        selection_list[min_index],
        selection_list[i]
    )

selection_time = time.perf_counter() - start

selection_correct = selection_list == correct_list


# ----------------------------------
# 6. SIEVE OF ERATOSTHENES
# ----------------------------------

start = time.perf_counter()

limit = 100000

prime = [True] * limit

prime[0] = False
prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):

    if prime[i]:

        for j in range(i * i, limit, i):
            prime[j] = False

sieve_count = sum(prime)

sieve_time = time.perf_counter() - start


# ----------------------------------
# 7. NAIVE PRIME CHECK
# ----------------------------------

start = time.perf_counter()

naive_count = 0

for num in range(2, limit):

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        naive_count += 1

naive_time = time.perf_counter() - start


# ----------------------------------
# 8. PRINT RESULTS
# ----------------------------------

print("\nSEARCH AND SORT BENCHMARK")
print("-" * 55)

print(f"{'Algorithm':<20}{'Time (s)':<15}{'Correct'}")

print("-" * 55)

print(f"{'Linear Search':<20}{linear_time:<15.6f}{'yes' if linear_correct else 'no'}")

print(f"{'Binary Search':<20}{binary_time:<15.6f}{'yes' if binary_correct else 'no'}")

print(f"{'Bubble Sort':<20}{bubble_time:<15.6f}{'yes' if bubble_correct else 'no'}")

print(f"{'Selection Sort':<20}{selection_time:<15.6f}{'yes' if selection_correct else 'no'}")

print(f"{'Sieve (<100k)':<20}{sieve_time:<15.6f}{sieve_count} primes")

print(f"{'Naive (<100k)':<20}{naive_time:<15.6f}{naive_count} primes")

print("-" * 55)

print("Prime Results Match:", sieve_count == naive_count)


# ----------------------------------
# 9. BIG-O EXPLANATION
# ----------------------------------

print("\nBIG-O EXPLANATION:")

print("1. Linear Search O(n) checks numbers one by one.")

print("2. Binary Search O(log n) divides the search area in half.")

print("3. Bubble Sort and Selection Sort O(n^2) are slow for large lists.")

print("4. Sieve is faster than naive prime checking.")

print("\nAssignment Completed!")