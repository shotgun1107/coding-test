from collections import Counter
print(*["Possible" if Counter(word[0]) == Counter(word[1]) else "Impossible" for word in[input().split() for _ in range(int(input()))]],sep='\n')