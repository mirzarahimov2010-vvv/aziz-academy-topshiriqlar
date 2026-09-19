try:
    n = int(input())
    lst = [input() for _ in range(n)]
    index = int(input())
    print(lst[index])
except (IndexError, ValueError):
    print("OUT")