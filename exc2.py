i = 0
sum = 0
num1 = 0
num2 = 1

while i < 4000000 :
    num1 = sum
    num2 = num1
    sum = num1 + num2

    if (i % 2 == 0):
        sum += i

    print(sum)