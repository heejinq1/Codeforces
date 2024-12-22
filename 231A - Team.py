n = int(input())
count = 0
for _ in range(n):
    score = input().split(" ")
    sum = int(score[0])+int(score[1])+int(score[2])
    if(sum >=2):
        count+=1
    
print(count)