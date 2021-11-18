# Analyse en composantes principales
Je vais faire une analyse en composantes principales des performances d'athlètes olympiques au décathlon.
Ce jeu de données contient 41 entrées, qui décrivent chacune les performances d'un athlète à une compétition de décathlon. Je vais faire une ACP des dix variables décrivant les performances à chacune des épreuves du décathlon (100 mètres, saut en hauteur, lancer de poids, saut en hauteur, 400 mètres, 110 mètres haies, lancer de disque, saut à la perche, javelot, et 1500 mètres).

## 1- Importation des données
Dans un premier temps, nous importons le tableau des individus et variables actifs X (xij ; i =    1,…,n, nombre d’observations ; j = 1,…,p, nombre de variables) pour la construction des axes factoriels. Nous utilisons la librairie Pandas.
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/1.png"> <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/2.png"><br>
## 2- Préparation des données
Je dois explicitement centrer et réduire les variables pour réaliser une ACP normée avec PCA. Nous utilisons la classe StandardScaler pour ce faire. Ici aussi, il est important de vérifier la version de ‘’scikit- learn’’ utilisée.
 J’instance l’objet et nous l’appliquons sur la matrice X. Nous obtenons une matrice Z: <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/3.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/4.png"> <br>
 Vérifions, par acquit de conscience, les propriétés du nouvel ensemble de données. 
 <ul>
  <li>	Les moyennes sont maintenant nulles (aux erreurs de troncature près) </li>
  <li>	Et les écarts-type unitaires.</li>
  <ul>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/5.png"> <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/6.png"> <br>

## 3-	Analyse en composantes principales avec ACP de ‘’scikit-learn’’
   
    ### a. Instanciation et lancement des calculs
    Il faut instancier l’objet PCA dans un premier temps, nous affichons ses propriétés.
La fonction fit_transform() renvoie en sortie les coordonnées factorielles Fik que je collecte dans la variable coord. J’affiche le nombre de composantes générées (K), il est bien égal à p = 10. <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/7.png"> <br>
    ###  b.	Valeurs propres
La propriété .explained_variance_ semble faire l’affaire pour obtenir les variances (valeurs propres, λk) associées aux axes factoriels.
J’aurai pu obtenir les bonnes valeurs propres en passant par les valeurs singulières .singular_values_ issues de la factorisation de la matrice des données centrées et réduites. <br>
    <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/8.png"> <br>


