import datetime

class Personne:
    def __init__(self, annee_naissance: int, nom: str, prenom: str):
        self.annee_naissance = annee_naissance
        self.nom = nom
        self.prenom = prenom
    
    def data(self)->dict:
        return vars(self)
    
    def etat_civil(self)->str:
        return (f'{self.prenom} {self.nom}')
    
    def age(self)->int:
        annee_courante = datetime.datetime.now().year
        age = annee_courante - self.annee_naissance
        return age
 
michou = Personne(1966, "Dupont", "Jean")
print(michou.data())
print(michou.etat_civil())
print(michou.age())
