nums = input().split(" ")
num = int(nums[0])
k = int(nums[1])
while(k>0):
    if(str(num)[-1] == "0"):
        num//=10
    else:
        num-=1
    k-=1
print(num)