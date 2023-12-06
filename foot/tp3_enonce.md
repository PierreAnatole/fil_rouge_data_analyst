## UPDATE :  TP Football Total

Une dernière mission en urgence vient d'arriver dans les locaux de votre entreprise, il s'agit d'un sous traitant de la league européenne de footbal qui s'appelle Total football.

Cette société est spécialisée dans le conseil aux clubs de football et dans la traitement de données statistiques en vue d'améliorer les datas dans le footbal.

Il voudrait que vous l'aidiez dans le traitement de données des championnats européens sur des points biens précis.

Il ne dispose que d'un fichier sous forme sqli : https://mohamed-compartiment-neosoft.s3.amazonaws.com/database.sqlite

Vous pouvez l'ouvrir et y accéder avec : https://inloop.github.io/sqlite-viewer/

Dans ce fichier, vous disposez de tables et de données sous format sql.
Elle contient des données pour des matchs de football, des joueurs et des équipes de plusieurs pays européens de 2008 à 2016.

Vous aurez besoin d'extraire ces données dans des dataframes. Il faudra probablement effectuer des jointures entre tables pour certains dataframes.

La société Total Football a besoin de récupérer et d'obtenir un certain nombre d'information.

Voici leurs demandes : 

 1 - <b>Quelles équipes se sont le plus améliorées au cours de la période? </b> Sur ces critères : buildUpPlaySpeed, buildUpPlayDribbling, buildUpPlayDribblingClass	buildUpPlayPassing, chanceCreationPassing, chanceCreationCrossing	chanceCreationShooting, defencePressure, defenceAggression et	defenceTeamWidth. Il voudrait un histogramme par critères qui retourne les 5 meilleures equipes. Et enfin un histogramme global qui retourne le total pour les 5 meilleures equipes sur tous les critères.

 2 - <b>Qui est le meilleur joueur en penalties ?</b>


 3 - <b>Quels facteurs mènent aux plus de victoires ?</b> Comme par exemple l'impact de jouer à domicile ou à l'extérieur. Et enfin, est ce que certains attributs des equipes peuvent être determinants dans la victoire.




