from collections import deque

def shuffle_cards(cards):
    # Okay, so first I’ll initialize a deque for efficient top/bottom operations.
    new_pile = deque()
    put_under = False  # This flag will help me alternate between under/top placements.

    # While there are still cards in the original pile
    while cards:
        # Take the top card (front of the list)
        card = cards.pop(0)
        
        if not new_pile:
            # First card simply starts the new pile
            new_pile.append(card)
        else:
            if put_under:
                # If the flag says put under → append to the bottom
                new_pile.append(card)
            else:
                # Otherwise → put on top
                new_pile.appendleft(card)
        
        # Flip the flag for next iteration
        put_under = not put_under

    # Return as a normal list for readability
    return list(new_pile)


# Example test
print(shuffle_cards(["Ace of Spades", "2 of Hearts", "3 of Clubs", "4 of Diamonds"]))
# Expected: ['3 of Clubs', 'Ace of Spades', '2 of Hearts', '4 of Diamonds']
