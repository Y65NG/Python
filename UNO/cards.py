import random
from enum import Enum

# 数字牌由红黄蓝绿4色组成，每色都有数字牌0~9。数字牌每色有19张，1~9每色各2张，0每色各1张
# 功能牌也由红黄蓝绿4色组成。它们的名称分别为"跳过"、"反转"、"+2"。功能牌每种8张，每色2张，它们有着特殊的功能。
# 跳过：打出跳过后，你的下家不能出牌，轮到再下家出牌。
# 反转：打出反转后，当前出牌时针顺序将反转，轮到下家（原来的上家）出牌。
# +2：打出+2后，下家将被罚摸2张牌，并且不能出牌，轮到再下家出牌。
# +4

class CardType(Enum):
    NUMERAL = 0
    SKIP = 1
    REVERSE = 2
    DRAW_TWO = 3

class Color(Enum):
    RED = 0
    YELLOW = 1
    BLUE = 2
    GREEN = 3

    def __str__(self):
        return self.name.capitalize()


class Card:
    def __init__(self, card_type, color = None, number = None):
        self.card_type = card_type
        self.color = color
        self.number = number
    
    def __str__(self):
        if self.card_type == CardType.NUMERAL:
            return f'{self.color} {self.number}'
        elif self.card_type == CardType.DRAW_TWO:
            return f'{self.color} +2'
        elif self.card_type != CardType.NUMERAL:
            return f'{self.color} {self.card_type.name.capitalize()}'
        raise RuntimeError('Unknown type')

    def __repr__(self):
        if self.card_type == CardType.NUMERAL:
            return f'{self.color} {self.number}'
        elif self.card_type == CardType.DRAW_TWO:
            return f'{self.color} +2'
        elif self.card_type != CardType.NUMERAL:
            return f'{self.color} {self.card_type.name.capitalize()}'
        raise RuntimeError('Unknown type')

class Deck:
    def __init__(self):
        self.cards = []
        for color in [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]:
            for i in range(2):
                for num in range(10):
                    self.cards.append(Card(CardType.NUMERAL, color, num))
                for card_type in [CardType.SKIP, CardType.REVERSE, CardType.DRAW_TWO]:
                    self.cards.append(Card(card_type, color))
            self.cards.append(Card(CardType.NUMERAL, color, 0))
        self.current = len(self.cards)
        self.shuffle()

    def shuffle(self):
        for i in range(self.current - 1, -1, -1):
            self.cards[i], self.cards[random.randint(0, i)] = self.cards[random.randint(0, i)], self.cards[i]
    
    def fill(self):
        self.current = len(self.cards)
        self.shuffle()
    
    def pop(self):
        self.current -= 1
        return self.cards[self.current]
    
    def __len__(self):
        return self.current
    
    def __str__(self):
        # print(self.cards)
        return str(self.cards[:self.current])
        
