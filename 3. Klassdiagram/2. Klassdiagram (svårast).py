import random
import time

class Card(): #Sätt kort värde&färg
    #Bestäm färg -- bestäm grupp -- 
    def __init__(self, card_number):
        self.color = self.set_color(card_number) #färg attribute
        self.number = self.set_number(card_number) #nummer attribute
        self.value = self.set_value(card_number) #värde attribute

    def set_color(self, card_number): #sätt grupp beroende på kortnummer
        if card_number < 13:
            return "Hjärter"
        elif card_number < 26:
            return "Ruter"
        elif card_number < 39: 
            return "Spader"
        else: 
            return "Klöver" 

    def set_number(self, card_number): #sätta kortnummer 
        return str(self.color)
    
    def set_number(self, card_number):
        card_value = card_number % 13
        if card_value < 9:
            return str(card_value + 2)
        elif card_value == 9:
            return "Knekt"
        elif card_value == 10:
            return "Dam"
        elif card_value == 11:
            return "Kung"
        else:
            return "Ess"

    def set_value(self, soft):
        if self.value in ["Knekt", "Dam", "Kung"]:
            return 10
        elif self.value == "Ess":
            return 1 if soft else 11
        else:
            return int(self.value)

            
    def __str__(self):
        return f"{self.color} {self.number}"







class Hand(): #
    def __init__(self, cards):
        self.cards = cards
        self.is_soft = False
        total = 0

    def add_card(self, card):
        self.cards.append(card)
        self.is_soft = False
        total = self.total_sum()
        if total > 21:
            self.is_soft = True
        return self.cards

    def is_busted(self):
        cards_sum = 0
        for card in self.cards:
            cards_sum += card.get_value(self.is_soft)
        if cards_sum > 21:
            return True
        else:
            return False
        
    def get_first_card(self):
        return self.cards[0]

    def is_black_jack(self):
        cards_sum = 0
        for card in self.cards:
            cards_sum += card.get_value(self.is_soft)
        if cards_sum == 21:
            return True
        else:
            return False

    def total_sum(self):
        total = 0
        for card in self.cards:
            total += card.get_value(self.is_soft)
        return total

    def __str__(self):
        total = 0
        cards = []
        for card in self.cards:
            cards.append(card.__str__())
            total += card.get_value(self.is_soft)
        output = "{:<15}, Totalt: {}".format(", ".join(cards), total)
        return output








class CardPlayer():
    def __init__(self, name):
        self.hand = Hand([])
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self.name



class BlackJack: #Superklass
    def __init__(self): #attribut inskriv i metod sen
        self.player = None
        self.dealer = None
        self.card = None

    def play(self): #sätter igång black jack och hanterar spelet
        self.welcome() #introduktion och inskrivningar

        while self.player.get_balance() > 0 and input("Vill du spela? (j/n) ").lower() in ["j", "ja"]: #så länge player svarar "j" till spel och balanse är pos
            self.deck = Deck() #hämtar deck
            self.player.hand = Hand([]) 
            self.dealer.hand = Hand([])
            
            self.status()
            
            amount = int(input("Hur mycket vill du satsa? "))
            win = False
            # Draw the first two cards to dealer and player
            self.dealer_draw_cards()
            while not self.player.hand.is_black_jack() and not self.player.hand.is_busted() and input("Vill du dra ett nytt kort? (y/n) ") == "y":
                self.player.hand.add_card(self.deck.take_card())
                print("\n{:<10}: {}\n".format(self.player.get_name(), self.player.hand))
            if self.player.hand.is_black_jack():
                win = True
            elif self.player.hand.is_busted():
                print("Du blev tyvärr tjock!")
            else:
                print("\n- Dealers tur")
                print("{:<10}: {}\n".format(self.dealer.get_name(), self.dealer.hand))
                while self.dealer.hand.total_sum() < 16:
                    time.sleep(0.5)
                    self.dealer.hand.add_card(self.deck.take_card())
                    print("{:<10}: {}\n".format(self.dealer.get_name(), self.dealer.hand))
                if self.dealer.hand.is_black_jack():
                    print("\n- " + self.dealer.get_name() + " fick Black Jack!")
                elif self.dealer.hand.is_busted():
                    print("\n -" + self.dealer.get_name() + " blev tjock!")
                    win = True
                else:
                    if self.player.hand.total_sum() > self.dealer.hand.total_sum() and self.dealer.hand.total_sum() < 22:
                        win = True
            if win:
                print("\nSnyggt jobbat!")
                self.player.add_money(amount)
            else:
                print("\nBättre lycka nästa gång!")
                self.player.remove_money(amount)
            print("*" * 28)
        if self.player.get_balance() == 0:
            print("\nDu gick bankrutt, trist!")
        else:
            print("\nVälkommen tillbaka! =)")

    def welcome(self): #välkomnar spelaren, inskriv namn(player&dealder) & satsning
        print("-- Välkommen!!")
        name = input("Vad heter du? \nPlayer namn: ")
        money = int(input("Hur mycket vill du satsa? (kr) \nSumma: "))
        self.player = Player(name, money)
        
        dealer = input("Vad heter dealerna idag? \nDealer namn: ")
        self.dealer = Dealer(dealer)
        print("\nVälkommen " + name + " och lycka till!!\n" + "-- " + dealer + " är dealer idag")


    def status(self): #visa status
        print("\nDitt status:", self.player)

    def dealer_draw_cards(self):
        for i in range(2):
            self.dealer.draw_card(self.dealer, self.deck)
            self.dealer.draw_card(self.player, self.deck)
        print("\nUtdelade kort:")
        print("*"*28)
        print((self.player.get_name(), self.player.hand))
        print((self.dealer.get_name(), self.dealer.hand.get_first_card()))






class Player(CardPlayer):
    def __init__(self, name, money):
        self.balance = money #från play metod ange player insatts
        super().__init__(name) #från play metod ange player namn

    def get_balance(self):
        return self.balance 

    def add_money(self, money):
        self.balance += money #lägg till pengar
        return self.balance #skriv ut ny balance

    def remove_money(self, money):
        self.balance -= money #tar bort pengar
        return self.balance #skriv ut ny balance

    def __str__(self):
        return "Namn: {}, Pengar: {}".format(self.name, self.balance)







class Dealer(CardPlayer):  
    def __init__(self, name):  
        super().__init__(name) #från play metod ange player namn

    def draw_card(self, player, deck):
        player.hand.add_card(deck.take_card())






class Deck(BlackJack):
    def __init__(self):
        self.cards = self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        cards = [] #tom list för kort
        for i in range(52): #lägg till kort i listan, kortnummer 1-52
            cards.append(Card(i))
        return cards #print listan

    def shuffle_deck(self):
        random.shuffle(self.cards) #skuffa kort

    def take_card(self):
        return self.cards.pop() #print listan med random utdragen kort








game = BlackJack()
game.play()
