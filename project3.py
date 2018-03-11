# Implement the codes from previous question for determining phase
from collections import defaultdict as dd
from itertools import combinations, permutations
# List of wild cards
WILD_CARDS = ['AS', 'AH', 'AD', 'AC']
# Assign integer value to each card value, not including wild cards
VALUE_ORDER = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
               '0': 8, 'J': 9, 'Q': 10, 'K': 11}
# Colour for each suit
COLOUR_DICT = {'H': 'red', 'D': 'red', 'S': 'black', 'C': 'black'}


def phasedout_group_1(group):
    '''Return 1 if the group satisfies type 1's requirement,
    otherwise return None'''
    value_count = dd(int)
    # Check the number of cards
    if len(group) != 3:
        return None

    # Counting values of the card set
    for card in group:
        if card in WILD_CARDS:
            value_count['wild_card'] += 1
        else:
            value_count[card[0]] += 1

    for value in value_count.copy().keys():
        # 3 natural cards with same value
        if value != 'wild_card' and value_count[value] == 3:
            return 1

        # 2 natural cards with same value + one wild card
        elif value_count['wild_card'] == 1 and value_count[value] == 2:
            return 1

    return None


def phasedout_phase_1(phase):
    '''Return 1 if the phase satisfies phase 1's requirement,
    otherwise return None'''

    # Check the number of groups
    if len(phase) != 2:
        return None

    # Check if each group of cards is group 1
    for card_set in phase:
        if not phasedout_group_1(card_set):
            return None
    return 1


def phasedout_group_2(group):
    '''Return 2 if the group satisfies type 2's requirement,
    otherwise return None'''

    suit_count = dd(int)
    # Check the number of cards
    if len(group) != 7:
        return None
    # Counting cards' suits and number of wild cards
    for card in group:
        if card in WILD_CARDS:
            suit_count['wild_card'] += 1
        else:
            suit_count[card[1]] += 1

    for suit in suit_count.copy().keys():
        if suit != 'wild_card':
            # 7 cards of same suit
            if suit_count[suit] == 7:
                return 2

            # a set of at least 2 natural cards with same suit
            # + wild cards
            elif suit_count[suit] >= 2 and suit_count[
                 suit] + suit_count['wild_card'] == 7:
                return 2

    return None


def phasedout_phase_2(phase):
    '''Return 2 if the phase satisifies phase 2's requirement'''

    # Check the number of groups
    if len(phase) == 1:
        # Check if the group is group 2
        if phasedout_group_2(phase[0]):
            return 2
        else:
            return False
    else:
        return False


def phasedout_group_3(group):
    '''Return 3 if the group satisfies type 3's requirement,
    otherwise return None'''

    value_count = dd(int)
    # Check the number of cards
    if len(group) != 4:
        return None

    # Counting values of the card set
    for card in group:
        if card in WILD_CARDS:
            value_count['wild_card'] += 1
        else:
            value_count[card[0]] += 1

    for value in value_count.copy().keys():
        if value != 'wild_card':
            # 4 natural cards with same value
            if value_count[value] == 4:
                return 3

            # a set of at least 2 natural cards with same value
            # + wild cards
            elif value_count[value] >= 2 and value_count[
                 value] + value_count['wild_card'] == 4:
                return 3
    return None


def phasedout_phase_3(phase):
    ''' Return 3 if phase satisfies phase 3's requirement,
    otherwise return None'''

    # Check the number of groups
    if len(phase) == 2:
        # Check if both groups are group 3
        for group in phase:
            if not phasedout_group_3(group):
                return None
        return 3


