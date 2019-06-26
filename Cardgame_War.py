##import##
from random import shuffle

##class##
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"] #インデックス操作と値を一致

    def __init__(self, v, s):
        """スート（マーク）も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2): # less than
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2): # greater than
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self): # official string representaion
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前: ")
        name2 = input("プレーヤー2の名前: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは{}が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{}は{}、{}は{}を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("------------------------------------")
        print("戦争を始めます")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでPlay: "
            print("------------------------------------")
            response = input(m)
            if response == "q":
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            
            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
            print("------------------------------------")
            print("{}: {}勝  {}: {}勝".format(p1n, self.p1.wins, p2n, self.p2.wins))
            print("残り{}枚".format(len(cards)))
            print("------------------------------------")
            print()

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "引き分け！ 両者"

##main##

game = Game()
game.play_game()
    

"""
--deck creation test--

deck = Deck()
for card in deck.cards:
    print(card)
"""
