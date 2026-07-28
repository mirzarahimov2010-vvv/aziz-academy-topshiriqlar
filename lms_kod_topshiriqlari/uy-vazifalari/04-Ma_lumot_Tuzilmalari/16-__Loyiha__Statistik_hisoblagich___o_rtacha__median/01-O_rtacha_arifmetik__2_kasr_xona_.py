numbers = [int(x) for x in input().split()]

average = sum(numbers) / len(numbers)


print(round(average, 2))