size = int(input())
word = list(input().lower())
word = list(set(word))
if(len(word) == 26):
    print("YES")
else:
    print("NO")