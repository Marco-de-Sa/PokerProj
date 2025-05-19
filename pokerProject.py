from random import randint

# todo add a class dedicated to handling the cards dealt to the player and by extension detecting what hands they have
# todo add a way to count how many times specific hands have been encountered preferably in the above mentioned player hand class

class GameDeck:
    """
    This is the class that handles all operations that the deck of cards will need to undertake.
    The code that handles the hand of the player will most likely be in a different area.
    A brief description of the methods:

    todo this will probably need rewriting after the class is done

    __init__: will be automatically used on a new object of this class being made
    count_suit: counts the number of cards belonging to a specific suit that remain in the deck
    rejoin: will take a list of cards provided by the player and rejoin them into the deck
    deal_cards: deals out the specified number of cards in list form
    sort_deck: is at the moment non-functional, but it is planned to have a way for the player to
            select what sorting method will be used
    shuffle: shuffles the deck of cards using the fisher yates method
    __str__: this method overwrites the default __str__ method to instead return the string below
            this is used to print out the deck of cards in a string format

    """
    def __init__(self):
        # declares a list called deck that holds every type of card
        self.deck = ['ace of clubs', 'ace of spades', 'ace of hearts', 'ace of diamonds', '2 of clubs', '2 of spades', '2 of hearts', '2 of diamonds', '3 of clubs', '3 of spades', '3 of hearts', '3 of diamonds', '4 of clubs', '4 of spades', '4 of hearts', '4 of diamonds', '5 of clubs', '5 of spades', '5 of hearts', '5 of diamonds', '6 of clubs', '6 of spades', '6 of hearts', '6 of diamonds', '7 of clubs', '7 of spades', '7 of hearts', '7 of diamonds', '8 of clubs', '8 of spades', '8 of hearts', '8 of diamonds', '9 of clubs', '9 of spades', '9 of hearts', '9 of diamonds', '10 of clubs', '10 of spades', '10 of hearts', '10 of diamonds', 'jack of clubs', 'jack of spades', 'jack of hearts', 'jack of diamonds', 'queen of clubs', 'queen of spades', 'queen of hearts', 'queen of diamonds', 'king of clubs', 'king of spades', 'king of hearts', 'king of diamonds']

###########################################################################################################

    def count_suit(self, target):
        """this method counts all the cards belonging to the specified suit"""
        # warning this method may be vestigial feel free to use it in your code though but please do tell me if you do otherwise I will delete this
        temp = 0 # this variable keeps count of every time a card of target suit is found
        for i in self.deck: # iterates through the deck and checks where the last index is equal to the target String
            if i.split(" ")[-1] == target:
                temp += 1
        print(f"There are {temp} cards belonging to {target} remaining in the deck") # prints out the amount of cards belonging to the target suit

###########################################################################################################

    def rejoin(self, hand):
        """this method joins a given list onto the card deck in the class"""
        for i in range(len(hand)): # takes the iterates through the hand indexes
            self.deck.append(hand.pop()) # pops each hand value into the deck

###########################################################################################################

    def deal_cards(self, card_count):
        """returns the specified amount of cards"""
        # todo add a way to sort cards before handing them out
        temp = [] # creates a temporary list
        for i in range(int(card_count)): # converts car_count to an integer and then iterates throughout it
            temp.append(self.deck.pop()) # appends the specified amount(from card_count) to the temp list by popping them from the deck
        return temp # returns the temp list
    
