from art import logo
from replit import clear
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards: 


def game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  deck = {
    "♣": [],
    "♥": [],
    "♦": [],
    "♠": []
  }
  
  player = {
    "♣": [],
    "♥": [],
    "♦": [],
    "♠": []
  }
  
  computer = {
    "♣": [],
    "♥": [],
    "♦": [],
    "♠": []
  }
  
  player_list = []
  computer_list = []
  
  for type in deck:
    deck[type] = cards
  
  plant = False
  win = False
  game_over = False
  
  def turn(dict,list):
    clear()
    print(logo)
    type = random.randint(1,4)
    key = ""
    if type == 1:
      key = "♣"
    if type == 2:
      key = "♥"
    if type == 3:
      key = "♦"
    if type == 4:
      key = "♠"
    place_dict = dict[key]
    place_deck = deck[key]
    index_card = random.randint(0,len(place_deck)-1)
    value = place_deck[index_card]
    number = value
    if number == 11:
      number = "A"
    card = f"{number}{key}"
    list.append(card)
    place_dict.append(value)
    place_deck.remove(value)
  
  def calculate_score(dict):
    score = 0
    num_of_aces = 0
    for key in dict:
      list = dict[key]
      for card in list:        
        score += card
        if card == 11:
          num_of_aces += 1
    while num_of_aces > 0 and score > 21:
      score -= 10
      num_of_aces -= 1        
    return score
  
  #if start == "y":
  for x in range(2):
    turn(player, player_list)
    turn(computer, computer_list)
    score_player = calculate_score(player)
    score_computer = calculate_score(computer)
    print(f"Your cards: {player_list}, current score: {score_player}")
    print(f"Computer's first card: {computer_list[0]}")
    if score_player == 21:
      win = True
      result = "You Win! BlackJack 21"
      if score_player == score_computer:
        result = "Tie!"
  
  while plant == False and game_over == False and win == False and score_computer <= 21:
    ask_card = input("Type 'y' to get another card, type 'n' to plant: ")
    if ask_card == "y":
      turn(player, player_list)
      turn(computer, computer_list)
      score_player = calculate_score(player)
      score_computer = calculate_score(computer)
      print(f"Your cards: {player_list}, current score: {score_player}")
      print(f"Computer's first card: {computer_list[0]}")
    elif ask_card == "n":
      plant = True
      while score_computer < score_player:
        turn(computer, computer_list)
        score_computer = calculate_score(computer)
    result = ""
    if score_player == 21:
      win = True
      result = "You Win! BlackJack 21"
      if score_player == score_computer:
        result = "Draw!"
    elif score_player > 21:
      game_over = True
      result = "You Lose!"
    elif score_player == score_computer and score_player < 21:
      result = "Tie!"
    elif score_player > score_computer: 
      if score_player < 21:
        result = "You Win!"
      else:
        result = "You Lose!"
    elif score_player < score_computer: 
      if score_computer > 21:
        result = "You Win!"
      else:
        result = "You Lose!"
  
  clear()
  print(logo)
  print(f"Your cards: {player_list}, current score: {score_player}")
  print(f"Computer cards: {computer_list}, current score: {score_computer}")
  print(result)
  return start

run_game = False

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if start == "y":
  run_game = True

while not run_game == False:
  game()
  start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if start != "y":
    run_game = False


#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

