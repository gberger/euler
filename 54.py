f = open("poker.txt", 'r')
rounds = f.read().split('\n')
cards = [a.split(' ') for a in rounds]
player1 = [c[0:5] for c in cards]
player2 = [c[5:10] for c in cards]

def cardsplit(card):
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    suits = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
    return (values[card[0]], suits[card[1]])
    
for x in player1[0]:
    print cardsplit(x)