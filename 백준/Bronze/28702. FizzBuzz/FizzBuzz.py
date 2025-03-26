s = [input().strip() for _ in range(3)]

for i in range(2, -1, -1):
    if s[i].isdigit():
        answer = int(s[i]) + (3-i)
        break      
        
if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)