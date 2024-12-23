word = input()
lower_letter = 0
upper_letter = 0
for i in range(len(word)):
    if(word[i].islower()):
        lower_letter +=1
    else:
        upper_letter +=1
if(lower_letter >= upper_letter):
    print(word.lower())
else:
    print(word.upper())