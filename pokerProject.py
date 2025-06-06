from random import randint
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

"""
This is the main file for the poker game project. It has a gui in the class called PokerGUI and it
contains the GameDeck class which handles the deck of cards and the HandAssignment class which handles the hand of cards.
"""

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

    def sort_cards(self, sortingType):
        """
        this method sorts the deck of cards in a specific order using a sorting algorithm chosen by the user.
        The sorting algorithms available are heapsort, binary insertion, merge sort and quick sort.
        """
        tempDeck = [] # creates a temporary list
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

        if sortingType.lower() == "heapsort":
            def heapify(arr, n, i):
                largest = i 
                l = 2 * i + 1 
                r = 2 * i + 2  
                if l < n and int(arr[l].split(" ")[0]) > int(arr[largest].split(" ")[0]):
                    largest = l
                if r < n and int(arr[r].split(" ")[0]) > int(arr[largest].split(" ")[0]):
                    largest = r
                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    heapify(arr, n, largest)

            def heapSort(arr):
                n = len(arr)
                for i in range(n // 2 - 1, -1, -1):
                    heapify(arr, n, i)
                for i in range(n - 1, 0, -1):
                    arr[0], arr[i] = arr[i], arr[0]
                    heapify(arr, i, 0)

            heapSort(spade)
            heapSort(heart)
            heapSort(club)
            heapSort(diamond)

        elif sortingType.lower() == "binary insertion":
            def binary_search(arr, val, start, end):
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
                for i in range(1, len(arr)):
                    val = arr[i]
                    j = binary_search(arr, val, 0, i-1)
                    arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
                return arr
            
            spade = insertion_sort(spade)
            heart = insertion_sort(heart)
            club = insertion_sort(club)
            diamond = insertion_sort(diamond)

        elif sortingType.lower() == "merge sort":
            def merge(arr, left, mid, right):
                n1 = mid - left + 1
                n2 = right - mid
                L = [0] * n1
                R = [0] * n2
                for i in range(n1):
                    L[i] = arr[left + i]
                for j in range(n2):
                    R[j] = arr[mid + 1 + j]
                i = 0
                j = 0
                k = left
                while i < n1 and j < n2:
                    if int(L[i].split(" ")[0]) <= int(R[j].split(" ")[0]):
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < n1:
                    arr[k] = L[i]
                    i += 1
                    k += 1
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
                pivot = arr[high]
                i = low - 1
                for j in range(low, high):
                    if int(arr[j].split(" ")[0]) < int(pivot.split(" ")[0]):
                        i += 1
                        swap(arr, i, j)
                swap(arr, i + 1, high)
                return i + 1

            def swap(arr, i, j):
                arr[i], arr[j] = arr[j], arr[i]

            def quickSort(arr, low, high):
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
        - combinations: Generates all possible combinations of cards.
        - evaluate_5_card_hand: Evaluates a standard 5-card poker hand.
        - find_best_hand_from_many: Finds the best possible 5-card hand from a larger set of cards.
        - evaluate_partial_hand: Evaluates hands with less than 5 cards.
        - log: Helper method to output messages either to GUI or console.
        - hand_detection: Main method to detect the type of poker hand based on the cards in the hand.
    """

    def __init__(self, hand, output_callback=None):
        self.hand = hand
        self.output_callback = output_callback
    
    def _log(self, message):
        # Helper method to output messages either to GUI or console
        # This allows for flexibility in how messages are displayed.
        if self.output_callback:
            self.output_callback(message)
        else:
            print(message)

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
                self._log(f"Unrecognized card face: {face}")
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
            # Check if all cards are of the same suit (only for exactly 5 cards)
            if len(cards) != 5:
                return False
            suits = [suit(card) for card in cards]
            first_suit = suits[0]
            for i in suits:
                if i != first_suit:
                    return False
            return True

        def check_straight(cards):
            # Check if the hand is a straight (only for exactly 5 cards)
            if len(cards) != 5:
                return False

            values = [rank_value(card) for card in cards]
            values = manual_sort(list(set(values)))  # Remove duplicates and sort

            # Need exactly 5 unique values for a straight
            if len(values) != 5:
                return False

            # Check for A-2-3-4-5 straight (wheel) - Ace low
            if values == [2, 3, 4, 5, 14]:
                return True

            # Check for normal straight (consecutive values)
            for i in range(1, len(values)):
                if values[i] - values[i - 1] != 1:
                    return False
            return True

        def combinations(iterable, r):
            # Manual combinations function
            # Generates all combinations of r elements from the iterable
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = list(range(r))
            yield tuple(pool[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    if indices[i] != i + n - r:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i + 1, r):
                    indices[j] = indices[j - 1] + 1
                yield tuple(pool[i] for i in indices)

        def evaluate_5_card_hand(cards):
            # Standard 5-card poker hand evaluation
            counts = count_ranks(cards)
            freq = list(counts.values())
            freq = manual_sort(freq)
            freq.reverse()

            is_flush = check_flush(cards)
            is_straight = check_straight(cards)
            values = [rank_value(card) for card in cards]
            values = manual_sort(values)

            # Royal Flush check (highest priority)
            if is_flush and values == [10, 11, 12, 13, 14]:
                return "Royal Flush"

            # Straight Flush check
            if is_flush and is_straight:
                return "Straight Flush"

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
            
            # High Card check (default case)
            return "High Card"

        def find_best_hand_from_many(cards):
            # Find the best possible 5-card hand from a larger set
            best_hand = "High Card"
            best_rank = 10  # High Card is rank 10 (lowest)

            # Hand rankings for comparison (lower number = better hand)
            hand_rankings = {
                "Royal Flush": 1,
                "Straight Flush": 2,
                "Four of a Kind": 3,
                "Full House": 4,
                "Flush": 5,
                "Straight": 6,
                "Three of a Kind": 7,
                "Two Pair": 8,
                "One Pair": 9,
                "High Card": 10
            }

            self._log(f"Evaluating {len(cards)} cards to find the best 5-card hand...")
            combinations_checked = 0

            # Generate all possible 5-card combinations
            for combo in combinations(cards, 5):
                hand_type = evaluate_5_card_hand(list(combo))
                hand_rank = hand_rankings[hand_type]
                combinations_checked += 1

                if hand_rank < best_rank:
                    best_hand = hand_type
                    best_rank = hand_rank
                    self._log(f"New best hand found: {best_hand}")

                # If we found a Royal Flush, there's no need to check further
                if best_hand == "Royal Flush":
                    break

            self._log(f"Checked {combinations_checked} combinations. \nBest hand: {best_hand}")
            return best_hand

        def evaluate_partial_hand(cards):
            # Evaluate hands with less than 5 cards
            counts = count_ranks(cards)
            freq = list(counts.values())
            freq = manual_sort(freq)
            freq.reverse()

            pairs = freq.count(2)
            threes = freq.count(3)
            fours = freq.count(4)

            if fours >= 1:
                return "Four of a Kind"
            if threes >= 1 and pairs >= 1:
                return "Full House"
            if threes >= 1:
                return "Three of a Kind"
            if pairs >= 2:
                return "Two Pair"
            if pairs >= 1:
                return "One Pair"

            return "High Card"

        # Main evaluation logic
        if len(self.hand) == 5:
            result = evaluate_5_card_hand(self.hand)
        elif len(self.hand) > 5:
            result = find_best_hand_from_many(self.hand)
        else:
            result = evaluate_partial_hand(self.hand)
            
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

class PokerGUI:
    """
    This class handles the graphical user interface for the Poker game using Tkinter.
    It provides buttons for user actions and displays output in a scrolled text area.
    """

    def __init__(self, root, my_hand, poker_game):
        # Initialize the GUI with the main window, deck, and game statistics
        self.root = root
        self.my_hand = my_hand
        self.poker_game = poker_game

        root.title("Poker Game")

        # Output area for displaying messages to the user
        self.output = scrolledtext.ScrolledText(root, width=60, height=15, state='disabled')
        self.output.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Welcome message
        self.print_output("Welcome to the Poker Game!\nClick a button below to begin.")

        # Buttons for user actions
        tk.Button(root, text="Draw Cards", width=20, command=self.draw_cards).grid(row=1, column=0, pady=5)
        tk.Button(root, text="Draw Poker Hand", width=20, command=self.draw_poker_hand).grid(row=1, column=1, pady=5)
        tk.Button(root, text="Show Statistics", width=20, command=self.show_statistics).grid(row=1, column=2, pady=5)
        tk.Button(root, text="Show Deck Size", width=20, command=self.show_deck_size).grid(row=2, column=0, pady=5)
        tk.Button(root, text="Shuffle Deck", width=20, command=self.shuffle_deck).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Sort Deck", width=20, command=self.sort_deck).grid(row=2, column=2, pady=5)
        tk.Button(root, text="Rejoin Cards to Deck", width=20, command=self.rejoin_cards).grid(row=3, column=0, pady=5)
        tk.Button(root, text="Exit", width=20, command=self.exit_game).grid(row=3, column=2, pady=5)

    def print_output(self, text):
        """
        Print a message to the output area.
        """
        self.output.config(state='normal')
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.output.config(state='disabled')

    def draw_cards(self):
        """
        Draw a user-specified number of cards from the deck.
        Handles adding to the current hand and optionally analyzes a 5-card hand.
        """
        try:
            num = simpledialog.askinteger("Draw Cards", "How many cards do you want to draw?", minvalue=1)
            if num is None:
                return
            if num > len(self.my_hand.deck):
                self.print_output(f"Not enough cards in deck! Only {len(self.my_hand.deck)} cards remaining.")
                return

            drawn_cards = self.my_hand.deal_cards(num)
            self.print_output(f"You drew: {drawn_cards}")

            # Analyze the hand once
            hand_checker = HandAssignment(drawn_cards)
            hand_type = hand_checker.hand_detection()
            self.print_output(f"Detected hand: {hand_type}")

            # Pass the output callback to HandAssignment
            hand_checker = HandAssignment(drawn_cards, self.print_output)
            hand_type = hand_checker.hand_detection()

            # Handle tuple return (if your hand_detection still returns tuples)
            if isinstance(hand_type, tuple):
                hand_type = hand_type[0]

            # Add to statistics
            self.poker_game.add_hand_result(hand_type)

            # Handle current hand management
            if len(self.poker_game.current_hand) == 0:
                self.poker_game.current_hand.extend(drawn_cards)
            else:
                # If current_hand is not empty, ask user if they want to rejoin old hand to deck
                if messagebox.askyesno("Replace Hand?",
                                       "You already have cards in your hand. Do you want to return them to the deck and draw new cards?"):
                    self.my_hand.rejoin(self.poker_game.current_hand)
                    self.poker_game.current_hand.clear()
                    self.poker_game.current_hand.extend(drawn_cards)
                else:
                    # If not, just show the drawn cards but don't add to current_hand
                    self.print_output("You kept your previous hand. The new cards are not added to your hand.")

            # Only ask about additional analysis if it's exactly 5 cards AND user wants extra confirmation
            if num == 5:
                analyze = messagebox.askyesno("Analyze Hand",
                                              "Would you like to see detailed analysis of this poker hand?")
                if analyze:
                    # Don't re-analyze, just show more details about the already-detected hand
                    self.print_output(f"Detailed analysis: This is a {hand_type} hand.")

        except Exception as e:
            self.print_output(f"Error: {e}")

    def draw_poker_hand(self):
        """
        Draw a 5-card poker hand from the deck.
        Handles replacing the current hand and analyzes the hand type.
        """
        if len(self.my_hand.deck) < 5:
            self.print_output(f"Not enough cards in deck for a poker hand! Only {len(self.my_hand.deck)} cards remaining.")
            return
        # If current_hand is not empty, ask user if they want to rejoin old hand to deck
        if len(self.poker_game.current_hand) > 0:
            if messagebox.askyesno("Replace Hand?", "You already have cards in your hand. Do you want to return them to the deck and draw a new hand?"):
                self.my_hand.rejoin(self.poker_game.current_hand)
                self.poker_game.current_hand.clear()
            else:
                self.print_output("You kept your previous hand. No new hand was drawn.")
                return
        drawn_cards = self.my_hand.deal_cards(5)
        self.print_output(f"Your poker hand: {drawn_cards}")
        self.poker_game.current_hand = drawn_cards.copy()
        hand_checker = HandAssignment(drawn_cards, self.print_output)
        hand_type = hand_checker.hand_detection()
        self.print_output(f"Detected hand: {hand_type}")
        if isinstance(hand_type, tuple):
            hand_type = hand_type[0]
        self.poker_game.add_hand_result(hand_type)

    def show_statistics(self):
        """
        Display a window with the statistics of all poker hands played.
        """
        stats_win = tk.Toplevel(self.root)
        stats_win.title("Poker Game Statistics")
        stats_text = scrolledtext.ScrolledText(stats_win, width=40, height=15, state='normal')
        stats_text.pack(padx=10, pady=10)
        total_hands = sum(self.poker_game.hand_counts.values())
        if total_hands == 0:
            stats_text.insert(tk.END, "No hands played yet.\n")
        else:
            for hand_type, count in self.poker_game.hand_counts.items():
                percentage = (count / total_hands) * 100
                stats_text.insert(tk.END, f"{hand_type}: {count} ({percentage:.1f}%)\n")
            stats_text.insert(tk.END, f"Total hands played: {total_hands}\n")
        stats_text.config(state='disabled')

    def show_deck_size(self):
        """
        Show the number of cards remaining in the deck and in the current hand.
        """
        self.print_output(f"Cards remaining in deck: {len(self.my_hand.deck)}")
        if len(self.poker_game.current_hand) > 0:
            self.print_output(f"Cards in your current hand: {len(self.poker_game.current_hand)}")

    def shuffle_deck(self):
        """
        Shuffle the deck and display the shuffled deck.
        """
        self.my_hand.shuffle()
        self.print_output("Deck has been shuffled!")
        self.print_output(f"Shuffled deck: {self.my_hand}")

    def sort_deck(self):
        """
        Sort the deck using a user-selected sorting algorithm.
        Show a spinner animation for 5 seconds while sorting.
        """
        if len(self.my_hand.deck) == 0:
            self.print_output("No cards in deck to sort!")
            return

        # Ask for sorting method before starting spinner
        sortingType = simpledialog.askstring(
            "Sorting Algorithm",
            "What type of sorting would you like to use?\n- heapsort\n- binary insertion\n- merge sort\n- quick sort\n",
            parent=self.root
        )
        if sortingType is None or sortingType.strip().lower() not in ["heapsort", "binary insertion", "merge sort", "quick sort"]:
            self.print_output("Sorting cancelled or invalid sorting type.")
            return

        self._sortingType = sortingType

        spinner_chars = ['-', '/', '|', '\\']
        spinner_duration = 2500  # milliseconds
        spinner_interval = 100   # milliseconds
        spinner_steps = spinner_duration // spinner_interval
        self._spinner_index = 0
        self._spinner_count = 0

        def update_spinner():
            if self._spinner_count < spinner_steps:
                char = spinner_chars[self._spinner_index % len(spinner_chars)]
                self.output.config(state='normal')
                self.output.delete("end-2l", "end-1l")
                self.output.insert(tk.END, f"Sorting... {char}\n")
                self.output.see(tk.END)
                self.output.config(state='disabled')
                self._spinner_index += 1
                self._spinner_count += 1
                self.root.after(spinner_interval, update_spinner)
            else:
                self.output.config(state='normal')
                self.output.delete("end-2l", "end-1l")
                self.output.insert(tk.END, "Sorting... done!\n")
                self.output.config(state='disabled')
                sorted_deck = self.my_hand.sort_cards(self._sortingType)
                self.my_hand.set_deck(sorted_deck)
                if sorted_deck:
                    self.print_output("Deck has been sorted!")
                    self.print_output(f"Deck: {sorted_deck}")

        self.output.config(state='normal')
        self.output.insert(tk.END, "Sorting... -\n")
        self.output.config(state='disabled')
        update_spinner()

    def rejoin_cards(self):
        """
        Return the current hand to the deck.
        """
        if len(self.poker_game.current_hand) == 0:
            self.print_output("No cards in current hand to rejoin to the deck.")
        else:
            self.my_hand.rejoin(self.poker_game.current_hand)
            self.poker_game.current_hand.clear()
            self.print_output("Current hand has been rejoined to the deck.")

    def exit_game(self):
        """
        Show final statistics and exit the game after a short delay.
        """
        total_hands = sum(self.poker_game.hand_counts.values())
        if total_hands == 0:
            self.print_output("\nNo hands played. Exiting game.")
        else:
            self.print_output("\nFinal game statistics:")
            self.poker_game.show_statistics()
        self.root.after(1000, self.root.destroy)

# Launch the GUI
if __name__ == "__main__":
    my_hand = GameDeck()
    poker_game = PokerGame()
    my_hand.shuffle()
    root = tk.Tk()
    app = PokerGUI(root, my_hand, poker_game)
    root.mainloop()