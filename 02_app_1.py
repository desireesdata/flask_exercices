import os

# 1. Afficher le chemin du dossier courant 
path = os.getcwd() #chemin absolu
print(path)

# 2. Afficher le nom du répertoire courant
current_dir = os.path.basename(path)
print(current_dir, os.path)
# On peut aussi utiliser le chemin absolu, sans utiliser la méthode basename :
current_dir = path.split("/")
current_dir = current_dir[-1]
print(current_dir)

# 3. Créer un répertoire dans celui courant sans os.system.
new_dir = "joli_dossier"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"{new_dir} apparait ! :)")
else :
    print(f"{new_dir} n'a pas besoin d'être crée")

# 4. Supprimer le nouveau dossier
if os.path.exists(new_dir):
    os.rmdir(new_dir)
    print(f"{new_dir} a été supprimé sans vergogne:(")

# 5. Lister les fichiers et les dossiers parents
# print(os.system("ls")) #Compatible pour les système UNIX. Affichage sur la sortie standard
print("Répertoire parent :", current_dir)
fichiers = os.listdir(path)
for element in fichiers:
    print(f"Fichier dans le dossier {current_dir} : {element}")