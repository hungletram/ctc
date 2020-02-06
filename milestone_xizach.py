import random

# Chọn bài Xì Dách vì gần gũi với người Việt hơn.

class player():
    def __init__(self):
        self.bank = 0
        self.bet = 0
        self.cards = []
    def value(self):
        if sum(self.cards) > 21:
            s = -21
        elif sum(self.cards) == 0:
            s = 21
        else:
            if len(self.cards) == 5 and sum(self.cards) <= 21:
                s = 100
            else:
                if 0 not in self.cards:
                    s = sum(self.cards)
                else:
                    if sum(self.cards) > 11:
                        s = sum(self.cards) + self.cards.count(0)
                    elif sum(self.cards) == 11:
                        s = sum(self.cards) + 10
                    else:
                        s = sum(self.cards) + 11
        return s

def result(player,ai):
    if ai.value() > player.value():
        ai.bank += player.bet
        player.bank -= player.bet
        return 'loses'
    elif ai.value() == player.value():
        return 'draws'
    else:
        ai.bank -= player.bet
        player.bank += player.bet
        return 'wins'

draw = lambda p: abs(p.value()) < 16

ai = player()
n = int(input('Number of players: '))
humans = [player() for i in range(n)]
players = humans + [ai]
dealing = [i for i in range(n+1)]*2

playmore = '1'

while playmore != '0':
    deck = []
    for i in range(4):
        deck += [0,2,3,4,5,6,7,8,9,10,10,10,10]
    random.shuffle(deck)

    ai.cards = []
    for p in range(len(humans)):
        humans[p].bet = int(input('Player {} bets: '.format(p+1)))
        humans[p].cards = []
    for p in dealing:
        players[p].cards += [deck.pop(0)]

    announce = []

    for p in range(len(humans)):
        if humans[p].value() == 21:
            announce += ['- Player {} cards {} add up to {}.'.format(p+1,humans[p].cards,humans[p].value())]
        else:
            # print('Your cards: {} = {}.'.format(you,value(you)))
            while draw(humans[p]):
                humans[p].cards += [deck.pop(0)]
            if abs(humans[p].value()) < 21:
                draw1 = str(input('Player {}: {} = {}. Draw more (0 = no, 1 = yes)? '.format(p+1,humans[p].cards,humans[p].value()))) if abs(humans[p].value()) < 21 else 0
            while abs(humans[p].value()) < 21 and draw1 != '0':
                humans[p].cards += [deck.pop(0)]
                draw1 = str(input('Player {}: {} = {}. Draw more (0 = no, 1 = yes)? '.format(p+1,humans[p].cards,humans[p].value()))) if abs(humans[p].value()) < 21 else 0
            else:
                announce += ['- Player {} cards {} add up to {}.'.format(p+1,humans[p].cards,humans[p].value())]

    for i in announce:
        print(i)

    while draw(ai):
        ai.cards += [deck.pop(0)]
    print('RESULT')

    cards = [len(p.cards) for p in humans]

    while sum(cards) > 0:
        p = cards.index(max(cards))
        cards[p] = 0
        if ai.value() > 0 and ai.value() < 21:
            if len(humans[p].cards) == 2:
                while ((1-(12/13)**(21-ai.value())) > (ai.value()-16)/6) and (abs(ai.value()) < 21):
                    ai.cards += [deck.pop(0)]
            else:
                while ((1-(12/13)**(21-ai.value())) > (1-21/(len(humans[p].cards)*13))) and (abs(ai.value()) < 21):
                    ai.cards += [deck.pop(0)]
        print('- Computers cards {} add up to {}. Player {} {}, your bank = {}.'.format(ai.cards,ai.value(),p+1,result(humans[p],ai),humans[p].bank))
    playmore = str(input('\nPlay more? (0 = no, 1 = yes) '))
    print()
else:
    print('FINAL RESULTS')
    print('Computer has {} in the bank.'.format(ai.bank))
    for p in range(n):
        print('Player {} has {} in the bank.'.format(p+1,humans[p].bank))
