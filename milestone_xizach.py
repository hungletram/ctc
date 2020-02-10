import random

# Chọn bài Xì Dách vì gần gũi với người Việt.

print('WELCOME TO BLACKJACK!')
print('+'+'-'*18+'+')
print('|'+'NOTE'.center(18,' ')+'|')
print('|'+'-'*18+'|')
print('| 0 : A' + '|'.rjust(13,' '))
print('| 10: 10, J, Q, K' + '|'.rjust(3,' '))
print('+'+'-'*18+'+')
print()

# tạo đối tượng người chơi, gồm tên, tài khoản, đặt cược và lá bài
class player():
    def __init__(self,name):
        self.name = name
        self.bank = 0
        self.bet = 0
        self.cards = []
        
    # phương thức tính toán số nút bài trên tay người chơi
    def value(self):
        # s_min = số nút trên tay khi coi Ace = 1 nút
        s_min = sum(self.cards) + self.cards.count(0)
        
        # xì bàn
        if sum(self.cards) == 0:
            s = 21
        
        # không quắc
        elif s_min <= 21:
            
            # ngũ linh: thắng xì bàn và ngũ linh lớn nút hơn
            if len(self.cards) == 5:
                s = 100 - s_min

            # không ngũ linh
            else:
                # không có Ace
                if 0 not in self.cards:
                    s = sum(self.cards)
                # có Ace
                else:
                    # số nút còn lại > 11, Ace = 1 nút
                    if sum(self.cards) > 11:
                        s = s_min
                    # số nút còn lại = 11 và có 1 Ace thì Ace = 10, có hơn 1 Ace thì Ace = 1
                    elif sum(self.cards) == 11:
                        s = sum(self.cards) + 10 if self.cards.count(0) == 1 else s_min
                    # (số nút còn lại < 11 nút) và (số Ace > 11 - số nút còn lại) thì tính Ace = 1
                    # <= số nút còn lại thì 1 con Ace = 11, còn lại tính Ace = 1
                    else:
                        s = s_min if s_min > 11 else s_min + 10
        # quắc
        else:
            s = sum(self.cards)
            
        # nếu quắc thì xuất số âm, không quắc thì xuất số dương
        return -s if s in range(22,79) else s

def result(player,ai):
    value = lambda v: 0 if v.value() < 0 else v.value()
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

    if ai.value() == 21:
        print('- Computer cards {} add up to 21.'.format(ai.cards))
        for p in humans:
            print('- {} {}. Your bank has {}.'.format(p.name,result(p,ai),p.bank))
    else:
        announce = []

        for p in range(len(humans)):
            if humans[p].value() == 21:
                announce += ['- {} cards {} add up to {}.'.format(humans[p].name,humans[p].cards,humans[p].value())]
            else:
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
            if abs(ai.value()) < 21:
                if len(humans[p].cards) == 2:
                    if humans[p].value() != 21:
                        while ((1-(12/13)**(21-ai.value())) > (ai.value()-16)/6) and (abs(ai.value()) < 21):
                            ai.cards += [deck.pop(0)]
                else:
                    while ((1-(12/13)**(21-ai.value())) > (1-21/(len(humans[p].cards)*13))) and (abs(ai.value()) < 21):
                        ai.cards += [deck.pop(0)]
            print('- Computer cards {} add up to {}. {} {}, your bank has {:,}.'.format(ai.cards,ai.value(),humans[p].name,result(humans[p],ai),humans[p].bank))
    playmore = str(input('\nPlay more? (0 = no, 1 = yes) '))
    print()
else:
    print('FINAL RESULT')
    print('Computer has {:,} in the bank.'.format(ai.bank))
    for p in range(n):
        print('{} has {:,} in the bank.'.format(humans[p].name,humans[p].bank))
