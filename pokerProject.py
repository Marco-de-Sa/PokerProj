from random import randint

class GameDeck:
    """
    This is the class that handles all operations that the deck of cards will need to undertake.
    The code that handles the hand of the player will most likely be in a different area.
    A brief description of the methods:

    __init__: will be automatically used on a new object of this class being made
    count_suit: counts the number of cards belonging to a specific suit that remain in the deck
    rejoin: will take a list provided and rejoin them into the deck
    deal_cards: deals out the specified number of cards in list form
    sort_deck: allows the user to sort the deck of cards in a specific order using a sorting algorithm chosen by the user
    shuffle: shuffles the deck of cards using the fisher yates method
    __str__: this method overwrites the default __str__ method to instead return the string below
            this is used to print out the deck of cards in a string format

    """
    def __init__(self):
        # declares a list called deck that holds every type of card
        self.deck = ['ace of clubs', 'ace of spades', 'ace of hearts', 'ace of diamonds', '2 of clubs', '2 of spades', '2 of hearts', '2 of diamonds', '3 of clubs', '3 of spades', '3 of hearts', '3 of diamonds', '4 of clubs', '4 of spades', '4 of hearts', '4 of diamonds', '5 of clubs', '5 of spades', '5 of hearts', '5 of diamonds', '6 of clubs', '6 of spades', '6 of hearts', '6 of diamonds', '7 of clubs', '7 of spades', '7 of hearts', '7 of diamonds', '8 of clubs', '8 of spades', '8 of hearts', '8 of diamonds', '9 of clubs', '9 of spades', '9 of hearts', '9 of diamonds', '10 of clubs', '10 of spades', '10 of hearts', '10 of diamonds', 'jack of clubs', 'jack of spades', 'jack of hearts', 'jack of diamonds', 'queen of clubs', 'queen of spades', 'queen of hearts', 'queen of diamonds', 'king of clubs', 'king of spades', 'king of hearts', 'king of diamonds']

    def rejoin(self, hand):
        """this method joins a given list onto the card deck in the class"""
        self.deck.extend(hand)
        hand.clear()

    def deal_cards(self, card_count):
        """returns the specified amount of cards"""
        temp = [] # creates a temporary list
        for i in range(int(card_count)): # converts car_count to an integer and then iterates throughout it
            temp.append(self.deck.pop()) # appends the specified amount(from card_count) to the temp list by popping them from the deck
        return temp # returns the temp list

    def sort_cards(self, optional):
        """
        this method sorts the deck of cards in a specific order using a sorting algorithm chosen by the user. Leave optional as None to sort the entire deck.
        The sorting algorithms available are heapsort, binary insertion, merge sort and quick sort.
        """

        tempDeck = [] # creates a temporary list
        if optional != None:
            tempDeck = optional.copy() # makes a copy of the optional list to sort
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
        
        sortingType = input("What type of sorting would you like to use?\n- heapsort\n- binary insertion\n- merge sort\n- quick sort\n")

        if sortingType.lower() == "heapsort":
            def heapify(arr, n, i):
                # Initialize largest as root
                largest = i 
                l = 2 * i + 1 
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
                """function to perform heap sort where arr is the list to be sorted"""
                n = len(arr)
                # Build heap (rearranges the array into a heap)
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

        elif sortingType.lower() == "binary insertion":
            def binary_search(arr, val, start, end):
                """performs a binary search on the array to find the correct index to insert the value"""
                if start == end:
                    if int(arr[start].split(" ")[0]) > int(val.split(" ")[0]):
                        return start
                    else:
                        return start+1

                if start > end:
                    return start

                mid = (start+end)//2
                if int(arr[mid].split(" ")[0]) < int(val.split(" ")[0]):
                    return binary_search(arr, val, mid+1, end)
                elif int(arr[mid].split(" ")[0]) > int(val.split(" ")[0]):
                    return binary_search(arr, val, start, mid-1)
                else:
                    return mid


            def insertion_sort(arr):
                """performs an insertion sort on the array"""
                for i in range(1, len(arr)):
                    val = arr[i]
                    j = binary_search(arr, val, 0, i-1)
                    arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
                return arr
            
            # parses each card list into the insertion sort function
            spade = insertion_sort(spade)
            heart = insertion_sort(heart)
            club = insertion_sort(club)
            diamond = insertion_sort(diamond)

        elif sortingType.lower() == "merge sort":
            def merge(arr, left, mid, right):
                n1 = mid - left + 1 # gets left half of the array
                n2 = right - mid # gets right half of the array

                # Create temp arrays
                L = [0] * n1
                R = [0] * n2

                # copies subsections of the array into temp arrays
                for i in range(n1):
                    L[i] = arr[left + i]
                for j in range(n2):
                    R[j] = arr[mid + 1 + j]

                i = 0  # starting index of first subarray
                j = 0  # starting index of second subarray
                k = left  # starting index of merged subarray

                # Merge the temp arrays back into arr
                while i < n1 and j < n2:
                    if int(L[i].split(" ")[0]) <= int(R[j].split(" ")[0]):
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # Copy the remaining elements of L
                while i < n1:
                    arr[k] = L[i]
                    i += 1
                    k += 1

                # Copy the remaining elements of R
                while j < n2:
                    arr[k] = R[j]
                    j += 1
                    k += 1

            def merge_sort(arr, left, right):
                if left < right:
                    mid = (left + right) // 2

                    merge_sort(arr, left, mid)
                    merge_sort(arr, mid + 1, right)
                    merge(arr, left, mid, right)
                    
            merge_sort(heart, 0, len(heart) - 1)
            merge_sort(spade, 0, len(spade) - 1)
            merge_sort(club, 0, len(club) - 1)
            merge_sort(diamond, 0, len(diamond) - 1)

        elif sortingType.lower() == "quick sort":
            def partition(arr, low, high):
                """this function partitions the array into two parts"""
                pivot = arr[high]
    
                i = low - 1

                for j in range(low, high):
                    if int(arr[j].split(" ")[0]) < int(pivot.split(" ")[0]):
                        i += 1
                        swap(arr, i, j)
    
                swap(arr, i + 1, high)
                return i + 1

            def swap(arr, i, j):
                """this function swaps two elements in the array"""
                arr[i], arr[j] = arr[j], arr[i]

            def quickSort(arr, low, high):
                """this function sorts the array using the quick sort algorithm"""
                if low < high:
                    parind = partition(arr, low, high)

                    quickSort(arr, low, parind - 1)
                    quickSort(arr, parind + 1, high)
            
            quickSort(spade, 0, len(spade) - 1)
            quickSort(heart, 0, len(heart) - 1)
            quickSort(club, 0, len(club) - 1)
            quickSort(diamond, 0, len(diamond) - 1)

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

    def set_deck(self, newDeck):
        """this method makes the deck equal to the newDeck provided"""
        self.deck = newDeck

    def shuffle(self):
        """shuffles the deck of cards"""
        # below I used the fisher yates method of shuffling a deck of cards
        shuffled = []
        while self.deck:
            k = randint(0, len(self.deck) - 1)
            shuffled.append(self.deck[k])
            self.deck.pop(k)
        self.deck = shuffled

    def __str__(self):
        """this method overwrites the default __str__ method to instead return the string below"""
        return f"{self.deck}" # returns the deck as a string

