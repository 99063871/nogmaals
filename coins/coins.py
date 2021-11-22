# name of student: Stijn van Gils
# number of student: 99063871
# purpose of program: work
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #vraagt wat er betaald moet worden en doet het keer 100
paid = int(float(input('Paid amount: ')) * 100) #vraagt wat er betaald is en doet het keer 100
change = paid - toPay #berekend het wisselgeld

if change > 0: #als het wisselgeld meer dan 0 is word het uitgevoerd
  coinValue = 500 #zet de value van de coin naar 50
  
  while change > 0 and coinValue > 0: #als wisselgeld en coinvalue meer dan 0 is voert de while loop uit
    nrCoins = change // coinValue #deelt change met coinvalue en zet het in de variable nrCoins

    if nrCoins > 0: #als de variable meer dan 0 is word het uitgevoert
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #er word geprint hoeveel muntjes van coinvalue je moet hebben
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #vraagt hoeveel coins je terug hebt gegeven
      change -= nrCoinsReturned * coinValue #eht kijkt of het goed gegeven is

# comment on code below: het checkt hoeveel coinvalue is en gaat door tot het 0 is
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #het kijkt of het wisselgeld is gegeven
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')