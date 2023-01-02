## uitleg maken over de verschillende codes en modellen

Hoe is de testdata samengesteld?
Hoe te gebruiken met de daadwerkelijke data?

##stats
gemaakt met visual studio 
versie
Python versie.. 

Packages welke nodig zijn voor de uitvoering

## Link naar de database


## Algoritmes
Er zijn verschillende machine learning-algoritmes die geschikt zijn voor het binair classificeren van data.
voor dit project heb ik 4 verschillende algoritmes getest opdezelfde testdata. Hieronder geef ik een samenvatting weer en de accuracy score van het algoritme.

### KNN neigbors algoritme
K-nearest neighbors (KNN): Dit algoritme werkt door te kijken naar de K (meestal 5 of 10) "dichtstbijzijnde" datapunten
en te classificeren op basis van de meerderheid van de categorieën van deze punten.

Accuracy op testdata: 63% - 68 %

###Logistische regressie
Dit is een lineaire model dat wordt gebruikt om de kans te berekenen dat een datapunt tot een bepaalde categorie behoort.
Het is een populaire keuze voor binair classificeren omdat het gemakkelijk te begrijpen is en snel te trainen is.

Accuracy op testdata: 63% - 68 %

###SVM
Support Vector Machines (SVM): Dit is een algoritme dat traint op een hyperplane die de twee categorieën van data het beste scheidt. 
Het is een krachtig algoritme dat goede prestaties kan behalen, vooral als de data niet perfect lineair scheidbaar is.

Accuracy op testdata: 75% - 78%

###Decision tree
Dit algoritme bouwt een boomstructuur met beslissingspunten op basis van de kenmerken van de data, 
zodat het gemakkelijk is om nieuwe datapunten te classificeren.

Accuracy op testdata 94% - 97%

##Advies
Decision tree is het beste te gebruiken voor het classificeren van kans en doorstroomwijken. 

# Sla het model op in het bestand 'decision_tree_model.pkl'
joblib.dump(model, 'decision_tree_model.pkl') Dit moet toegevoegd worden aan de ml code om de code toe te passen

