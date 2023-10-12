from collections import Counter
print(sum((Counter(s := input()) - Counter(s1 := input())).values()) + sum((Counter(s1) - Counter(s)).values()) )