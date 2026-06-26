A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection = A & B 
union = A | B 
jaccard = len(intersection) / len(union)
print(f"{jaccard:.3f}")
