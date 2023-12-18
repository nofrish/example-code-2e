
class FrenchDeck:
    ranks = ["A"] + [str(i) for i in range(2, 11)] + list("JQK")
    suits = "Spade Diamond Club Heart".split()

    def __init__(self) -> None:
        self._cards = [(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
    
    def __len__(self):
        print("calling __len__ magic method.")
        return len(self._cards)
    
    def __getitem__(self, index):
        print("calling __getitem__ magic method.")
        return self._cards[index]

    def __contains__(self, card):
        print("calling __contains__ magic method.")
        return card[0] in self.ranks and card[1] in self.suits



deck = FrenchDeck()

# Test Case: pick a random card in deck
import random
card = random.choice(deck)
print(card)

# Test Case: slicing
print(*deck[:13], sep='\n')