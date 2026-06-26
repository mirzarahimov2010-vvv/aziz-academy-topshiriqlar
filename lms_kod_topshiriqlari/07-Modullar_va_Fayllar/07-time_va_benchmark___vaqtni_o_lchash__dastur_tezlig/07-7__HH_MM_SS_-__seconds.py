time_str = input()
h, m, s = map(int, time_str.split(':'))
print(h * 3600 + m * 60 + s)