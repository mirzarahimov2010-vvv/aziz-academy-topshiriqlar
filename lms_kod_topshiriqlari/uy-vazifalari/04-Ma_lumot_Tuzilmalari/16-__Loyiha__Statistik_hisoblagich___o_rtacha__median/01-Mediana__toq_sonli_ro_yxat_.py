numbers = [int(x) for x in input().split()]

numbers.sort()

median_index = len(numbers) // 2 

print(numbers[median_index])