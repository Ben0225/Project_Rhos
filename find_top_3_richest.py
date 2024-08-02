import csv

def find_richest_by_blocks(filename, block_size=10000000, header_lines=8):
    richest_people = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for _ in range(header_lines):
            next(reader)

        # Déterminer l'index de la colonne représentant la richesse
        header = next(reader)
        g_index = 6

        block_count = 0
        block_number = 1
        for row in reader:
            block_count += 1
            # Extraire le nom complet (prénom et nom) en concaténant les colonnes 2 et 3
            full_name = f"{row[2]} {row[3]}"
            wealth = float(row[g_index])

            if full_name not in [name for name, _ in richest_people]:
                # Ajouter la personne à la liste des plus riches si elle est plus riche que les 3 premières
                if len(richest_people) < 3:
                    richest_people.append((full_name, wealth))
                    richest_people.sort(key=lambda x: x[1], reverse=True)
                else:
                    if wealth > richest_people[-1][1]:
                        richest_people.pop()
                        richest_people.append((full_name, wealth))
                        richest_people.sort(key=lambda x: x[1], reverse=True)
           

            if block_count == block_size:
                # Sauvegarder les 3 personnes les plus riches du bloc 
                print(f"Bloc {block_number}: {richest_people}")

                # Réinitialiser la liste pour le prochain bloc
                richest_people = []
                block_count = 0
                block_number += 1

    # Traiter les éventuelles personnes restantes après le dernier bloc
    if richest_people:
        print(f"Dernier bloc: {richest_people}")


    return richest_people

# Exemple d'utilisation :
filename = r"C:\Users\DELL\Downloads\data\-"  # Remplacer par le chemin complet de votre fichier
richest = find_richest_by_blocks(filename)
