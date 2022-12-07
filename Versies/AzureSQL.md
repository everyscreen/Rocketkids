#$Technische specificaties Azure SQL.  
##Volg de local SQL handleiding vanaf stap 3 indien je de database op je eigen AZure SQL server wilt
 

De huidige situatie: 

De BI  omgeving die opgezet wordt vereist een database die op afstand bereikt kan worden vanuit meerdere punten.  Microsoft is voor nu het gekozen platform omdat we Power bi gebruiken als front.  
 
De kosten en connectie opties liggen makkelijker binnen Azure.   Als er in de toekomst gekozen wordt voor een statische power bi omgeving in de Azure Cloud, dan kan de database op hetzelfde Vnet ingesteld worden. Dit geld niet alleen voor Power bi maar ook andere eindoplossingen die in de Cloud gehost kunnen worden. 

 

De SQL Database: 

Standard-series (Gen5) 

Provisioned compute 
- Intel® E5-2673 v4 (Broadwell) 2.3 GHz, Intel® SP-8160 (Skylake)*, Intel® 8272CL (Cascade Lake) 2.5 GHz*, Intel® Xeon Platinum 8307C (Ice Lake)*, AMD EPYC 7763v (Milan) processors 
- Provision up to 128 vCores (hyper-threaded) 
 
Serverless compute 
- Intel® E5-2673 v4 (Broadwell) 2.3 GHz, Intel® SP-8160 (Skylake)*, Intel® 8272CL (Cascade Lake) 2.5 GHz*, Intel Xeon® Platinum 8307C (Ice Lake)*, AMD EPYC 7763v (Milan) processors 
- Auto-scale up to 40 vCores (hyper-threaded) 

Provisioned compute 
- 5.1 GB per vCore 
- Provision up to 625 GB 
 
Serverless compute 
- Auto-scale up to 24 GB per vCore 
- Auto-scale up to 120 GB max 

Het product is een Prototype en dat geld ook voor de database. De database functioneert op 1VCore en 5GB aan storage. Beide kunnen uitgebreid worden, maar we werken  momenteel  vanuit een  koste besparend oogpunt. 
 
Dit zijn de specificaties  volgens het Cloud model: 
 

 
De Server maakt gebruik van een serverless environment i.v.m. met de opschaling. 

Softwarematig beschikt de SQL  server over de laatste versie van SQL  evergreen. Evergreen is een versie die alleen door Azure geprovioned wordt. 

 

 

 

Het netwerk: 

De SQL  server hangt direct aan een firewall die naar buiten communiceert. Gebruikers   met   de juiste credentials   kunnen aan de hand van een URL direct inloggen.  

 

URL: rockettheunsinkable.database.windows.net 

 

De firewall vereist Azure AD authenticatie om gebruikers toe te laten, en  de  SQL server werkt op SQL credentials. 
 

 

 