if __name__ == "__main__":
    import random

# Đối tượng bộ bài
class deck_of_cards():

    # Bộ bài chuẩn: 52 lá xếp theo thứ tự A-K, ♠-♥
    suits = ['♠','♣','♦','♥']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    deck_reset = []
    for rank in ranks:
        for suit in suits:
            deck_reset += [rank+suit]

    def __init__(self):
        self.deck = []

    # Trở về bộ bài chuẩn
    def reset(self):
        self.deck = self.deck_reset.copy()

    # Xào bài
    def shuffle(self):
        random.shuffle(self.deck)

    # Chia bài
    def dealing(self,everyone,number_of_cards):
        if len(everyone) * number_of_cards > len(self.deck):
            print('Không đủ bài để chia.')
        else:
            for p in [i for i in range(len(everyone))]*number_of_cards:
                everyone[p].cards += [self.deck.pop(-1)]

# Đối tượng người chơi
class player_xidach():
    def __init__(self):
        self.name = 'Người chơi'
        self.bank = 0
        self.bet = 0
        self.cards = []

    # Tính giá trị bài trên tay
    def value(self):
        points = []

        # Chuyển giá trị lá bài từ chuỗi thành số
        for card in self.cards:
            if card[:-1].isdigit():
                points += [int(card[:-1])]
            else:
                points += [0] if card[0] == 'A' else [10]
        
        s_min = sum(points) + points.count(0) # Số nút bài khi tính A = 1

        # Xì bàn
        if sum(points) == 0:
            s = 21
        
        # Không xì bàn
        elif s_min <= 21:

            # Ngũ Linh, số nút = s_min
            if len(points) == 5:
                s = 100 - s_min

            # Không Ngũ Linh
            else:

                # Không có A
                if 0 not in points:
                    s = sum(points)

                # Có A
                else:
                    if sum(points) > 11:
                        s = s_min
                    elif sum(points) == 11:
                        s = sum(points) + 10 if points.count(0) == 1 else s_min
                    else:
                        s = s_min if s_min > 11 else s_min + 10

        # Quắc
        else:
            s = 0
        return 0
    
    # Người chơi chưa đủ tuổi
    premature = lambda self: (self.value() in range(1,16)) and (len(self.cards) < 5)
    
    # Kết quả trên tay
    def result(self):
        c,n,s = ', '.join(self.cards),self.name,self.value()
        if s == 0:
            return '{} rút được {} quắc!!!'.format(n,c)
        # elif s <= 16:
        #     return '{} chưa đủ tuổi!!!'.format(n)
        elif s <= 21:
            return '{} rút được {} bằng {} nút.'.format(n,c,s)
        else:
            return '{} rút được Ngũ Linh {} bằng {} nút!!!'.format(n,c,100-s)

# Đối tượng nhà cái
class dealer_xidach(player_xidach):

    # Tính các xác suất để quyết định rút bài
    def strategy(self,player):
        draw = self.premature()
        if self.value() in range(16,21):
            if len(player.cards) == 2:
                if player.value() != 21:
                    if (1-(12/13)**(21-self.value())) > (self.value()-16)/6):
                        draw = True
            else:
                if (1-(12/13)**(21-self.value())) > (1-21/(len(player.cards)*13))):
                    draw = True
        return draw

# Tổ chức ván bài
class xidach():
    def __init__(self):
        self.deck = deck_of_cards()
        self.player = player_xidach()
        self.dealer = dealer_xidach()
        self.dealer.name = 'Cái'
    
    # Kết quả chung cuộc
    def result(self):
        print('-- KẾT QUẢ --')
        if self.player.value() < self.dealer.value():
            self.dealer.bank += self.player.bet
            self.player.bank -= self.player.bet
            return '- {}\n- {}\n- {} thua.'.format(self.player.result(),self.dealer.result(),self.player.name)
        elif self.player.value() == self.dealer.value():
            return '- {}\n- {}\n- Hòa.'.format(self.player.result(),self.dealer.result())
        else:
            self.dealer.bank -= self.player.bet
            self.player.bank += self.player.bet
            return '- {}\n- {}\n- {} thắng.'.format(self.player.result(),self.dealer.result(),self.player.name)
    
    # Chơi bài
    def play(self):
        playmore = '1'
        self.player.name = str(input('Tên người chơi: '))
        self.player.bank = int(input('Số vốn: '))
        while (playmore != '0') and (self.player.bank > 0):
            bet = int(input('\nSố tiền {} đang có là {:,}. Bạn đặt cược bao nhiêu? '.format(self.player.name,self.player.bank)))
            self.player.bet = bet if (bet <= self.player.bank and bet > 0) else self.player.bank
            self.player.cards = []
            self.dealer.cards = []
            self.deck.reset()
            self.deck.shuffle()
            self.deck.dealing([self.player,self.dealer],2)
            if self.dealer.value() == 21:
                print(self.result())
            else:
                while self.player.premature():
                    self.player.cards += [self.deck.deck.pop(0)]
                if self.player.value() in range(1,21):
                    ask = str(input('{} Bạn có rút thêm không (0=không, 1=có)? '.format(self.player.result())))
                while (self.player.value() in range(1,21)) and (ask == '1'):
                    self.player.cards += [self.deck.deck.pop(0)]
                    while self.player.premature():
                        self.player.cards += [self.deck.deck.pop(0)]
                    if self.player.value() in range(1,21):
                        ask = str(input('{} Bạn có rút thêm không (0=không, 1=có)? '.format(self.player.result())))
                
                while self.dealer.strategy(self.player):
                    self.dealer.cards += [self.deck.deck.pop(0)]
                
                print(self.result())
            playmore = str(input('Chơi tiếp (0=không, 1=có)? ')) if self.player.bank > 0 else '0'
        print('{} còn {:,}.'.format(self.player.name,self.player.bank))
game = xidach()
game.play()
