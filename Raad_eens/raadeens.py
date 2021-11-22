import random

i=0
x=0


while i < 4:
    randomint = random.randint(1, 1000)
    print(randomint)
    x=0
    while x < 10:
        x+=1
        anwser = int(input("Wat is het geheime getal? \n"))

        if anwser == randomint:
            print("Goedzo")
            i+=1
            x+=10
        else:
            print("Probeer het nog eens")