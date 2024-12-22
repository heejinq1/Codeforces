a = input().split(" ")

score = input().split(" ")
k = int(score[int(a[1])-1])
output = 0
for x in score:
    if(int(x) >= k and int(x)>0):
        output += 1
print(output)