n = int(input())
answer = [str(i) for i in range(1, n + 1) if all(int(str(i)[j+1]) - int(str(i)[j]) == int(str(i)[1]) - int(str(i)[0]) for j in range(len(str(i))-1))]
print(len(answer))
