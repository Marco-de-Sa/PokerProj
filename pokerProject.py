from random import randint

# todo add a class dedicated to handling the cards dealt to the player and by extension detecting what hands they have
# todo add a way to count how many times specific hands have been encountered preferably in the above mentioned player hand class

class GameDeck:
    """
    This is the class that handles all operations that the deck of cards will need to undertake.
    The code that handles the hand of the player will most likely be in a different area.
    A brief description of the methods:

    this will probably need rewriting after the class is done

    __init__: will be automatically used on a new object of this class being made
    count_suit: counts the number of cards belonging to a specific suit that remain in the deck
    rejoin: will take a list of cards provided by the player and rejoin them into the deck
    deal_cards: deals out the specified number of cards in list form
    sort_deck: is at the moment non-functional, but it is planned to have a way for the player to
            select what sorting method will be used
    shuffle: self-explanatory, it will shuffle the cards remaining in the deck by switching 2
            random indexes 1000 times
    to_string: I am not sure if this name is in line with python naming practices with this sort
            of method, but basically it takes the deck of cards(list) and transforms it into a string
            which is returned
    """
    def __init__(self):
        self.spCard = {1: "ace", 2: "jack", 3: "queen", 4: "king"} # this dictionary contains all types of cards that do not begin with a number
        self.suit = {1: "clubs", 2: "spades", 3: "hearts", 4: "diamonds"} # a dictionary that stores all possible suits of cards
        # declares a list called deck that holds every type of card
        self.deck = ['ace of clubs', 'ace of spades', 'ace of hearts', 'ace of diamonds', '2 of clubs', '2 of spades', '2 of hearts', '2 of diamonds', '3 of clubs', '3 of spades', '3 of hearts', '3 of diamonds', '4 of clubs', '4 of spades', '4 of hearts', '4 of diamonds', '5 of clubs', '5 of spades', '5 of hearts', '5 of diamonds', '6 of clubs', '6 of spades', '6 of hearts', '6 of diamonds', '7 of clubs', '7 of spades', '7 of hearts', '7 of diamonds', '8 of clubs', '8 of spades', '8 of hearts', '8 of diamonds', '9 of clubs', '9 of spades', '9 of hearts', '9 of diamonds', '10 of clubs', '10 of spades', '10 of hearts', '10 of diamonds', 'jack of clubs', 'jack of spades', 'jack of hearts', 'jack of diamonds', 'queen of clubs', 'queen of spades', 'queen of hearts', 'queen of diamonds', 'king of clubs', 'king of spades', 'king of hearts', 'king of diamonds']

    def count_suit(self, target):
        temp = 0 # this variable keeps count of every time a card of target suit is found
        for i in self.deck: # iterates through the deck and checks where the last index is equal to the target String
            if i.split(" ")[-1] == target:
                temp += 1
        print(f"There are {temp} cards belonging to {target} remaining in the deck") # prints out the amount of cards belonging to the target suit

    def rejoin(self, hand):
        for i in range(len(hand)): # takes the iterates through the hand indexes
            self.deck.append(hand.pop()) # pops each hand value into the deck

    def deal_cards(self, card_count):
        # todo add a way to sort cards before handing them out
        temp = [] # creates a temporary list
        for i in range(int(card_count)): # converts car_count to an integer and then iterates throughout it
            temp.append(self.deck.pop()) # appends the specified amount(from card_count) to the temp list by popping them from the deck
        return temp # returns the temp list

    def sort_cards(self):
        # wip not ready for use(will work if used however just not in it's final state)
        # possible solution is to get every suit into it's own list and sort them by their numbers and then rejoin them in a specific order
        # todo add a method to sort the cards by suit and number
        # todo allow add new methods of sorting from what we have learned so far and let the user choose between them
        # Heap Sort, Binary Insertion Sort, Merge Sort and
        # A sorting algorithm of your choice not taught in class, with average
        # time complexity of at most O(n log n) all need to be implemented

        tempDeck = []
        for i in range(len(self.deck)):
            if self.deck[i].split(' ')[0] == "ace":
                tempDeck.append(self.deck[i])

        for i in range(2, 11): # to sort card numbers
            for j in range(len(self.deck)):# to get iterate through the deck
                if self.deck[j].split(' ')[0] == str(i):
                    tempDeck.append(self.deck[j])

        for i in range(2, 5):
            for j in range(len(self.deck)):
                if self.deck[j].split(' ')[0] == self.spCard[i]:
                    tempDeck.append(self.deck[j])
        self.deck = tempDeck

    def shuffle(self):
        for i in range(1000): # iterates the code 1000 times
            ind1, ind2 = randint(0,51), randint(0,51) # randomly generates two indexes that will be swapped later
            # below swaps the two random indexes of the deck variable
            temp = self.deck[ind1]
            self.deck[ind1] = self.deck[ind2]
            self.deck[ind2] = temp

        # todo below is the fisher yates method of shuffling it is as I have found to be the most efficient method of shuffling find a way to implement it
        # numbers = list(range(n))
        # shuffled = []
        # while numbers:
        # k = randint(0, len(numbers) - 1)
        # shuffled.append(numbers[k])
        # numbers.pop(k)
        # return shuffled

    def __str__(self): # this method overwrites the default __str__ method to instead return the string below
        return f"{self.deck}" # returns the deck as a string

my_hand = GameDeck() # makes a new object of the GameDeck class

my_hand.count_suit("hearts")
print(my_hand)
my_hand.shuffle()
print(my_hand)
tem = my_hand.deal_cards(5)
print(my_hand)
print(tem)
my_hand.rejoin(tem)
print(my_hand)
my_hand.sort_cards()
print(my_hand)