class HandAssignment:
    """
    This is the class that handles all operations that related to assigning a hand type to the hand dealt to the user.
    A brief description of the methods:

    __init__: Initializes the HandAssignment class and sets up the hand attribute.
    hand_detection: Detects and assigns the poker hand type for a given hand of cards.
        - manual_sort: Sorts the hand using a simple bubble sort algorithm.
        - rank_value: Extracts the rank value of a card (e.g., 'king' => 13, '5' => 5).
        - suit: Extracts the suit of a card (e.g., 'hearts', 'clubs').
        - count_ranks: Counts how many times each rank appears in the hand.
        - check_flush: Checks if all cards are of the same suit.
        - check_straight: Checks if the hand is a straight (consecutive values).
        - hand_assignment: Determines the poker hand category based on the hand.
    """

    def __init__(self, hand):
        self.hand = hand

    def hand_detection(self):
        # Manual sort function
        def manual_sort(arr):
            # Simple bubble sort implementation
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        def rank_value(card):
            # Extract the rank value of a card
            face = card.split()[0]
            face_cards = {"ace": 14, "jack": 11, "queen": 12, "king": 13}
            if face in face_cards:
                return face_cards[face]
            elif face.isdigit():
                return int(face)
            else:
                print(f"Unrecognized card face: {face}")
                return 0

        def suit(card):
            # Extract the suit of a card
            return card.split()[-1]

        def count_ranks(cards):
            # Count how many times each rank appears in the hand
            counts = {}
            for card in cards:
                val = rank_value(card)
                counts[val] = counts.get(val, 0) + 1
            return counts

        def check_flush(cards):
            # Check if all cards are of the same suit
            suits = [suit(card) for card in cards]
            first_suit = suits[0]
            for i in suits:
                if i != first_suit:
                    return False
            return True

        def check_straight(cards):
            # Check if the hand is a straight
            values = [rank_value(card) for card in cards]
            values = manual_sort(values)
            
            # Straight must have 5 unique values
            if len(values) < 5:
                return False
            
            # Check for A-2-3-4-5 straight (wheel)
            if values == [2, 3, 4, 5, 14]:
                return True
            
            # Check for normal straight
            for i in range(1, len(values)):
                if values[i] - values[i-1] != 1:
                    return False
            return True

        def hand_assignment(cards):
            counts = count_ranks(cards)
            freq = list(counts.values())
            freq = manual_sort(freq)
            freq.reverse()  # Sort in descending order
            
            is_flush = check_flush(cards)
            is_straight = check_straight(cards)
            values = [rank_value(card) for card in cards]
            values = manual_sort(values)

            # Royal Flush check
            if is_flush and values == [10, 11, 12, 13, 14]:
                return "Royal Flush", "Flush"

            # Straight Flush check
            if is_flush and is_straight:
                return "Straight Flush", "Flush", "Straight"
            
            # Four of a Kind check
            if freq == [4, 1]:
                return "Four of a Kind"

            # Full House check
            if freq == [3, 2]:
                return "Full House"

            # Flush check
            if is_flush:
                return "Flush"

            # Straight check
            if is_straight:
                return "Straight"

            # Three of a Kind check
            if freq == [3, 1, 1]:
                return "Three of a Kind"

            # Two Pair check
            if freq == [2, 2, 1]:
                return "Two Pair"

            # One Pair check
            if freq == [2, 1, 1, 1]:
                return "One Pair"

            # High Card check
            return "High Card"

        result = hand_assignment(self.hand)
        print(f"Detected hand: {result}")
        return result
    
