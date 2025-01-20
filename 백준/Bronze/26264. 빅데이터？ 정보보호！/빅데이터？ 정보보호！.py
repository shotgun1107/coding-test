input()
print('security!') if (s := (string := input()).count('bigdata')) < (b := string.count('security')) else print('bigdata?') if b < s else print('bigdata? security!')