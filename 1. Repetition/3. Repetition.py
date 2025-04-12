"""
På ett gym kan man antingen köpa ett årskort eller köpa en biljett vid varje besök. Skriv ett program som läser in priset för ett årskort, 
priset för en biljett samt antalet gånger man planerar att besöka gymmet under ett år. Därefter ska programmet ange om det lönar sig att 
köpa årskort eller inte. 
"""

#inmat av kostnader
månads_kort = int(input("Hur mycket kostar månadskort? ")) 
års_kort = int(input("Hur mycket kostar årskort? "))

#uträkning
månads_kostnad = månads_kort *12

#jämförelse
if månads_kostnad < års_kort:
    print("Det är billigare att köpa månadskort.")
else:
    print("Det är billigare att köpa årskort.")