class PokerGame:
    """
    Class to track poker game statistics and handle multiple hands
    __init__: will be automatically used on a new object of this class being made
    add_hand_result: Adds a hand result to the statistics.
    show_statistics: Displays the statistics of the poker game.
    self.hand_counts: Dictionary to keep track of the count of each hand type.
    self.current_hand: List to store the current hand of cards.
    """
    def __init__(self):
        self.hand_counts = {
            "Royal Flush": 0,
            "Straight Flush": 0,
            "Four of a Kind": 0,
            "Full House": 0,
            "Flush": 0,
            "Straight": 0,
            "Three of a Kind": 0,
            "Two Pair": 0,
            "One Pair": 0,
            "High Card": 0
        }
        self.current_hand = []
    
    # Add hand result to the statistics
    def add_hand_result(self, hand_type):
        if hand_type in self.hand_counts:
            self.hand_counts[hand_type] += 1
    
    def show_statistics(self):
        print("\n==== Poker Game Statistics ====")
        total_hands = sum(self.hand_counts.values())
        if total_hands == 0:
            print("No hands played yet.")
            print()
            return
        
        for hand_type, count in self.hand_counts.items():
            percentage = (count/total_hands) * 100
            print(f"{hand_type}: {count} ({percentage:.1f}%)")
        print(f"Total hands played: {total_hands}")
        print("=" * 30 + "\n")


