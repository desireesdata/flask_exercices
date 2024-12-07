"""
Exercices app3 à app7
"""

class Livre:
    #attribut de classe
    nombre_editions = 1

    def __init__(self, titre, auteur, annee_publication):
        self.nombre_editions += 1 #incrémentation à chaque instanciation
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.commentaires = []
    def display_data(self):
        print(f"{self.titre} par {self.auteur}, publié en {self.annee_publication}")
    def get_nombre_editions(self):
        print(self.nombre_editions)
    def eq(self, Livre):
        if vars(self) == vars(Livre):
            print("les livres sont pareils")
        else :
            print("les livres sont différents")
    def ajouter_commentaire(self, commentaire:str)->str:
        self.commentaires.append(str(commentaire))
    def afficher_commentaires(self):
        print(self.commentaires)

# Je choisis de stocker mes livres dans une liste pour pouvoir tester mes fonctions 
# dans une seule boucle et sur tous les objets instanciés 
livres = []
livres.append(Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954))
livres.append(Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954))
livres.append(Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1956))
livres.append(Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997))

for livre in livres:
    livre.display_data()
    livre.get_nombre_editions()

# Compare deux livres
livres[0].eq(livres[1])
livres[1].eq(livres[2])

# Ajouter des commentaires à un livre
livres[-1].ajouter_commentaire("Super livre, mais Voldemort est mal écrit")
livres[-1].ajouter_commentaire("Pas mal... mes enfants adorent Harry Potter.... et moi aussi")
livres[-1].afficher_commentaires() #affiche les commentaires du dernier livre de la liste