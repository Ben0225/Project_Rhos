import os
import csv

path = r"C:\Users\DELL\Downloads\data\-"
if os.path.exists(path):
    print("Le fichier existe.")
else:
    print("Le fichier n'existe pas.")






try:
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file) #Crée un objet lecteur CSV qui itère sur les lignes du fichier
        count = 0
        max_lines = 100  # Définissez le nombre maximum de lignes à afficher
        for row in reader:
            print(row)
            count += 1
            if count >= max_lines:
                break
except Exception as e:
    print(f"Erreur lors de la lecture du fichier : {e}")