my_hand = GameDeck() # Makes a new object of the GameDeck class
poker_game = PokerGame() # Makes a new object of the PokerGame class

my_hand.shuffle() # Shuffles the deck of cards at the start of the game
# Main game loop
while True:
    question = input("Do you want to:\n- Draw cards\n- Draw poker hand (5 cards)\n- Show statistics\n- Show deck size\n- Shuffle deck\n- Sort deck\n- Rejoin cards to the deck\n- Exit\n").lower()
    if question == "draw cards":
        try:
            # Ask the user how many cards they want to draw
            num = int(input("Input the number of cards you want to draw: "))
            # Validate the input number
            # If the number is less than or equal to 0, prompt for a valid number
            if num <= 0:
                print("Please enter a number above zero.")
                continue   
            # If the number is greater than the number of cards in the deck, prompt for a valid number      
            elif num > len(my_hand.deck):
                print(f"Not enough cards in deck! Only {len(my_hand.deck)} cards remaining.")
                continue

            # Deal the specified number of cards
            drawn_cards = my_hand.deal_cards(num)
            print(f"You drew: {drawn_cards}")

            # Store current hand for potential return
            poker_game.current_hand.extend(drawn_cards)

            # If # of cards drawn are exactly 5 cards, offer to assign a hand type
            if num == 5:
                analyze = input("Would you like to analyze this as a poker hand? (y/n): ").lower()
                if analyze == 'y':
                    hand_checker = HandAssignment(drawn_cards)
                    hand_type = hand_checker.hand_detection()
                    poker_game.add_hand_result(hand_type)
    
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")

    elif question == "draw poker hand" or question == "draw poker hand (5 cards)":
        #If the length of the deck is less than 5, we cannot draw a poker hand
        if len(my_hand.deck) < 5:
            print(f"Not enough cards in deck for a poker hand! Only {len(my_hand.deck)} cards remaining.")
            continue

        #Draw 5 cards
        drawn_cards = my_hand.deal_cards(5)
        print(f"Your poker hand: {drawn_cards}")

        # Store current hand for potential return
        poker_game.current_hand = drawn_cards.copy()

        # Automatically assign a hand type
        hand_checker = HandAssignment(drawn_cards)
        hand_type = hand_checker.hand_detection()
        poker_game.add_hand_result(hand_type)

    elif question == "shuffle deck":
        # Shuffle the deck using the shuffle method
        my_hand.shuffle()
        print("\nDeck has been shuffled!\n")
        print(f"Shuffled deck: {my_hand}\n")

    elif question == "sort deck":
        # Check if there are cards in the deck to sort
        # If the deck is empty, we cannot sort it
        if len(my_hand.deck) == 0:
            print("No cards in deck to sort!")
            continue
        sorted_deck = my_hand.sort_cards(None)
        my_hand.set_deck(sorted_deck)  # Update the deck with the sorted cards
        if sorted_deck:
            print("Deck has been sorted!")
            print(f"Sorted deck: {sorted_deck}\n")
    
    elif question == "show deck size":
        # Display the size of the deck and current hand
        print(f"Cards remaining in deck: {len(my_hand.deck)}")
        if len(poker_game.current_hand) > 0:
            print(f"Cards in your current hand: {len(poker_game.current_hand)}")
    
    elif question == "rejoin cards to the deck":
        # Checks if there are cards in the current hand to rejoin
        if len(poker_game.current_hand) == 0:
            print("No cards in current hand to rejoin to the deck.")
        else:
            # Rejoin the current hand to the deck
            my_hand.rejoin(poker_game.current_hand)
            poker_game.current_hand.clear()
            print("Current hand has been rejoined to the deck.")

    elif question == "show statistics":
        # Display the statistics of the poker game
        poker_game.show_statistics()
        
    elif question == "exit":
        # Exit the game and show final statistics
        print("\nFinal game statistics:")
        poker_game.show_statistics()
        print("Exiting the game. Thanks for playing! Goodbye!")
        break
    else:
        # Handle invalid input
        print("Invalid option, please try again.")