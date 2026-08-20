def eng_katta(*sonlar):
    return max(sonlar)

sonlar = list(map(int, input().split()))

print(eng_katta(*sonlar))