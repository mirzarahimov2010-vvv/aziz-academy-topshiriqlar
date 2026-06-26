numbers = list(map(int, input().split()))
mean_value = sum(numbers) / len(numbers)
deviations = [x - mean_value for x in numbers]
print(' '.join(f"{dev:.2f}" for dev in deviations))