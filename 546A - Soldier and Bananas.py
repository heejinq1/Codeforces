inputs = input().split(" ")
cost = int(inputs[0])
money = int(inputs[1])
banana = int(inputs[2])
result = 0
total = 0
while(banana >0):
    total += banana*cost
    banana-=1
if(total <= money):
    print(0)
else:
    print(abs(total - money))