n = int(input())
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print(next_number-1)