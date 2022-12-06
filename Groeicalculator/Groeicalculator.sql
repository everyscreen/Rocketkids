--- eerste CTE ophalen van gegevens
WITH cte_populatie  as (
	-- Selecteren van de bron 
	Select  [kwb-2022].gm_naam, [kwb-2020].a_inw as  a_inw20, [kwb-2021 ].a_inw as a_inw21, [kwb-2022 ].a_inw as a_inw22

	-- Inner join uitvoeren op basis van de 2 sleutel colommen (gwb_10 en gwb_8) Nederland excluden
		from dbo.[kwb-2022] 
	-- Inner join op basis van gemeente en converteren naar varchar
			inner join [kwb-2021 ] on CONVERT(varchar(50), [kwb-2022].gwb_code_8) = [kwb-2022].gwb_code_8 and [kwb-2022].gwb_code_10  = [kwb-2021 ].gwb_code_10
			inner join [kwb-2020]  on CONVERT(varchar(50), [kwb-2022].gwb_code_8) = [kwb-2022].gwb_code_8 and [kwb-2022].gwb_code_10  = [kwb-2020 ].gwb_code_10
	-- Nederland Excluden	
		Where not [kwb-2022].gm_naam = 'Nederland'
),
	-- Getallen casten als 'decimaal' voor de verhoudingsberekening
getal as (
		Select gm_naam, CAST(NULLIF([a_inw20],'') AS decimal(13,2)) as inwoners2020, CAST(NULLIF([a_inw21],'') AS decimal(13,2)) as inwoners2021, CAST(NULLIF([a_inw22],'') AS decimal(13,2)) as inwoners2022
		from cte_populatie
	-- Windowen op basis van gemeente en daar de totaal berekening op uitvoeren.
),
cteinwoners as (

Select   distinct gm_naam,			(sum(inwoners2020) over
		(partition by gm_naam ))
				as Populatie_2020,  
									(sum(inwoners2021) over
		(partition by gm_naam ))
				as Populatie_2021,
									(sum(inwoners2022) over
		(partition by gm_naam ))
				as Populatie_2022
	From getal)

		-- De verhoudingen berekenen voor de compound calculatie

Select gm_naam, 
																Populatie_2020 * 100/ SUM(Populatie_2020) over()  as 'Verhouding2020',
																Populatie_2021 * 100/ SUM(Populatie_2021) over()  as 'Verhouding2021',
																Populatie_2022 * 100/ SUM(Populatie_2022) over()  as 'Verhouding2022'
from cteinwoners


-- Unpivot tabelP

------Populatie_2020) FROM cteinwoners)