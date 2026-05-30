numbers = list(map(int, input().split()))
mean_value = sum(numbers) / len(numbers)
range_value = max(numbers) - min(numbers)
if range_value == 0:
    z_values = [0.00] * len(numbers)
else:
    z_values = [(x - mean_value) / range_value for x in numbers]
print(' '.join(f"{z:.2f}" for z in z_values))