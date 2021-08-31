import random
suits=("spades","clover","hearts","diamond")
ranks=("two","three","four","five","six","seven","eight","nine","jack","queen","king","ace")
values={"two":2,"three":3,"four":4,"five":4,"six":6,"seven":7,"eight":8,"nine":9,"jack":10,"queen":10,"king":10,"ace":11}

class Card():
    def __init__(self,suit, rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+" of "+self.suit

class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_img=''
        for card in self.deck:
            deck_img+="\n"+card.__str__()
        return 'the deck has '+deck_img
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
       self.cards=[]
       self.value=0
       self.ace=0

    def add(self,card1):
        self.cards.append(card1)
        self.value+=values[card1.rank]
        if card1.rank == 11:
            self.ace+=1
    def ace_adjust(self):
        while self.value>21 and self.ace==0:
            self.value-=10
            self.ace-=1

class Chips():
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        chips.bet=int(input("enter your bet"))
        if chips.bet>chips.total:
            print("sorry bet more the your total money , ur total money is {}".format(chips.total))
        else:
            break



def hit(deck,hand):
    single_card=deck.deal()
    hand.add(single_card)
    hand.ace_adjust()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("enter hit or stand by typing h or s ")
        if x.lower() == 'h':
            hit(deck, hand)

        elif x.lower() == 's':
            print("player decided to stand ")
            playing=False
        else:
            print("enter h or s ")
            continue

        break

playing=True
def show_some(player,dealer):
    print("\n dealer hand")
    print("one card is hidden")
    print(dealer.cards[1])
    print('\n player hands')
    for i in player.cards:
        print(i)

def show_all(player,dealer):
    print("\n dealer hand")
    for i in dealer.cards:
        print(i)

    print('\n player hands')
    for i in player.cards:
        print(i)

def player_bust(chips):
    print("player is busted ")
    chips.lose_bet()

def player_wins(chips):
    print("player wins")
    chips.win_bet()

def dealer_bust(chips):
    print("player wins as dealer bust")
    chips.win_bet()

def dealer_wins(chips):
    print("dealer wins ")
    chips.lose_bet()

def push():
    print("they both tie")

#the game is starting
while True:
    print("welcome to black jack game ")
    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    player1.add(deck.deal())
    player1.add(deck.deal())
    dealer = Hand()
    dealer.add(deck.deal())
    dealer.add(deck.deal())
    player_chips = Chips()
    take_bet(player_chips)
    show_some(player1, dealer)
    while playing:
        hit_or_stand(deck, player1)
        show_some(player1,dealer)

        if player1.value > 21:
            player_bust(player1, dealer, player_chips)

            break

    if player1.value <= 21:
        while dealer.value < player1.value:
            hit(deck, dealer)

        show_all(player1, dealer)

        if dealer.value > 21:
            dealer_bust(player_chips)
        elif dealer.value > player1.value:
            dealer_wins(player_chips)
        elif dealer.value < player1.value:
            player_wins(player_chips)
        else:
            push()

    print("\n player total chips are {}".format(player_chips.total))
    #for new game
    n_g=input("do u wanna continue ? y or n ")
    if n_g=='y':
        playing=True
        continue
    else:
        print("thanks ")
        break












