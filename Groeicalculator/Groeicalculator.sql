
WITH cte_populatie  as (
	-- Selecteren van de bron 
	Select  [kwb-2022].gm_naam, [kwb-2020].a_inw as  a_inw20, [kwb-2021 ].a_inw as a_inw21, [kwb-2022 ].a_inw as a_inw22

	-- Inner join uitvoeren op basis van de 2 sleutel colommen (gwb_10 en gwb_8)
	from dbo.[kwb-2022] 

	inner join [kwb-2021 ] on CONVERT(varchar(50), [kwb-2022].gwb_code_8) = [kwb-2022].gwb_code_8 and [kwb-2022].gwb_code_10  = [kwb-2021 ].gwb_code_10
	inner join [kwb-2020]  on CONVERT(varchar(50), [kwb-2022].gwb_code_8) = [kwb-2022].gwb_code_8 and [kwb-2022].gwb_code_10  = [kwb-2020 ].gwb_code_10

) 

--Percentage berekening
Select gm_naam,   a_inw20,  
	From cte_populatie
	




-----Rommelbak--------
---a_inw20 * 100/(SELECT SUM(a_inw20) FROM cte_populatie) as 'Percentage of Total20',
---(INTO NewTable)