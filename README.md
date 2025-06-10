## 1 Introduction

This report will go into the details of our poker project, and the process behind
the decisions made during development.

## 2 Classes & Major Functions

There are three classes in the Python file:
- GameDeck
- HandAssignment
- PokerGame
GameDeck is the class that handles all operations regarding the sorting of the
cards, while HandAssignment handles the functions that aid in detecting the
poker hand type in the user’s hand. Finally, the PokerGame class tracks the
statistics of the game, such as how many times a hand type is drawn, and displays it when prompted.
The classes are displayed in the order given above, from the most complex
and important to the least.
Finally, we have the main game loop, which is a while loop that keeps on going
until the user prompts to exit, displaying the statistics of the game alonsgide a
goodbye message.
Arguably the most important function in the program is the sort cards function, which, as the name implies, sorts the cards using the sorting method of
the user’s choice, with the options being:
- Binary Insertion Sort
- Heapsort
- Merge Sort
- Quick Sort
There is also the hand detection function, which is essentially the entire HandAssignment class in a single function. It contains sub-functions that are essen1
tial to determining the user’s hand, such as functions that determine whether a
hand is straight, a flush, as well as the suits of the cards. The most important
sub-function, in my opinion, is the final function, called hand assignment. As
the name implies, it puts all of the previous functions together to determine the
user’s hand.

## 3 Analysis of the HandAssignment Class

The class HandAssigment is responsible for finding the different poker hands.
Inside, there are two methods, init and hand detection, the former being the
constructor and the latter being the one that actually does any sort of work.
Inside it, there are 8 functions:
- manual sort: which is a simple bubble sort implementation, with a complexity
of 0(n²) for all cases. - rank value: this function extracts the rank value of an
individual card, which has a complexity of O(1) for all cases.
- suit: this function extracts the suit of a card, which has a complexity of O(1).
- count ranks: this function counts how many times a rank is present in a hand,
having a complexity of O(n) of all cases.
- check flush: this function checks if all cards are in the same suit, and has a
complexity of O(n) for all cases.
- check straight: this function checks if the hand is a straight, and if so, uses
a if to analyze if the straight is a wheel (A-2-3-4-5), and also uses a for loop
with an if statement inside of the function to analyse if the straight is a normal
straight. This function has a complexity of O(n2
) for all cases.
- combinations: this function manually generates all possible combinations of r
elements from an iterable, used for evaluating larger hands. This function has
a complexity of O(C(n,r)) where C(n,r) is the binomial coefficient.
- evaluate 5 card hand: this function evaluates a standard 5-card poker hand
and determines its type (Royal Flush, Straight Flush, Four of a Kind, etc.). It
has a complexity of O(n²) for all cases.
- find best hand from many: this function finds the best possible 5-card hand
from a larger set of cards by generating all combinations and evaluating each
one. This function has a complexity of O(C(n,5) × n²) where n is the number
of cards.
HandAssigement has an overall time complexity of O(n5) for hands with
more than 5 cards, O(n²) for exactly 5 cards, and O(n) for fewer than 5 cards.
For hands with more than 5 cards, the function generates C(n,5) combinations
which is O(n), and since this dominates the O(n²) evaluation of each combination, the overall complexity is O(n5). (O(1) < O(n) < O(n2) < O(n5))).
2

## 4 Decisions Made During Development

One of the many issues during development was finding a way to sort the cards
to fit the criterion of storing as strings of text instead of numbers for the sake of
readability. We solved this issue by splitting the string into lists and checking
the first index of the list and sorting that value by converting it to an integer.
In the case that they were not numbers, they were assigned a numerical value
and then sorted (Ace as 1, Jack as 11, Queen as 12, King as 13).
For the additional sorting method, we chose the quick sort as it was the
simplest to implement that fit the criteria, being of O(n log n) complexity.

## 5 Expected Behaviour of The Sorting Algorithms

Heapsort
Heapsort is an in-place, non-stable sorting algorithm with a time complexity of
O(n log n). It is robust for larger datasets, but for small lists such as a single
suit (13 cards), its advantages are less pronounced.
Binary Insertion Sort
This algorithm improves upon standard insertion sort by using binary search to
find the correct insertion point, reducing the number of comparisons. Its time
complexity is O(n²) in the worst case, but for small or nearly sorted lists, it is
very efficient and straightforward.
Merge Sort
Merge sort is a stable, divide-and-conquer algorithm with a consistent O(n log
n) time complexity. It requires additional memory for merging, but for small
lists, the overhead is minimal.
Quick Sort
Quick sort is an in-place, non-stable algorithm with an average time complexity
of O(n log n), but a worst-case of O(n²). It is generally fast for random data,
such as a shuffled deck, but its recursive nature can introduce overhead for small
lists.
Given that the sorting is performed on small lists typically and, since we
split the deck into it’s individual suits which are 13 cards per suit, all four
algorithms will execute quickly. However, binary insertion sort is likely to be
the most efficient in practice for this context due to its simplicity and low
overhead. For larger datasets, merge sort or heapsort would be preferable due
to their predictable performance.

## 6 The GUI

We have implemented a GUI that allows the user to interact with the program
instead of having to type out prompts. Below is a sreenshot of what the GUI
looks like:

![image](https://github.com/user-attachments/assets/221c696a-f083-4284-9465-000bf4210759)

Figure 1: Screenshot of thee GUI
The GUI uses tkinter as the framework, which is imported at the beginning
of the program. Specifically, messagebox, simpledialog and scrolledtext are the
packages from tkinter we use in this program.

## 7 How To Run The Project

All of the code is self-contained in pokerProject.py. Running that file will run
the program.
