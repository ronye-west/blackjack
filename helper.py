
# package import
import random

# returns the total of the entered deck
def calc_hand_sum(current_deck):
    face = ['J', 'Q', 'K']
    face_indices = [index for index, element in enumerate(current_deck) if element in face]
    for i in face_indices:
        current_deck[i] = 10
    ace_indices = [index for index, element in enumerate(current_deck) if element == 'A']
    for i in ace_indices:
        current_deck[i] = 11
    while sum(current_deck) > 21 and 11 in current_deck:
        current_deck[current_deck.index(11)] = 1
    return sum(current_deck)

# deck class
class deck:

    def __init__(self):
        self.current_deck = ['A', 'A', 'A', 'A',
                              2, 2, 2, 2,
                              3, 3, 3, 3,
                              4, 4, 4, 4,
                              5, 5, 5, 5,
                              6, 6, 6, 6,
                              7, 7, 7, 7,
                              8, 8, 8, 8,
                              9, 9, 9, 9,
                              10, 10, 10, 10,
                              'J', 'J', 'J', 'J',
                              'Q', 'Q', 'Q', 'Q',
                              'K', 'K', 'K', 'K']

# player class
class player():

    def __init__(self):
        self.current_deck = []

    def draw(self, deck):
        random_index = random.randint(0, len(deck.current_deck)-1)
        self.current_deck.append(deck.current_deck[random_index])
        deck.current_deck.pop(random_index)
        self.total = calc_hand_sum(self.current_deck)
        self.bust = True if self.total > 21 else False
        self.blackjack = True if self.total == 21 else False

    def split(self, deck):
        pass

# dealer class
class dealer(player):
    
    def __init__(self):
        self.current_deck = []

    def turn_1(self, deck):
        random_index = random.randint(0, len(deck.current_deck)-1)
        self.current_deck.append(deck.current_deck[random_index])
        deck.current_deck.pop(random_index)
        random_index = random.randint(0, len(deck.current_deck)-1)
        self.current_deck.append(deck.current_deck[random_index])
        deck.current_deck.pop(random_index)
        self.total = calc_hand_sum(self.current_deck)

    def turn_2(self, deck):
        while calc_hand_sum(self.current_deck) <= 16:
            self.draw(deck)
        self.bust = True if self.total > 21 else False