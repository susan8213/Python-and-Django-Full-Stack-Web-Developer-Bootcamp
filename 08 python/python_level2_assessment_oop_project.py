#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = []
        for suite in SUITE:
            for rank in RANKS:
                self.cards.append((suite, rank))

    def split(self):
        print("Split the deck in half.")
        return self.cards[:26], self.cards[26:]

    def shuffle(self):
        print("Shuffling the deck.")
        shuffle(self.cards)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.__cards = cards
    
    def add(self, cards):
        self.__cards.extend(cards)

    def remove_card(self):
        return self.__cards.pop(0)

    @property
    def cards(self):
        return len(self.__cards)


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))

        return drawn_card

    def remove_war_cards(self, is_first=False):
        war_cards = []

        if is_first:
            for _ in range(3):
                if self.has_card():
                    war_cards.append(self.hand.remove_card())
                else:
                    return None
        else:
            war_cards.append(self.hand.remove_card())
        
        return war_cards
    
    def has_card(self):
        return bool(self.hand.cards)


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
deck = Deck()
deck.shuffle()
first_half, last_half = deck.split()

player_name = input("What is your name player?")
user = Player(player_name, Hand(first_half))
comp = Player("Computer", Hand(last_half))

def winning_process():
    if RANKS.index(card_comp[1]) < RANKS.index(card_user[1]):
        print(user.name+" has the higher card, adding to hand.")
        user.hand.add(table_cards)
    else:
        print(comp.name+" has the higher card, adding to hand.")
        comp.hand.add(table_cards)

continued = 'y'

# Set Round Count
total_rounds = 0
war_count = 0
while (continued == 'y') and user.has_card() and comp.has_card():
    total_rounds += 1

    print("\n\n")
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(user.hand.cards))
    print(comp.name+" count: "+str(comp.hand.cards))
    print("Both players play a card!")
    print()

    table_cards = []
    
    # Play cards
    card_user = user.play_card()
    card_comp = comp.play_card()

    # Add to table_cards
    table_cards.append(card_user)
    table_cards.append(card_comp)

    if RANKS.index(card_user[1]) == RANKS.index(card_comp[1]):
        print("WAR!!!!!")
        is_first = True
        while user.has_card() and comp.has_card():
            war_count +=1
            print("We have a match, time for war!")
            if is_first:
                print("Each player removes 3 cards 'face down' and then one card face up")
            else:
                print("Each player removes 1 card 'face down' and then one card face up")

            war_card_user = user.remove_war_cards(is_first=is_first)
            war_card_comp = comp.remove_war_cards(is_first=is_first)

            if user.has_card() and comp.has_card():

                # Play cards
                card_user = user.play_card()
                card_comp = comp.play_card()

                # Add to table_cards
                table_cards.extend(war_card_user)
                table_cards.extend(war_card_comp)
                table_cards.append(card_user)
                table_cards.append(card_comp)

                if RANKS.index(card_user[1]) != RANKS.index(card_comp[1]):
                    winning_process()
                    break
            
            is_first = False

    else:
        winning_process()
    
    # continued = input("To be continued for the new round? (y/n)")


print("\n\n")
print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
print(user.name+" count: "+str(user.hand.cards))
print(comp.name+" count: "+str(comp.hand.cards))