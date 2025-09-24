import random
f = open("name_list.txt","r",encoding="UTF-8")
lines = f.readlines()
print("You are lucky:", random.choice(lines))
