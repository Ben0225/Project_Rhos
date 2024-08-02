import csv

def find_richest(filename, header_lines=8):
    richest_people = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for _ in range(header_lines):
            next(reader)

        # Déterminer l'index de la colonne représentant la richesse
        header = next(reader)
        g_index = 6

        for row in reader:
            # Extraire le nom complet (prénom et nom) en concaténant les colonnes 2 et 3
            full_name = f"{row[2]} {row[3]}"
            wealth = float(row[g_index])

            if full_name not in [name for name, _ in richest_people]:
                # Ajouter la personne à la liste des plus riches si cette dernière n'a pas encore les 03 personnes
                if len(richest_people) < 3:
                    richest_people.append((full_name, wealth))
                    richest_people.sort(key=lambda x: x[1], reverse=True)
                else:
                    if wealth > richest_people[-1][1]:
                        richest_people.pop()
                        richest_people.append((full_name, wealth))
                        richest_people.sort(key=lambda x: x[1], reverse=True)

    return richest_people



filename = r"C:\Users\DELL\Downloads\data\-"  # Remplacer par le chemin complet de votre fichier
richest = find_richest(filename)

print(richest)
