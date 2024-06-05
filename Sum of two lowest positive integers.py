def sum_two_smallest_numbers(numbers):
    numbers2 = numbers.copy()
    numbers2.remove(min(numbers))
    return min(numbers) + min(numbers2)


numbers = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(numbers))
