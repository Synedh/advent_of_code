input = open('input').read().splitlines()

num1 = ''
num2 = ''
l = len(input)
for i in range(len(input[0])):
    num = [val[i] for val in input].count('0')
    num1 += str(int(num > l / 2))
    num2 += str(int(num < l / 2))
print(int(num1, 2) * int(num2, 2))