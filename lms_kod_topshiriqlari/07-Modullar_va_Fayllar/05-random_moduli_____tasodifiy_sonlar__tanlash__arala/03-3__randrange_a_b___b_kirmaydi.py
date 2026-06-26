import random 

seed_value = int( input())
a, b = map(int, input().split())

random.seed( seed_value )

for _ in range( 5):
    print(random.randint( a, b ))