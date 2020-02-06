import random

# Chọn bài Xì Dách vì gần gũi với người Việt hơn.

print('WELCOME TO BLACKJACK!')
print('+'+'-'*18+'+')
print('|'+'NOTE'.center(18,' ')+'|')
print('|'+'-'*18+'|')
print('| 0 : A' + '|'.rjust(13,' '))
print('| 10: 10, J, Q, K' + '|'.rjust(3,' '))
print('+'+'-'*18+'+')
print()

class player():
    def __init__(self,name):
        self.name = name
        self.bank = 0
        self.bet = 0
        self.cards = []
    def value(self):
        if sum(self.cards) == 0:
            s = 21
        elif sum(self.cards) <= 21:
            if len(self.cards) == 5:
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
        else:
            s = - sum(self.cards)
        return s

def result(player,ai):
    value = lambda v: 0 if v.value() in range(22,100) else v.value()
    if value(ai) > value(player):
        ai.bank += player.bet
        player.bank -= player.bet
        return 'loses'
    elif value(ai) == value(player):
        return 'draws'
    else:
        ai.bank -= player.bet
        player.bank += player.bet
        return 'wins'

draw = lambda p: abs(p.value()) < 16

ai = player('AI')
n = int(input('Number of players: '))
humans = [player(str(input('Player {}\'s name: '.format(p+1)))) for p in range(n)]
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
        humans[p].bet = int(input('{} bets (number > 0): '.format(humans[p].name)))
        humans[p].cards = []
    for p in dealing:
        players[p].cards += [deck.pop(0)]

    announce = []

    for p in range(len(humans)):
        if humans[p].value() == 21:
            announce += ['- {}\'s cards {} add up to {}.'.format(humans[p].name,humans[p].cards,humans[p].value())]
        else:
            # print('Your cards: {} = {}.'.format(you,value(you)))
            while draw(humans[p]):
                humans[p].cards += [deck.pop(0)]
            if abs(humans[p].value()) < 21:
                draw1 = str(input('{}: {} = {}. Draw more? (0 = no, 1 = yes) '.format(humans[p].name,humans[p].cards,humans[p].value()))) if abs(humans[p].value()) < 21 else 0
            while abs(humans[p].value()) < 21 and draw1 != '0':
                humans[p].cards += [deck.pop(0)]
                while draw(humans[p]):
                    humans[p].cards += [deck.pop(0)]
                draw1 = str(input('{}: {} = {}. Draw more? (0 = no, 1 = yes) '.format(humans[p].name,humans[p].cards,humans[p].value()))) if abs(humans[p].value()) < 21 else 0
            else:
                announce += ['- {} cards {} add up to {}.'.format(humans[p].name,humans[p].cards,humans[p].value())]

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
        print('- Computer\'s cards {} add up to {}. {} {}, your bank has {:,}.'.format(ai.cards,ai.value(),humans[p].name,result(humans[p],ai),humans[p].bank))
    playmore = str(input('\nPlay more? (0 = no, 1 = yes) '))
    print()
else:
    print('FINAL RESULTS')
    print('Computer has {:,} in the bank.'.format(ai.bank))
    for p in range(n):
        print('{} has {:,} in the bank.'.format(humans[p].name,humans[p].bank))
