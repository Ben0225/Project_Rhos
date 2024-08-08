# **Interprétation des Instructions**

Il est demandé de réaliser les tâches suivantes :

- **Expliquer chaque colonne :** Analyser ce que chaque colonne représente en fonction des données disponibles et des descriptions.
- **Trouver les 3 personnes les plus riches :** Identifier la colonne représentant la richesse (probablement une colonne avec des valeurs numériques) et trouver les trois valeurs les plus élevées.

## **Manipulation des Données**

Pour manipuler les données, utilisez des outils de la bibliothèque standard de Python, tels que `csv`, pour analyser le fichier. Vous pouvez lire le fichier ligne par ligne et extraire les informations nécessaires pour l'analyse.

## **Résultats**

### **`data.py`**

Ce script est conçu pour :

1. **Vérification de l'existence du fichier :** Le code vérifie si un fichier spécifié est présent dans le répertoire.
2. **Lecture et Affichage des Données :** Une fois le fichier trouvé, le script lit les premières lignes du fichier CSV et les affiche. Par défaut, il affiche un maximum de 100 lignes pour éviter une surcharge d'affichage dans le cas où le fichier est volumineux.
3. **Gestion des Erreurs :** En cas d'échec lors de l'ouverture ou de la lecture du fichier, un message d'erreur est affiché pour informer l'utilisateur.

### **Description des Colonnes**

Les données sont structurées en 7 colonnes, chacune représentant une information spécifique :

- **`a` :** Un identifiant ou index pour chaque enregistrement, démarrant à 0 et augmentant de 1 pour chaque ligne.
- **`b` :** Une description textuelle associée à chaque enregistrement, souvent sous forme de chaînes comme "longue description 0", "longue description 1", etc.
- **`c` :** Prénom de la personne.
- **`d` :** Nom de famille.
- **`e` :** Un montant associé à chaque enregistrement, qui pourrait représenter une valeur monétaire ou un score.
- **`f` :** Une autre mesure ou valeur associée, souvent égale à zéro mais parfois négative, suggérant qu’il pourrait s’agir de dettes.
- **`g` :** Ce champ semble correspondre à la somme des valeurs des colonnes `e` et `f`. On pourrait l'interpréter comme représentant la fortune nette.

### **`find_top_3_richest.py`**

Ce script traite les données pour identifier les trois personnes les plus riches en fonction de la colonne `g`. Le traitement peut prendre un temps plus ou moins long en fonction des capacités des serveurs. Il est également possible de traiter les données par blocs pour éviter de surcharger la mémoire RAM.
Enfin, en sortie, le script identifie les trois personnes les plus riches en fonction de la somme de la colonne `g` que nous avons considérée. Les trois personnes les plus riches sont :

- **Zoé Walliand** : 893 338 574.0
- **Gerard Parmentier** : 891 964 976.0
- **Océane Urbain** : 891 870 971.0

