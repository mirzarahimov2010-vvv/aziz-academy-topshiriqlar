n = int(input())
lst = [input() for _ in range(n)]


try:
    idx = int(input())
    print(lst[idx])
    
except IndexError:
    print("OUT")
except TypeError:
    print("TYPE")
except ValueError:
    print("TYPE")