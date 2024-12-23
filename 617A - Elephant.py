distance = int(input())
result = 0
while (distance >= 5):
    result = distance // 5
    distance %= 5
if distance >0:
    result+=1
print(result)