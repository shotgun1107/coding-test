from collections import Counter

input()
print(max(Counter(input().replace(' ','')).values()))