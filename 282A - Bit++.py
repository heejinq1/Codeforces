n = int(input())
x = 0
for _ in range(n):
    bit = input()
    if bit in ["X++", "++X"]:
        x+=1
    else:
        x-=1
print(x)