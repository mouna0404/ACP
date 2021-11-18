#librairie pandas 
import pandas
#chargement de la première feuille de données
data = pandas.read_csv("decathlon.txt",sep='\t')
# éliminer les colonnes que nous n'utiliserons pas
X = data.drop(['Points', 'Rank', 'Competition'], axis=1)
print(X)
#dimension
n = X.shape[0] #nombre d'observations 
p = X.shape[1] #nombre de variables 

#scikit-learn 
import sklearn
#classe pour standardisation
from sklearn.preprocessing import StandardScaler
#instanciation 
sc = StandardScaler() 
#transformation – centrage-réduction
Z = sc.fit_transform(X) 
print(Z)
#vérification - librairie numpy 
import numpy 
#moyenne
print(numpy.mean(Z,axis=0)) 
#écart-type
print(numpy.std(Z,axis=0,ddof=0))
#classe pour l'ACP 
from sklearn.decomposition import PCA 
#instanciation 
acp = PCA(svd_solver='full')
#calculs 
coord = acp.fit_transform(Z) 
#nombre de composantes calculées 
print(acp.n_components_)
#variance expliquée 
print(acp.explained_variance_)
#corrigé les valeurs en passant par les valeurs singulières 
print(acp.singular_values_**2/n)
eigval = (n-1)/n*acp.explained_variance_
#proportion de variance expliquée 
print(acp.explained_variance_ratio_)
#seuils pour test des bâtons brisés 
bs = 1/numpy.arange(p,0,-1) 
bs = numpy.cumsum(bs) 
bs = bs[::-1]
#test des bâtons brisés 
print(pandas.DataFrame({'Val.Propre':eigval,'Seuils':bs}))
import matplotlib.pyplot as plt
#positionnement des individus dans le premier plan 
fig, axes = plt.subplots(figsize=(12,12)) 
axes.set_xlim(-6,6) 
#même limites en abscisse 
axes.set_ylim(-6,6) #et en ordonnée

#placement des étiquettes des observations 
for i in range(n): 
    plt.annotate(X.index[i],(coord[i,0],coord[i,1])) 
#ajouter les axes 
plt.plot([-6,6],[0,0],color='silver',linestyle='-',linewidth=1) 
plt.plot([0,0],[-6,6],color='silver',linestyle='-',linewidth=1) 
#affichage 
plt.show()
#contribution des individus dans l'inertie totale 
di = numpy.sum(Z**2,axis=1) 
print(pandas.DataFrame({'ID':X.index,'d_i':di}))
#qualité de représentation des individus - COS2 
cos2 = coord**2 
for j in range(p): 
    cos2[:,j] = cos2[:,j]/di 
print(pandas.DataFrame({'id':X.index,'COS2_1':cos2[:,0],'COS2_2':cos2[:,1]}))
#contributions aux axes 
ctr = coord**2 
for j in range(p): 
    ctr[:,j] = ctr[:,j]/(n*eigval[j]) 
print(pandas.DataFrame({'id':X.index,'CTR_1':ctr[:,0],'CTR_2':ctr[:,1]}))
#le champ components_ de l'objet ACP 
print(acp.components_)
#racine carrée des valeurs propres 
sqrt_eigval = numpy.sqrt(eigval)
#corrélation des variables avec les axes 
corvar = numpy.zeros((p,p)) 
for k in range(p): 
    corvar[:,k] = acp.components_[k,:] * sqrt_eigval[k] 
#afficher la matrice des corrélations variables x facteurs 
print(corvar)
#on affiche pour les deux premiers axes 
print(pandas.DataFrame({'id':X.columns,'COR_1':corvar[:,0],'COR_2':corvar[:,1]}))
#cercle des corrélations 
fig, axes = plt.subplots(figsize=(8,8)) 
axes.set_xlim(-1,1) 
axes.set_ylim(-1,1)
#corrélation des variables avec les axes 
corvar = numpy.zeros((p,p)) 
for k in range(p): 
   corvar[:,k] = acp.components_[k,:] * sqrt_eigval[k]
#affichage des étiquettes (noms des variables) 
for j in range(p): 
    plt.annotate(X.columns[j],(corvar[j,0],corvar[j,1]))
#ajouter les axes 
plt.plot([-1,1],[0,0],color='silver',linestyle='-',linewidth=1) 
plt.plot([0,0],[-1,1],color='silver',linestyle='-',linewidth=1)

#ajouter un cercle 
cercle = plt.Circle((0,0),1,color='blue',fill=False) 
axes.add_artist(cercle) 
#affichage 
plt.show()
#cosinus carré des variables 
cos2var = corvar**2 
print(pandas.DataFrame({'id':X.columns,'COS2_1':cos2var[:,0],'COS2_2':cos2var[:,1]}))
#contributions 
ctrvar = cos2var 
for k in range(p): 
    ctrvar[:,k] = ctrvar[:,k]/eigval[k] 
#on n'affiche que pour les deux premiers axes 
print(pandas.DataFrame({'id':X.columns,'CTR_1':ctrvar[:,0],'CTR_2':ctrvar[:,1]}))







