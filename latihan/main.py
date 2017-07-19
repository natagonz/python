import random

a = random.randint(1,2)

def main(number):
    if number == a :
        return "win"
    else :
        return "lose the number is " + str(a)

print main(int(raw_input("word ")))
