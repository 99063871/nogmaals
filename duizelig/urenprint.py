#Print de hele uren van de dag. Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe
i = 1
while i < 25:
    istr = str(i)
    i = i + 1
    if i < 12:
        print(istr + "AM")
    else:
        print(istr + "PM")