def phasedout_group_4(group):
    '''Return 4 if the group satisfies type 4's requirement,
    otherwise return None'''
    wild_card_count = 0
    first_natural = 0
    n = 0

    # Check the number of cards in the group
    if len(group) != 8:
        return None

    # Find the first natural card's index in the group
    for i in range(len(group)):
        if group[i] in WILD_CARDS:
            wild_card_count += 1
            # the group has to have at least 2 natural cards
            if wild_card_count == 7:
                return None
        else:
            first_natural = i
            n = VALUE_ORDER[group[i][0]]
            break

    # number of wild cards before the first natural card exceeds
    # natural card's value
    if first_natural != 0 and wild_card_count >\
       VALUE_ORDER[group[first_natural][0]]:
        return None

    # Iterate from the first natural card for checking
    # if the values are in ascending order
    for card in group[first_natural + 1:]:
        if card in WILD_CARDS:
            wild_card_count += 1
            n += 1
            # the group has to have at least 2 natural cards
            if wild_card_count > 6:
                return None
            # no wild card is allowed after value 'K'
            elif n > 11:
                return None
        else:
            if VALUE_ORDER[card[0]] != n+1:
                return None
            else:
                n += 1
                # No card is allowed after value 'K'
                if n > 11:
                    return None
    return 4


def phasedout_phase_4(phase):
    '''Return 4 if phase satisfies phase 4's requirement,
    otherwise return None'''

    # Check the number of group and the number of cards in the group
    if len(phase) == 1:
        # Check if the group satisfies group 4's reuqirement
        if phasedout_group_4(phase[0]):
            return 4


def phasedout_group_5(group):
    '''Return 5 if the group satisfies type 5's requirement
    otherwise return None'''

    colour_count = dd(int)
    wild_card_count = 0
    first_natural = 0
    n = 0

    # Check the number of cards
    if len(group) != 4:
        return None

    for card in group:
        # Counting wild cards
        if card in WILD_CARDS:
            wild_card_count += 1
        # Counting colours of natural cards
        else:
            colour_count[COLOUR_DICT[card[1]]] += 1

    # Check if cards are in ascending order
    # Find the first natural card's index in the group
    for i in range(len(group)):
        if group[i] in WILD_CARDS:
            wild_card_count += 1
            # maximum of 2 wild cards for valid run
            if wild_card_count == 3:
                return None
        else:
            first_natural = i
            # find the order value of the first natural card
            n = VALUE_ORDER[group[i][0]]
            break

    # the number of wild cards before the first natural card
    # should not exceed the value of the natural card
    if first_natural != 0 and wild_card_count >\
       VALUE_ORDER[group[first_natural][0]]:
        return None

    # Iterate from the first natural acards for checking
    # if the cards are in ascending order
    for card in group[first_natural + 1:]:
        if card in WILD_CARDS:
            wild_card_count += 1
            n += 1
            # maximum of 2 wild cards for valid run
            if wild_card_count == 3:
                return None
            # no card allowed after value 'K'
            elif n > 11:
                return None
        else:
            if VALUE_ORDER[card[0]] != n+1:
                return None
            else:
                n += 1
                # no card allowed after value 'K'
                if n > 11:
                    return None

    # Check the colours of the cards
    for colour in colour_count.copy().keys():
        if colour != 'wild_card':
            # 4 cards of the same colour
            if colour_count[colour] == 4:
                return 5
            # A set of at least 2 natural cards of the same colour
            # + wild cards
            elif colour_count[colour] >= 2 and colour_count[
              colour] + colour_count['wild_card'] == 4:
                return 5

    return None


def phasedout_phase_5(phase):
    '''Return 5 if phase satisfies phase 5's requirement,
    otherwise return None'''

    # Check the number of groups and the number of cards in the group
    if len(phase) != 2:
        return None

    # Check if the groups of cards satisfy group 5's and group 3's requirement
    # respectively
    if phasedout_group_5(phase[0]) and phasedout_group_3(phase[1]):
        return 5


def phasedout_phase_type(phase):
    ''' Return the type of the given phase of cards. Return None if the phase
    doesn't match any type.'''

    # List that store all the previous phase test functions
    phasedout_phase = [phasedout_phase_1, phasedout_phase_2,
                       phasedout_phase_3, phasedout_phase_4, phasedout_phase_5]

    # Run the tests of phase types on the given phase
    for phase_test in phasedout_phase:
        if phase_test(phase):
            return phase_test(phase)

    return None


