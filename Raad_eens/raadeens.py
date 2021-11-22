import random

i=0
x=0
correct = 0

print("U moet een geheim getal raden, u mag 10 keer een getal kiezen. Typ quit als u wilt stoppen.")
while i < 20:
    i+=1
    randomint = random.randint(1, 1000)
    print(randomint)
    x=0
    while x < 10:
        x+=1
        anwser = input("Wat is het geheime getal? \n")
        
        if anwser == "quit":
            print("U stopt")
            i+=20
            x+=10
        elif int(anwser) == randomint:
            print("Geraden")
            x+=10
            correct+=1
        else:
            print("U kan het nog", (10-x), "keer proberen")
            verschil = randomint-int(anwser)
            if randomint > int(anwser):
                print("Hoger")
            elif randomint < int(anwser):
                print("Lager")
            if verschil > 20 and verschil < 50:
                print("U bent warm")
            elif verschil > 0 and verschil < 20:
                print("U bent heel warm")
            if x == 10:
                print("U heeft het niet geraden het getal was", randomint)  
    print("U heeft nu", correct, "goed geraden") 
    if i < 20 and i > 0:
        round = input("Nog een getal raden?")
        if round == "ja":
            print("De volgende ronde gaat beginnen!")
        else:
            print("Het was gezellig")
            i+=20             

print("U heeft", correct, "goed geraden")