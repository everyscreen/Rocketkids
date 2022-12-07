### **Advies Rocket-dashboard implementatie op  SQL server niveau**
*Voor kleine bedrijven raden we aan om de Excel variant van  het dashboard aan.*

#Indien je een SQL omgeving hebt of een wilt opzettenm  is deze markdown de juiste.



##1. hoe zet ik een SQL omgeving op? 
Ons advies om de kosten laag te houden is door de SQL express editie te downloaden voor op uw computer of server.
https://www.microsoft.com/nl-nl/sql-server/sql-server-downloads
De express editie is niet alleen  gratis, maar goed te gebruiken op locale computers.
Doorloop de installatie en kies voor basic indien u alleen de standaard functies wilt gebruiken.
Kies een naam  voor de database en ga naar stap 2

###Requirements SQL express omgeving:
De computer dient op het zelfde subnet te zitten als voor iedereen die de rapportage wilt laden, tenzij je webservices wilt gebruiken.
De computer heeft een statisch ip adres nodig op het netwerk
De bovenste requirements gelden niet als je alleen met de localhost wilt verbinden. IP:127.0.0.1 Resolutionname:computernaam
Minimaal 10GB aan schijf geheugen voor de database.

Verdere specificaties voor de SQL express omgeving:
Component	Requirement
Hard Disk	SQL Server requires a minimum of 6 GB of available hard-disk space.

Disk space requirements will vary with the SQL Server components you install. For more information, see Hard Disk Space Requirements later in this article. For information on supported storage types for data files, see Storage Types for Data Files.
Monitor	SQL Server requires Super-VGA (800x600) or higher resolution monitor.
Internet	Internet functionality requires Internet access (fees may apply).
Memory *	Minimum:
Express Editions: 512 MB
All other editions: 1 GB
Recommended:
Express Editions: 1 GB
All other editions: At least 4 GB and should be increased as database size increases to ensure optimal performance.
Processor Speed	Minimum: x64 Processor: 1.4 GHz
Recommended: 2.0 GHz or faster
Processor Type	x64 Processor: AMD Opteron, AMD Athlon 64, Intel Xeon with Intel EM64T support, Intel Pentium IV with EM64T support

##2. Hoe verbind ik met mijn database
Download SQL servermanagementstudio SMSS https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16
Wanneer u de installatie voltooid heeft kunt u uw  eigen computernaam invullen als server. Hiervoor moet de SQL server wel actief zijn na installatie

##3. importeren database
In de SQL servermanagementstudio kunt u een database importeren. Die kunt u downloaden uit de database URL in de GIT
Kies voor importeren en vervolgens de server waarnaar de import toe mag. Indien u stap 1  en 2 gedaan heeft is dat de localhost.
Wij raden aan om  de database naam hetzelfde te laten **RocketV3**

##4. verbinden met de SQL Server vanuit powerbi
Indien u een lokaal netwerk heeft zonder Vlans raden wij aan om vanuit powerbi de computernaam in te vullen bij het importeren van de SQL data en dan de databasenaam te gebruiken.

###Indien u niet op het zelfde subnet zit,  maar bijvoorbeeld op afstand wilt werken aan de database.

Het is mogelijk om vanuit de SQL express applicatie de webservices aan te zetten en uw computer als  webserver te laten functioneren. Hier hangen Risiso's aan vast vanwege het moeten instellen van een Port forward.
Wij raden aan om de volgende  stappen door een  IT profesional  uit te laten voeren, dit is op  uw  eigen risico.

1. De router op het netwerk zal een sql poort moeten forwarden
2. De firewall moet SQL  communicatie naar binnen moeten laten en uit kunnen sturen
3. de machine moet opgeroepen  kunnen  worden vanuit het externe IP adress
Een handleiding  is hieronder beschikbaar.
https://www.cloudfronts.com/uncategorized/making-sql-server-accessible-over-internet/
