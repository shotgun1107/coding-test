from collections import Counter
print('go' if sum(Counter(input()).values()) >= sum(Counter(input()).values()) else 'no')
