import random
import art

def deal_cards(cards):
    """Creates lists of cards that are the player's and dealer's hands."""
    p_hand = []
    d_hand = []
    # add cards to player and dealers hands and remove cards from cards list
    for i in range(0,2):
        p_hand.append(draw_card(cards))
        d_hand.append(draw_card(cards))
    return p_hand, d_hand

    # return player_hand and dealer_hand

def draw_card(deck):
    """Draws and individual card from deck"""
    card_index = random.randint(0,len(deck)-1)
    card = deck[card_index]
    # drawing without replacement
    deck.pop(card_index)
    return card

def check_ace_value(hand):
    """Checks to see which value of the ace face card to use depending on score."""
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    elif 1 in hand and sum(hand) < 11:
        hand.remove(1)
        hand.append(11)


def check_result(score1, score2):
    """ Checks the result of the game"""
    if score1 > 21:
        print(f"You went over.")
        print("You lose")
        return True
    elif score1 < score2:
        print(f"Your cards: {player_hand}")
        print(f"Computer's cards: {player_hand}")
        print("You lose")
        return True
    elif score1 == score2:
        print(f"Your cards: {player_hand}")
        print(f"Computer's cards: {player_hand}")
        print("It's a draw")
        return True
    elif score1 > score2:
        print(f"Your cards: {player_hand}")
        print(f"Computer's cards: {player_hand}")
        print("You win")
        return True


print(art.logo)

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#loops through games of blackjack
while play == 'y':
    # initializes a deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    # sets up the players hands
    player_hand, dealer_hand = deal_cards(cards)

    check_ace_value(player_hand)
    check_ace_value(dealer_hand)
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    # Displays relevant hand information
    print(f"Your cards: {player_hand}")
    print(f"Computer's first card: {dealer_hand[0]}")

    next_card = input("Type 'y' to get another card, type 'n to pass: ")
    winner = False

    # Checks condition for continue game
    # if there is a winner then the game stops or if the player doesn't want to draw anymore cards
    while winner == False or next_card =='y':
        if next_card == 'y':

            # players draw cards
            player_hand.append(draw_card(cards))
            if dealer_score < 17:
                dealer_hand.append(draw_card(cards))



            check_ace_value(player_hand)
            check_ace_value(dealer_hand)
            player_score = sum(player_hand)
            dealer_score = sum(dealer_hand)


            if player_score > 21:
                winner = check_result(player_score, dealer_score)
                next_card = 'n'
            else:
                print(f"Your cards: {player_hand}")
                print(f"Computer's first card: {dealer_hand[0]}")
                next_card = input("Type 'y' to get another card, type 'n to pass: ")

        else:
            winner =check_result(player_score, dealer_score)


    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")