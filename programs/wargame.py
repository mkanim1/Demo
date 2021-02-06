suits = ["Hearts", "Spades", "Clubs", "Diamonds" ]
deck = []
i=1
for i in range(1,14):
    if i == 1:
        value = "A"
    elif i == 11:
        value = "J"
    elif i == 12:
        value = "Q"
    elif i == 13:
        value = "K"
    else:
        value = str(i)
    j = 0
    for j in range(len(suits)):
        card = value + " " + suits[j]
        deck.append(card)

print(deck)
print("Length of deck", len(deck))