def phasedout_is_valid_play(play, player_id, table, turn_history,
                            phase_status, hand, discard):
    ''' Return True if the play is valid to the current game state,
    otherwise return False'''

    phase = phase_status[player_id]
    phase_card = table[player_id][1]
    play_type = play[0]
    cards_play = play[1]

    if (turn_history and turn_history[-1][0] != player_id) \
       or (not turn_history):
        # Player can't draw a card if it is not the first turn
        if turn_history[-1][0] != player_id:
            if play_type == 1 and turn_history and len(cards_play) == 2:
                return True
            elif play_type == 2 and cards_play == discard:
                return True
            else:
                return False

    # Discarding card must be in the hand
    elif play_type == 5 and cards_play in hand:
        return True

    # The phase to be placed must be valid
    # The phase type must be the current phase + 1
    elif play_type == 3:
        phase_type = phasedout_phase_type(cards_play)
        if phase_type == phase + 1:
            return True

    elif play_type == 4:
        # The card to be place on top of the other phase
        card = cards_play[0]
        # The player of the pre-existed phase
        phase_player = cards_play[1][0]
        # The type of the pre-existed phase
        phase_player_phase = phase_status[phase_player]
        # The cards of the pre-existed phase
        phase_cards = table[phase_player][1]
        # The group in the pre-existed phase
        phase_group = cards_play[1][1]
        # The position of the card to be placed in the group
        position = cards_play[1][2]

        if position == len(phase_cards[phase_group]) - 1:
            return False
        # group type 4 and 5: cards in sequence and wild card cannot take value
        # of 1 or 14
        if card in WILD_CARDS:
            if phase_player_phase == 4\
               or (phase_player_phase == 5 and phase_group == 0):
                new_card = phase_cards + []
                new_card[phase_group] = phase_cards[phase_group][
                    :position + 1] + [card] + phase_cards[
                        phase_group][position + 1:]
                wild_card_count = 0
                first_natural = 0
                n = 0
                colour_count = dd(int)

                for card in new_card[phase_group]:
                    # Counting wild cards
                    if card in WILD_CARDS:
                        wild_card_count += 1
                    # Counting colours of natural cards
                    else:
                        colour_count[COLOUR_DICT[card[1]]] += 1

                # Check if cards are in ascending order
                # Find the first natural card's index in the group
                for i in range(len(new_card[phase_group])):
                    if new_card[phase_group][i] in WILD_CARDS:
                        wild_card_count += 1
                    else:
                        # find the order value of the first natural card
                        first_natural = i
                        n = VALUE_ORDER[new_card[phase_group][i][0]]
                        break

                # the number of wild cards before the first natural card
                # should not exceed the value of the natural card
                if first_natural != 0 and wild_card_count >\
                   VALUE_ORDER[new_card[phase_group][first_natural][0]]:
                    return False

                # Iterate from the first natural acards for checking
                # if the cards are in ascending order
                for card in new_card[phase_group][first_natural + 1:]:
                    if card in WILD_CARDS:
                        wild_card_count += 1
                        n += 1
                        # no card allowed after value 'K'
                        if n > 11:
                            return False
                    else:
                        n += 1
                        if VALUE_ORDER[card[0]] != n:
                            return False
                        else:
                            # no card allowed after value 'K'
                            if n > 11:
                                return False
                return True

        # group type 1,3: same value
        if phase_player_phase in [1, 3] or\
           (phase_player_phase == 5 and phase_group == 1):
            value = 0
            for phase_card in phase_cards[phase_group]:
                if phase_card not in WILD_CARDS:
                    value = phase_card[0]
                    break
            if card[0] == value:
                return True

        # group type 2: same suit
        elif phase_player_phase == 2:
            for phase_card in phase_cards[phase_group]:
                if phase_card not in WILD_CARDS:
                    suit = phase_card[1]
                    break
            if card[1] == suit:
                return True

        # group type 4: cards in sequence
        elif phase_player_phase == 4:
            # in sequence
            new_card = phase_cards + []
            new_card[phase_group] = phase_cards[phase_group][
                :position + 1] + [card] + phase_cards[phase_group][
                    position + 1:]
            if phasedout_phase_type(new_card) == 4:
                return True

        # group type 5: same colour and in sequence
        elif phase_player_phase == 5 and phase_group == 0:
            new_card = phase_cards + []
            new_card[phase_group] = phase_cards[phase_group][
                :position + 1] + [card] + phase_cards[phase_group][
                    position + 1:]
            if phasedout_phase_type(new_card) == 5:
                return True

    return False


