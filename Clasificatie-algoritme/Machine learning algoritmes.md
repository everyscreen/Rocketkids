##Inleiding
Wat is het probleem wat ik probeer op te lossen

Vanuit WIJZIJNJONG kwam de opdracht om wijken te classificeren in kanswijken en doorstroomwijken
Kanswijk:
Doorstroomwijk:

###Waarom machine learning?
Het is te arbeidsintensief om van alle wijken een berekening te gaan maken en deze te classificeren. 
Machine learning kan worden gebruikt om complexe processen te vereenvoudigen en ze toegankelijker te maken.
Met een kleine testdataset moet het met het juiste model eenvoudig te berekenen zijn en dat scheelt veel werk. 

## uitleg maken over de verschillende codes en modellen
###Dataset

Om de juiste classificatie te maken zijn er een aantal gegevens nodig.
    - Lijst van de gemeenten in nederland
    - Aantal jongeren per gemeente
    - Aantal kindplaatsen per gemeente

Deze gegevens staan in de dataset landelijk registratie kinderdagopvang en je kunt zelf via .. een dataset samenstellen met daarin relevante gegevens van de inwoners per gemeente. 
Ik heb de volgende query gebruikt om de juiste gegevens uit de dataset te halen:

- hoe heb ik de dataset samengesteld
Dataset LRK. Query gemaakt om het aantal kindplaatsen per gemeente te berekenen. 
Deze geexporteerd en samengevoegd met het aantal kinderen per gemeente

Vanuit de interviews met WIJZIJNJONG en de requirements die zijn opgesteld door KIFO zag ik dat de verhouding kinderen ten op zichte van kindplaatsen /3 was
Alles boven 1:3 wordt geclassificeert als Kanswijk
Alles onder 1:3 wordt geclassificeert als Doorstroomwijk

Ik heb een testdataset opgesteld waarin ik mockdata heb aangemaakt met de juiste verhouding. Hierop heb ik onderstaande algorites getest in Python

##stats
Bijgevoegde codes zijn gemaakt in Visual Studio
Python versie 3.10 (64-bit)

De volgende python packages moeten zijn geinstalleerd om de code te laten werken
(installatie kan via cmd, pip install (naam package))
pandas
scikit-learn 
numpy 
scipy 
matplotlib
joblib
pyodbc

## Link naar de database
server: marlies.database.windows.net
database:rocketdb2
user:rocketadmin@marlies
password:Marlies123!

## Algoritmes
Er zijn verschillende machine learning-algoritmes die geschikt zijn voor het binair classificeren van data.
Welk algoritme het beste werkt, hangt af van verschillende factoren, zoals de kenmerken van de data, 
het aantal te classificeren categorieën, de hoeveelheid beschikbare data en de prestatie-eisen voor het model. 
Sommige algoritmes zijn beter geschikt voor bepaalde soorten data en bepaalde soorten problemen dan andere.
Voor dit project heb ik 4 verschillende algoritmes getest opdezelfde testdata. Hieronder geef ik een samenvatting weer en de accuracy score van het algoritme.

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
joblib.dump(model, 'decision_tree_model.pkl') pkl bestand kopieren naar repository welke je gebruikt voor ML
PKL bestand moet toegevoegd worden aan de ml code om de code toe te passen

