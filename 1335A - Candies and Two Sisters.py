t = int(input())
for _ in range(t):
    candies = int(input())
    if (candies < 3):
        print(0)
    elif (candies % 2 == 0):
        print(candies // 2 -1)
    else:
        print(candies // 2 )