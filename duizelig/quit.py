i = 0
x = 1
while quit != "quit":
    vraag = input("Wil je nog verder?").lower()
    if vraag != "quit":
        i = i + 1
    else:
        while i >= x:
            print(x)
            x = x + 1
        quit = "quit"
