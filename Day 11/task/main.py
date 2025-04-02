import random

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def deal_cards(cards):
    p_hand = []
    d_hand = []
    # add cards to player and dealers hands and remove cards from cards list
    for i in range(0,2):
        p_hand.append(draw_card(cards))
        d_hand.append(draw_card(cards))
    return p_hand, d_hand

    # return player_hand and dealer_hand

def draw_card(deck):
    card_index = random.randint(0,len(deck)-1)
    card = deck[card_index]
    deck.pop(card_index)
    return card

def check_ace_value(hand, hand_score):
    if 11 in hand and hand_score > 21:
        hand.remove(11)
        hand.append(1)
    elif 1 in hand and hand_score < 11:
        hand.remove(1)
        hand.append(11)


def check_score(score1, score2):
    if score1 > 21 or score1 < score2:
        print("You lose")
        return True
    elif score1 == score2:
        print("It's a draw")
        return True
    elif score1 > score2:
        print("You win")
        return True





while play == 'y':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4


    player_hand, dealer_hand = deal_cards(cards)
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    check_ace_value(player_hand,player_score)
    check_ace_value(dealer_hand,dealer_score)
    print(f"Your cards: {player_hand}")
    print(f"Computer's first card: {dealer_hand[0]}")
    next_card = input("Type 'y' to get another card, type 'n to pass: ")
    winner = False
    while winner == False or next_card =='y':
        if next_card == 'y':
            player_hand.append(draw_card(cards))
            if dealer_score < 17:
                dealer_hand.append(draw_card(cards))
            check_ace_value(player_hand, player_score)
            check_ace_value(dealer_hand, dealer_score)
            player_score = sum(player_hand)
            dealer_score = sum(dealer_hand)
            print(f"Your cards: {player_hand}")
            print(f"Computer's first card: {dealer_hand[0]}")
            if player_score > 21:
                winner = check_score(player_score, dealer_score)
                next_card = 'n'
            else:
                next_card = input("Type 'y' to get another card, type 'n to pass: ")

        else:
            winner =check_score(player_score,dealer_score)


    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")