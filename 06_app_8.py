import random

palette = ["blanc", "rouge", "bleu", "vert", "noir", "violet", "orange"]

class Fantome:
    couleur = None
    def __init__(self):
        self.couleur = random.choice(palette)

fantomes = []
for i in range(100):
    fantomes.append(Fantome().couleur)

for coul in sorted(set([i for i in fantomes])):
   print(coul + " : " + str(fantomes.count(coul)))