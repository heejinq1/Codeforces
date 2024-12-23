size = int(input())
inputs = list(input())
a_count = 0
d_count = 0
for i in range(size):
    if(inputs[i] == "A"):
        a_count+=1
    else:
        d_count+=1
if(a_count>d_count):
    print("Anton")
elif (d_count > a_count):
    print("Danik")
else:
    print("Friendship")