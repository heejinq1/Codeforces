tmp = input().split(" ")
limak = int(tmp[0])
bob = int(tmp[1])
result = 0
while(limak <= bob):
    limak*=3
    bob*=2
    result+=1
print(result)