username = input()
username_list = list(set(list(username)))
if(len(username_list) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")