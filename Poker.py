#  Description: This assignment will simulate a regular Poker game otherwise
#  known as the 5-Card Draw.

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, n = 1):
    self.deck = []
    for i in range (n):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    for i in range (num_players):
        self.all_hands.append([])

    # deal all the hands
    for i in range (self.numCards_in_Hand):
      hand = []
      for j in range (num_players):
        hand.append (self.deck.deal())
        self.all_hands[j].append (hand[j])

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points

  # determine if a hand is a straight flush takes as argument a list of 5
  # Card objects and returns a number (points) for that hand. A hand is a
  # straight flush if it is is made of 5 cards in numerical sequence but
  # of the same suit.
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
        same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
        return 0

    rank_order = True
    for i in range(len(hand)):
        if i == 0:
            pass
        rank_order = rank_order and (hand[i].rank == ((hand[i - 1].rank) - 1))

    if (not rank_order):
        return 0

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points

  # determine if a hand is a straight flush takes as argument a list of 5
  # Card objects and returns a number (points) for that hand
  # In four of a kind, the hand must have four cards of the same numerical rank.
  # Since they are already sorted by rank, we only need to check two scenarios.
  def is_four_kind (self, hand):
    count = hand.count(hand[2])
    if count != 4:
        return 0

    if (hand[0].rank) == (hand[2].rank):
        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points

    elif (hand[4].rank) == (hand[2].rank):
        points = 8 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
        points = points + (hand[0].rank)
        return points

  # determine if a hand is full house. Takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  # For a full house, three of the cards must have the same numerical rank and the
  # two remaining cards must also have the same numerical rank but different rank than the other three.
  def is_full_house (self, hand):
    count1 = 0
    count2 = 0
    first_card = hand[0].rank
    last_card = hand[4].rank
    for i in range(len(hand)):
        if i == 0:
            pass
        elif i == 4:
            pass
        else:
            if hand[i].rank == first_card:
                count1 += 1
            elif hand[i].rank == last_card:
                count2 += 1

    if (count1 != 3 and count1 != 2) or (count2 != 3 and count2 != 2):
        return 0

    if count1 == 3:
        points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points

    elif count2 == 3:
        points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
        points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
        points = points + (hand[1].rank)
        return points

  # determine if a hand is a flush. Takes as argument a list of 5
  # Card objects and returns a number (points) for that hand. A hand is a
  # flush if there are 5 cards all of the same suit.
  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
        same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
        return 0

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points

  # determine if a hand is a staight. Takes as argument a list of 5
  # Card objects and returns a number (points) for that hand. In a straight hand,
  # the 5 cards are in numerical order but are not all of the same suit.
  def is_straight (self, hand):

    rank_order = True
    for i in range(len(hand)):
        if i == 0:
            pass
        rank_order = rank_order and (hand[i].rank == ((hand[i - 1].rank) - 1))

    if (not rank_order):
        return 0

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points

  # determine if a hand is three of a kind. Takes as argument a list of 5
  # Card objects and returns a number (points) for that hand. In three of a kind
  # hand, there are 3 cards of the same rank and the other two are unrelated
  def is_three_kind (self, hand):
    count = hand.count(hand[2])
    if count != 3:
        return 0

    if (hand[2].rank) == (hand[0].rank):
        points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points

    elif (hand[2].rank) == (hand[4].rank):
        points = 4 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
        points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
        points = points + (hand[1].rank)
        return points

    elif (hand[1].rank == hand[2].rank) and (hand[2].rank == hand[3].rank):
        points = 4 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
        points = points + (hand[3].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points

  # determine if a hand is a two pair. Takes as argument a list of 5
  # Card objects and returns a number (points) for that hand. A hand is two pair if
  # there are two cards of a matching rank, another two cards of a different
  # matching rank, and a fifth random card.
  def is_two_pair (self, hand):
    count1 = hand.count(hand[1])
    count2 = hand.count(hand[3])
    if (count1 != 2) or (count2 != 2):
        return 0

    if hand[0].rank > hand[1].rank:
        points = 3 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
        points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
        points = points + (hand[0].rank)
        return points

    if (hand[2].rank < hand[1].rank) and (hand[2].rank > hand[3].rank):
        points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
        points = points + (hand[2].rank)
        return points

    if hand[4].rank < hand[3].rank:
        points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_one_pair (self, hand):
    place = 0
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        place = i
        break

    if (not one_pair):
      return 0

    if place == 0:
      points = 2 * 15 ** 5 + (hand[place].rank) * 15 ** 4 + (hand[place + 1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points

    if place == 1:
      points = 2 * 15 ** 5 + (hand[place].rank) * 15 ** 4 + (hand[place + 1].rank) * 15 ** 3
      points = points + (hand[0].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points

    if place == 2:
      points = 2 * 15 ** 5 + (hand[place].rank) * 15 ** 4 + (hand[place + 1].rank) * 15 ** 3
      points = points + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points

    if place == 3:
      points = 2 * 15 ** 5 + (hand[place].rank) * 15 ** 4 + (hand[place + 1].rank) * 15 ** 3
      points = points + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
      points = points + (hand[2].rank)
      return points

  # If none of the hands in a game qualified under the categories listed above
  # then the hand having the highest ranking card wins.
  def is_high_card (self, hand):
    highest_rank = 0
    place = 0
    for i in range(len(hand)):
        if i == 0:
            highest_rank = hand[i].rank
        elif hand[i].rank > highest_rank:
            highest_rank = hand[i].rank

    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points

  # Determine which player won. First function will compare hands against each other,
  # if top hand is unique, function will print out which player won. If top hand
  # is not unique, function will print out the players that are tied in descending
  # order.
  def winner (self):
    print("")
    points_hand = []
    indices_list = []
    for i in range(len(self.all_hands)):
      if self.is_royal(self.all_hands[i]) != 0:
        points_hand.append(self.is_royal(self.all_hands[i]))
        indices_list.append(10)
        print('Player {} : Royal Flush'.format(i+1))
      elif self.is_straight_flush(self.all_hands[i]) != 0:
        points_hand.append(self.is_straight_flush(self.all_hands[i]))
        indices_list.append(9)
        print('Player {} : Straight Flush'.format(i+1))
      elif self.is_four_kind(self.all_hands[i]) != 0:
        points_hand.append(self.is_four_kind(self.all_hands[i]))
        indices_list.append(8)
        print('Player {} : Four of a Kind'.format(i+1))
      elif self.is_full_house(self.all_hands[i]) != 0:
        points_hand.append(self.is_full_house(self.all_hands[i]))
        indices_list.append(7)
        print('Player {} : Full House'.format(i+1))
      elif self.is_flush(self.all_hands[i]) != 0:
        points_hand.append(self.is_flush(self.all_hands[i]))
        indices_list.append(6)
        print('Player {} : Flush'.format(i+1))
      elif self.is_straight(self.all_hands[i]) != 0:
        points_hand.append(self.is_straight(self.all_hands[i]))
        indices_list.append(5)
        print('Player {} : Straight'.format(i+1))
      elif self.is_three_kind(self.all_hands[i]) != 0:
        points_hand.append(self.is_three_kind(self.all_hands[i]))
        indices_list.append(4)
        print('Player {} : Three of a Kind'.format(i+1))
      elif self.is_two_pair(self.all_hands[i]) != 0:
        points_hand.append(self.is_two_pair(self.all_hands[i]))
        indices_list.append(3)
        print('Player {} : Two Pair'.format(i+1))
      elif self.is_one_pair(self.all_hands[i]) != 0:
        points_hand.append(self.is_one_pair(self.all_hands[i]))
        indices_list.append(2)
        print('Player {} : One Pair'.format(i+1))
      else:
        points_hand.append(self.is_high_card(self.all_hands[i]))
        indices_list.append(1)
        print('Player {} : High Card'.format(i+1))

    top_in_list = max(indices_list)
    order_dict = {}
    for i in range(len(indices_list)):
        if indices_list[i] == top_in_list:
            order_dict[str(i+1)] = points_hand[i]
    if len(order_dict) > 1:
        print('')
        for i in sorted(order_dict, key=order_dict.get, reverse=True):
            print ('Player {} ties.'.format(i))
    else:
        print('\nPlayer {} wins.'.format(points_hand.index(max(points_hand))+1))

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str(card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
    # determine winner and print
    self.winner()

def main():
  # prompt the user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))
  print('')
  # create the Poker object
  game = Poker (num_players)

  # play the game - poker
  game.play()

# do not remove this line above main()
if __name__ == '__main__':
  main()
