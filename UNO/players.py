from cards import Deck
import random

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def card_nums(self):
        return len(self.cards)
    
    def draw(self, deck, n=1):
        '''
        Draw a card from deck
        '''
        if n > len(deck): raise ValueError()
        for i in range(n):
            self.cards.append(deck.pop())

    def pop(self, n=1):
        result = []
        if n > self.card_nums(): raise ValueError()
        for i in range(n):
            result.append(self.cards.pop(random.randint(0, self.card_nums() - 1)))
        return result
    
    

if __name__ == '__main__':
    d1 = Deck()
    p1 = Player('yff', [])
    p1.draw(d1, 4)
    print(p1.cards)
    print(p1.cards.pop(1))



    