def play_4_5(player_id, table, turn_history, phase_status,
             hand, discard, drawn_card):
    '''Create a type 4 or 5 play after player has placed the phase
    if the player has already drawn a card, otherwise draw a card'''

    # Case 1: Need to draw a card in first turn
    if drawn_card == 0:
        return (1, None)

    # Case 2: player has already drawn a card
    # play type 4: Find the pre-existed phase that the card can be placed on
    for n in range(4):
        if table[n][1]:
            # the group in the pre-existed phase
            for i in range(len(table[n][1])):
                # the position in the pre-existed phase
                for j in range(len(table[n][1][i])):
                    for card in hand:
                        play = (4, (card, (n, i, j)))
                        # Check if the play is valid
                        if phasedout_is_valid_play(play, player_id, table,
                                                   turn_history, phase_status,
                                                   hand, discard):
                            return play

    # play type 5: discard a card
    for card in hand:
        if card not in WILD_CARDS:
            return (5, card)
    # only have wild card in hand
    return (5, hand[0])


def build_phase_1(hand, discard, drawn_card):
    ''' Return a play type 3 with a set of phase 1 card or the best card to be
    discarded if the player has already drawn card, otherwise draw a card'''

    # Counting the values of the cards in the set
    value_count = dd(int)
    for card in hand:
        if card not in WILD_CARDS:
            value_count[card[0]] += 1

    # Case 1: player need to draw a card
    if drawn_card == 0:
        # draw the disard card if the discard card's value is
        # the most frequent value in the hand
        # or if it is a wild card
        if discard:
            if discard in WILD_CARDS\
               or value_count[discard[0]] == max(value_count.values()):
                return (2, discard)
        return (1, None)

    # Case 2: player has already drawn a card
    # create a phase 1 card set
    for group in combinations(hand, 3):
        # 1st group in the phase
        if phasedout_group_1(group):
            phase = []
            group_lst = [i for i in group]
            phase.append(group_lst)
            left_over = []
            for card in hand:
                if card in hand and card not in group:
                    left_over.append(card)
            # 2nd group in the phase
            for group in combinations(left_over, 3):
                if phasedout_group_1(group):
                    group_lst = [i for i in group]
                    phase.append(group_lst)
                    return (3, phase)

    # No phase 1 set can be created
    # Discard card that has the least frequent value in the hand
    for card in hand:
        if card not in WILD_CARDS\
           and value_count[card[0]] == min(value_count.values()):
            return (5, card)


def build_phase_2(hand, discard, drawn_card):
    ''' Return a play type 3 with a set of phase 2 card or the best card to be
    discarded if the player has already drawn card, otherwise drawn a card'''

    # Counting suit
    suit_count = dd(int)
    for card in hand:
        if card not in WILD_CARDS:
            suit_count[card[1]] += 1

    # Case 1: Player need to draw a card
    if drawn_card == 0:
        # draw the disard if it is a wild card
        # or its suit is the most frequent suit in the hand
        if discard:
            if discard in WILD_CARDS\
               or suit_count[discard[1]] == max(suit_count.values()):
                return (2, discard)
        return (1, None)

    # Case 2: Player has already drawn a card
    # Create a phase 2 card set
    phase = []
    for group in combinations(hand, 7):
        if phasedout_group_2(group):
            phase.append(group)
            return (3, phase)

    # No phase 2 card set can be created
    # Discard the card that has the least frequent suit
    for card in hand:
        if card not in WILD_CARDS\
           and suit_count[card[1]] == min(suit_count.values()):
            return(5, card)


