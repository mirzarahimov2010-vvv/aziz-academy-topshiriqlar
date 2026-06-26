n = int(input())
numbers = list(map(int, input().split()))
k = int(input())
closest_number = numbers[0]
min_distance = abs(numbers[0] - k)
for num in numbers[1:]:
    distance = abs(num - k)
    if distance < min_distance or (distance == min_distance and num < closest_number):
        closest_number = num 
        min_distance = distance 
print(closest_number)