###########################################################################################################

    def sort_cards(self, optional):
        """
        this method sorts the deck of cards in a specific order using a sorting algorithm chosen by the user
        """

        # beware code here is WIP and not ready for use
        tempDeck = [] # creates a temporary list
        if optional == list:
            tempDeck = optional # makes a copy of the optional list to sort
        else:
            tempDeck = self.deck.copy() # makes a copy of the deck to sort
        # the code below is used to replace the face cards with numbers to make sorting easier
        # 1 = ace, 11 = jack, 12 = queen, 13 = king
        for i in range(len(tempDeck)):
            if tempDeck[i].split(" ")[0] == "ace":
                tempDeck[i] = f"1 {tempDeck[i].split(' ')[1]} {tempDeck[i].split(' ')[2]}" 
            if tempDeck[i].split(" ")[0] == "jack":
                tempDeck[i] = f"11 {tempDeck[i].split(' ')[1]} {tempDeck[i].split(' ')[2]}"
            if tempDeck[i].split(" ")[0] == "queen":
                tempDeck[i] = f"12 {tempDeck[i].split(' ')[1]} {tempDeck[i].split(' ')[2]}"
            if tempDeck[i].split(" ")[0] == "king":
                tempDeck[i] = f"13 {tempDeck[i].split(' ')[1]} {tempDeck[i].split(' ')[2]}"
        
        heart, diamond, club, spade = [], [], [], [] # creates 4 empty lists to hold the cards of each suit

        # this code below is used to sort the cards into their respective suits
        for i in range(len(tempDeck)):
            if tempDeck[i].split(" ")[2] == "spades":
                spade.append(tempDeck[i])
            if tempDeck[i].split(" ")[2] == "hearts":
                heart.append(tempDeck[i])
            if tempDeck[i].split(" ")[2] == "clubs":
                club.append(tempDeck[i])
            if tempDeck[i].split(" ")[2] == "diamonds":
                diamond.append(tempDeck[i])
        
        sortingType = input("What type of sorting would you like to use? (heapsort, binary insertion, merge sort or quick sort): ")

        if sortingType == "heapsort":
            def heapify(arr, n, i):
                # Initialize largest as root
                largest = i 
                #  left index = 2*i + 1
                l = 2 * i + 1 
                # right index = 2*i + 2
                r = 2 * i + 2  
                # If left child is larger than root
                if l < n and int(arr[l].split(" ")[0]) > int(arr[largest].split(" ")[0]):
                    largest = l
                # If right child is larger than largest so far
                if r < n and int(arr[r].split(" ")[0]) > int(arr[largest].split(" ")[0]):
                    largest = r
                # If largest is not root
                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]  # Swap
                    # Recursively heapify the affected sub-tree
                    heapify(arr, n, largest)

            # Main function to do heap sort
            def heapSort(arr):
                n = len(arr)
                # Build heap (rearrange array)
                for i in range(n // 2 - 1, -1, -1):
                    heapify(arr, n, i)
                    
                # One by one extract an element from heap
                for i in range(n - 1, 0, -1):
                    # Move root to end
                    arr[0], arr[i] = arr[i], arr[0] 
                    # Call max heapify on the reduced heap
                    heapify(arr, i, 0)
                    
            heapSort(spade)
            heapSort(heart)
            heapSort(club)
            heapSort(diamond)

        elif sortingType == "binary insertion":
            def insertion_sort(arr):
                for i in range(1, len(arr)):
                    for j in range(i):
                        if int(arr[i].split(' ')[0]) < int(arr[j].split(' ')[0]):
                            temp = arr[i]
                            arr[i] = arr[j]
                            arr[j] = temp
                return arr
            
            # parses each card list into the insertion sort function
            spade = insertion_sort(spade)
            heart = insertion_sort(heart)
            club = insertion_sort(club)
            diamond = insertion_sort(diamond)

        elif sortingType == "merge sort":
            # merge sort code here
            pass
        elif sortingType == "quick sort":
            # quick sort code here
            pass
        else:
            print("Invalid sorting type, please try again")
        
        def redoCards(temp): # replaces the numbers back to their face values
            # 1 = ace, 11 = jack, 12 = queen, 13 = king
            for i in range(len(temp)):
                if temp[i].split(" ")[0] == "1":
                    temp[i] = f"ace {temp[i].split(' ')[1]} {temp[i].split(' ')[2]}" 
                if temp[i].split(" ")[0] == "11":
                    temp[i] = f"jack {temp[i].split(' ')[1]} {temp[i].split(' ')[2]}"
                if temp[i].split(" ")[0] == "12":
                    temp[i] = f"queen {temp[i].split(' ')[1]} {temp[i].split(' ')[2]}"
                if temp[i].split(" ")[0] == "13":
                    temp[i] = f"king {temp[i].split(' ')[1]} {temp[i].split(' ')[2]}"
            return temp
        
        spade = redoCards(spade)
        heart = redoCards(heart)
        club = redoCards(club)
        diamond = redoCards(diamond)

        tempDeck = []
        for i in spade:
            tempDeck.append(i)
        for i in heart:
            tempDeck.append(i)
        for i in club:
            tempDeck.append(i)
        for i in diamond:
            tempDeck.append(i)
        
        return tempDeck # returns the sorted deck

###########################################################################################################

    def set_deck(self, newDeck):
        """this method makes the deck equal to the newDeck provided"""
        self.deck = newDeck

###########################################################################################################

    def shuffle(self):
        """shuffles the deck of cards"""
        # below I used the fisher yates method of shuffling a deck of cards
        shuffled = []
        while self.deck:
            k = randint(0, len(self.deck) - 1)
            shuffled.append(self.deck[k])
            self.deck.pop(k)
        self.deck = shuffled

###########################################################################################################

    def __str__(self): # this method overwrites the default __str__ method to instead return the string below
        return f"{self.deck}" # returns the deck as a string

class HandAssignment:
    """
    This is the class that handles all operations that related to assigning a hand type to the hand dealt to the user.
    A brief description of the methods:

    __init__: Initializes the HandAssignment class and sets up the hand attribute.
    hand_detection: Detects and assigns the poker hand type for a given hand of cards.
        - rank_value: Extracts the rank value of a card (e.g., 'king' => 13, '5' => 5).
        - suit: Extracts the suit of a card (e.g., 'hearts', 'clubs').
        - count_ranks: Counts how many times each rank appears in the hand.
        - check_flush: Checks if all cards are of the same suit.
        - check_straight: Checks if the hand is a straight (consecutive values).
        - hand_assignment: Determines the poker hand category based on the hand.
    """

    def __init__(self):
        self.hand = hand
    
    # Hand detection
    def hand_detection(self, hand):
        # Extract the rank value of a card (e.g., 'king' => 13, '5' => 5)
        def rank_value(card):
                face = card.split()[0]
                face_cards = {"ace": 14, "jack": 11, "queen": 12, "king": 13}
                if face in face_cards:
                    return face_cards[face]
                elif face.isdigit():
                    return int(face)
                else:
                    print(f"Unrecognized card face: {face}")

       # Extract the suit of a card (e.g., 'hearts', 'clubs') 
        def suit(card):
            return card.split()[-1]
        
        # Count how many times each rank appears in the hand
        def count_ranks(cards):
            counts = {}
            for card in self.hand:
                val = rank_value(card)
                counts[val] = counts.get(val, 0) + 1
            return counts
        
        # Check if all cards are of the same suit
        def check_flush(cards):
            suits = [suit(card) for card in self.hand]
            return len(set(suits)) == 1
        
         # Check if the hand is a straight (consecutive values)
        def check_straight(cards):
            values = sorted([rank_value(card) for card in self.hand])
            if len(values) < 5:
                return False
            elif values == [2, 3, 4, 5, 14]:
                return True
            return all(values[i] - values[i-1] == 1 for i in range(1,5))
        
        # Determine the poker hand category
        def hand_assignment(cards):
            counts = count_ranks(cards)
            freq = sorted(counts.values(), reverse=True) #remember to ask mistah agusto about sort
            is_flush = check_flush(cards)
            is_straight = check_straight(cards)
            values = sorted([rank_value(card) for card in self.hand])

            if is_flush and values == [10, 11, 12, 13, 14]:
                return "Royal Flush"
            
            if is_flush and is_straight:
                return "Straight Flush"
            
            if freq == [4, 1]:
                return "Four of a Kind"
            
            if freq == [3, 2]:
                return "Full House"
            
            if is_flush:
                return "Flush"

            if is_straight:
                return "Straight"
            
            if freq == [3, 1, 1]:
                return "Three of a Kind"
            
            if freq == [2, 2, 1]:
                return "Two Pair"

            if freq == [2, 1, 1, 1]:
                return "One Pair"
            
            else:
                return "No valid poker hand has been given"
            
        result = hand_assignment(self.hand)
        print(f"Detected hand: {result}")

my_hand = GameDeck() # makes a new object of the GameDeck class

# my_hand.count_suit("hearts")
# print(my_hand)
my_hand.shuffle()
# print(my_hand)
# tem = my_hand.deal_cards(5)
# print(my_hand)
# print(tem)
# my_hand.rejoin(tem)
print(my_hand)
print()
tem = my_hand.sort_cards(None)
my_hand.set_deck(tem)
print(my_hand)


# hand = my_hand.deal_cards(5)
# print("Dealt hand:", hand)
# HandAssignment.hand_detection(hand)