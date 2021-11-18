# Analyse en composantes principales
Je vais faire une analyse en composantes principales des performances d'athlètes olympiques au décathlon.
Ce jeu de données contient 41 entrées, qui décrivent chacune les performances d'un athlète à une compétition de décathlon. Je vais faire une ACP des dix variables décrivant les performances à chacune des épreuves du décathlon (100 mètres, saut en hauteur, lancer de poids, saut en hauteur, 400 mètres, 110 mètres haies, lancer de disque, saut à la perche, javelot, et 1500 mètres).

## 1- Importation des données
Dans un premier temps, nous importons le tableau des individus et variables actifs X (xij ; i =    1,…,n, nombre d’observations ; j = 1,…,p, nombre de variables) pour la construction des axes factoriels. Nous utilisons la librairie Pandas.


