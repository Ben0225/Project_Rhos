Interpréter les Instructions :

Il est démandé de : 

*Expliquer chaque colonne : Analyser ce que chaque colonne représente en fonction des données disponibles et des descriptions.
*Trouver les 3 personnes les plus riches : Identifiez la colonne représentant la richesse (probablement une colonne avec des valeurs numériques) et trouvez les trois valeurs les plus élevées.

*Manipulation des Données :

Utilisez des outils de la bibliothèque standard de Python, comme csv, pour analyser les données. On pourra lire le fichier ligne par ligne et extraire les informations nécessaires.



Résultats
data.py : Ce code est conçu pour vérifier si un fichier spécifié existe, puis lire et afficher les premières lignes de ce fichier CSV. 
Il affiche un maximum de 100 lignes (au choix) pour éviter une surcharge d'affichage si le fichier est très grand. 
En cas d'erreur lors de l'ouverture ou de la lecture du fichier, un message d'erreur est affiché.

*Les colonnes sont au nombre de  7: 'a' , 'b' ,'c' , 'd' , 'e' , 'f', 'g'

'a' : Un identifiant ou un index pour chaque enregistrement qui démarre de 0 et augmente de 1 pour chaque ligne.
'b' : Une description textuelle associée à chaque enregistrement. Ces descriptions semblent être des chaînes comme "longue description 0", "longue description 1", etc.
'c' : Prénom de la personne
'd' : Nom de famille
'e' : Montant associé à chaque enregistrement,peut être une sorte de valeur monétaire ou de score.
'f' : Une autre mesure ou valeur associée, qui semble souvent être zéro mais parfois négatif. On pourrait penser à des dettes.
'g' : Cela correspond généralement à la somme des valeurs dans les colonnes e et f; on pourrait se positionner en disant qu'il s'agit de la fortune.


A l'issu de l'excécution du fichier find_top_3_richest.py, on a des blocs de traitement de lignes spécifiques qui renvoie les trois personnes riches de chaque bloc (dans notre cas, nous avions choisi 10 000 000 lignes).

Enfin, on se retrouve avec moins de personnes ce qui nous permet de dire que les trois personnes les plus riches sont : 


