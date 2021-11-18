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
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/9.png"> <br>
pca.explained_variance_ratio_ nous donne le pourcentage de variance expliquée par chacune des composantes.
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/10.png"> <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/11.png"> <br>   
La première composante accapare 32.7% de l’information disponible et la deuxième 17.3%. Au total, ces deux composantes expliquent 50% de la variance totale, en utilisant seulement un cinquième des dimensions initiales.  Je peux représenter chaque athlète/compétition selon ces deux dimensions uniquement.
### c.	Détermination du nombre de facteur à retenir
Les seuils sont définis par : 
         𝑏𝑘=∑_(m=k)^p▒1/m 
Le facteur n°k est validé si (λk > bk), où λk est la valeur propre associée à l’axe n°k. 
Je ces seuils, puis j’affiche les valeurs propres et les seuils. <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/12.png"> <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/13.png"> <br>
Avec cette procédure, seul le premier facteur est valide. Le cercle des corrélations que nous construirons par la suite (Figure 5) semble aller dans le même sens.
Néanmoins, par commodité (pas seulement en réalité, cette étude est plus subtile qu’elle n’en a l’air), nous choisissons K* = 2 pour pouvoir représenter les individus et les variables dans le plan.
### d.	Représentation des individus – Outils pour l’interprétation
   
<ul>
 <li>Coordonnées factorielles </li>
 Les coordonnées factorielles (Fik) des individus ont été collectées dans la variable coord calculés précédemment.

On remarque dans le graphique que les dispersions des individus sont nettement plus marquées sur le premier axe, en abscisse.
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/14.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/15.png"> <br>
 <li>Qualité de représentation – Les COS²</li>
 Pour calculer la qualité de représentation des individus sur les axes, nous devons d’abord calculer les carrés des distances à l’origine des individus, qui correspondent également à leur contribution dans l’inertie totale.
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/16.png"> <br>
 Concrètement, « Casarsa », « Karpov » et « Sebrle » sont les trois athlètes qui se démarquent le plus des autres, et on les retrouve aux extrémités du premier axe factoriel qui porte 50% de l’information disponible. <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/17.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/18.png"> <br>
 Nous pouvons alors déduire la qualité de représentation des individus sur l’axe n°k. Les COS² pour les deux premiers facteurs sont affichés <br>
  <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/19.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/20.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/21.png"> <br>
 <li>Contribution des individus aux axes</li>
  <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/22.png"> <br>
 Sans surprises, ce sont « Karpov » et « Sebrle » qui sont déterminants pour le premier axe ; pour le second, on a «Casarsa» et «Drews ». <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/23.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/24.png"> <br>
   </ul>
### e-	Représentation des variables – Outils pour l’aide à l’interprétation <br>
J’ai besoin des vecteurs propres pour l’analyse des variables. Ils sont fournis par le champ .components_ <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/25.png"> <br>
 <img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/26.png"> <br>
Je dois en tenir compte pour obtenir les corrélations (variables x facteurs, 𝑟𝑗𝑘) en les multipliant par la racine carrée des valeurs propres <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/27.png"> <br>
Les variables sont maintenant en ligne, les facteurs en colonne : <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/28.png"> <br>
   Si l’on s’en tient spécifiquement aux deux premiers facteurs <br>
<img src="https://github.com/mouna0404/ACP/blob/4ceb5ec471e8ed1517822d43562d18b835922031/imgs/29.png"> <br>
