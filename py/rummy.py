#!python3 
import random

def card():
    deck_diamond = ['D_K','D_Q','D_J','D_10','D_9','D_8','D_7','D_6','D_5','D_4','D_3','D_2','D_A']
    deck_hearts = ['H_K','H_Q','H_J','H_10','H_9','H_8','H_7','H_6','H_5','H_4','H_3','H_2','H_A']
    deck_spades = ['S_K','S_Q','S_J','S_10','S_9','S_8','S_7','S_6','S_5','S_4','S_3','S_2','S_A']
    deck_clubs = ['C_K','C_Q','C_J','C_10','C_9','C_8','C_7','C_6','C_5','C_4','C_3','C_2','C_A']
    deck = [deck_diamond, deck_hearts, deck_spades, deck_clubs]
    player1 = []
    player2 = []
    stock_cards=[]

    for i in range(0,3):
        player1.append(random.choice(deck[i]))
        player2.append(random.choice(deck[i]))
        stock_cards.append(deck)

    print(player1)
    print(player2)
    print(stock_cards)

card()