def build_phase_3(hand, discard, drawn_card):
    ''' Return a play type 3 with a set of phase 3 card or the best card to be
    discarded if the player has already drawn card, otherwise drawn a card'''

    # counting value of the hand
    value_count = dd(int)
    for card in hand:
        if card not in WILD_CARDS:
            value_count[card[0]] += 1

    # Case 1: player need to draw a card
    if drawn_card == 0:
        # draw the discard if it is a wild card
        # or it has the most frequent value in the hand
        if discard:
            if discard in WILD_CARDS\
               or value_count[discard[0]] == max(value_count.values()):
                return (2, discard)
        return (1, None)

    # Case 2: player has already drawn a card
    # create a phase 3 card set
    for group in combinations(hand, 4):
        # 1st group in the phase
        if phasedout_group_3(group):
            phase = []
            group_lst = [i for i in group]
            phase.append(group_lst)
            left_over = []
            for card in hand:
                if card not in group:
                    left_over.append(card)
            # 2nd group in the phase
            for group in combinations(left_over, 4):
                if phasedout_group_3(group):
                    group_lst = [i for i in group]
                    phase.append(group_lst)
                    return (3, phase)

    # no phase 3 card set can be created
    # discard the card that has the least frequent value in the hand
    for card in hand:
        if (card not in WILD_CARDS)\
           and value_count[card[0]] == min(value_count.values()):
            return (5, card)


def build_phase_4(hand, discard, drawn_card):
    ''' Return a play type 3 with a set of phase 4 card or the best card to be
    discarded if the player has already drawn card, otherwise drawn a card'''

    phase = []
    existed_value = {}
    wild_card = []
    value_count = dd(int)
    # create a list for wild card and a dictionary of unique card value
    # and counting the value
    for card in hand:
        if card in WILD_CARDS:
            wild_card.append(card)
        else:
            value_count[card[0]] += 1
            if not VALUE_ORDER[card[0]] in existed_value.keys():
                existed_value[VALUE_ORDER[card[0]]] = card

    existed_value_ordered = sorted([i for i in existed_value.items()])

    # Case 1: the player need to draw a card
    if drawn_card == 0:
        # draw the discard card if it is wild card or
        # it has a unique value within the range of current cards in hand
        if discard and discard in WILD_CARDS:
            return (2, discard)
        elif discard:
            if not VALUE_ORDER[discard[0]] in existed_value.keys():
                discard_order = VALUE_ORDER[discard[0]]
                if min(existed_value.keys()) < discard_order\
                   < max(existed_value.keys()):
                        return (2, discard)
        return (1, None)

    # Case 2: Player has already drawn a card
    # Create a phase 4 card set
    # find the minimum number of natural cards need to be included in the phase
    min_total_natural = len(existed_value_ordered) 
    if len(existed_value_ordered) >= 2:
        for i in range(2, len(existed_value_ordered)):
            if i + len(wild_card) >= 8:
                min_total_natural = i
                break

    # sorted combination of cards with different numbers of natural cards
    for j in range(min_total_natural, len(existed_value_ordered) + 1):
        for comb in combinations(existed_value_ordered, j):
            # Maximum number of wild cards in the phsae
            n = min(8 - j, len(wild_card))
            group = [comb[0][1]]
            prev_val = comb[0][0]
            wild_card_in_group = 0
            for k in comb[1:]:
                prev_val += 1
                # append the card to the group if the sequence is continuous
                if prev_val == k[0]:
                    group.append(k[1])
                # the sequence of value is not continuous
                else:
                    # fill the difference of values between the two cards
                    # with wild cards
                    for l in range(k[0] - prev_val):
                        if wild_card_in_group < n:
                            group.append(wild_card[wild_card_in_group])
                            wild_card_in_group += 1
                        # number of wild cards in the group exceeds
                        # its maximum capacity
                        else:
                            break
                    group.append(k[1])
                    prev_val = k[0]

            if phasedout_group_4(group):
                phase.append(group)
                return (3, phase)

    # No phase 4 card set can be created
    for card in hand:
        # Discard a wild card if the number of wild cards
        # exceeds the maximum number of wild cards in a phase
        if len(wild_card) > 6:
            if card in WILD_CARDS:
                return (5, card)
        # Discard the card if there is more than 1 card with the same value
        elif card not in WILD_CARDS and value_count[card[0]] != 1:
            return (5, card)
        # discard a card that is the beginning/ending of
        # the ordered unique values
        else:
            if VALUE_ORDER[card[0]] == existed_value_ordered[
                 0] or VALUE_ORDER[card[0]] == existed_value_ordered[-1]:
                return (5, card)
            
