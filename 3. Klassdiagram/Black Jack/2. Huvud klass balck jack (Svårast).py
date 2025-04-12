import random
from Player import player
from Dealer import dealer
from Deck import deck

#Superklass BlackJack
class BlackJack:
    def __init__(self, player, dealer, card):
        self.player = player
        self.dealer = dealer
        self.card = card

    def play(self):
        self.welcome()
        self.status()
        self.dealer_draw_cards()
            
    def welcome(self):
        print("Välkommen till BlackJack")

    def status(self):
        amount = input("Ange hur mycket du vill ")
    def dealer_drav_cards(self):
        return


BlackJack.play()