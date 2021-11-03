days = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
i = 0
x = int(input("Tot en met welke dag wilt u het hebben?(vul het in met getallen)"))
if x < 0 or x > 7:
    print("probeer dat opnieuw")
else:
    while i < x:
        print(days[i])
        i = i + 1