def build_phase_5(hand, discard, drawn_card):
    ''' Return a play type 3 with a set of phase 5 card or the best card to be
    discarded if the player has already drawn card, otherwise drawn a card'''

    # Case 1: The player need to draw a card
    # Draw the discard if including it in the hand can create a phase 5 set
    if drawn_card == 0:
        if discard:
            new_hand = hand + []
            new_hand.append(discard)
            for group in permutations(new_hand, 4):
                if phasedout_group_5(group):
                    left_over = []
                    for card in new_hand:
                        if card not in group:
                            left_over.append(card)
                        for group in combinations(left_over, 4):
                            if phasedout_group_3(group):
                                return (2, discard)
        return (1, None)

    # Case 2: player has alerady drawn a card
    # Create a phase 5 card set
    for group in permutations(hand, 4):
        # 1st group in the phase
        if phasedout_group_5(group):
            phase = []
            group_lst = [i for i in group]
            phase.append(group_lst)
            left_over = []
            for card in hand:
                if card not in group:
                    left_over.append(card)
            # 2nd group in the phase
            for group in combinations(left_over, 4):
                if phasedout_group_3(group):
                    group_lst = [i for i in group]
                    phase.append(group_lst)
                    return (3, phase)

    # No phase 5 card set can be created
    value_count = dd(int)
    existed_value = {}
    colour_count = dd(int)
    # counting card's value, colour and the unique value in the hand
    for card in hand:
        if card not in WILD_CARDS:
            value_count[card[0]] += 1
            existed_value[card[0]] = VALUE_ORDER[card[0]]
            existed_value_ordered = sorted([i for i in existed_value.values()])
            colour_count[COLOUR_DICT[card[1]]] += 1
    # discard a natural card that either has the least frequent colour
    # or it is the beginning/ending of the ordered unique values
    for card in hand:
        if card not in WILD_CARDS:
            if value_count[card[0]] > 5 and \
               colour_count[COLOUR_DICT[card[1]]] ==\
               min(colour_count.values()):
                return (5, card)
            elif VALUE_ORDER[card[0]] == existed_value_ordered[
                 0] or VALUE_ORDER[card[0]] == existed_value_ordered[-1]:
                return (5, card)


def phasedout_play(player_id, table, turn_history, phase_status,
                   hand, discard):
    '''return the play that the player is going to place'''
    # player's phase
    player_phase = phase_status[player_id]
    # the phase that player has placed in the current round
    player_phase_card = table[player_id][1]
    # list of all the phase building functions
    phase_build_lst = [build_phase_1, build_phase_2, build_phase_3,
                       build_phase_4, build_phase_5]

    # Check if the player has drawn a card or not
    drawn_card = 0
    if turn_history and turn_history[-1][0] == player_id:
        drawn_card = 1

    # Case 1: Player has already placed a phase
    if player_phase_card:
        # Try to discard all the cards, play type 4 or 5
        return play_4_5(player_id, table, turn_history, phase_status,
                        hand, discard, drawn_card)
    # Case 2: Player is trying to place a phase
    else:
        # Determine the type of phase the player should place
        build_phase = phase_build_lst[player_phase]
        return build_phase(hand, discard, drawn_card)


if __name__ == '__main__':
    # Example call to the function.
    print(phasedout_play(1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H', '0S', 'JS']]), (None, []), (None, [])], [(0, [(2, 'JS'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']]), (4, ('0S', (1, 0, 8))), (4, ('JS', (1, 0, 9)))])], [0, 4, 0, 0], ['5D'], '7H'))
