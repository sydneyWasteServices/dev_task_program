USE JLL 
GO

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES;



-- ======================================================================
-- ======================================================================
-- To check Duplicate ID
WITH JoinTB as (
    SELECT 
        phub.[OVCP_ID], 
        progen.[Lease], 
        phub.[Property_Name], 
        progen.[Name], 
        phub.[Property_Status],
        progen.[Status],
        phub.[Address_2],
        progen.[Owner]
    FROM 
    dbo.[Property_hub] phub
    JOIN 
    dbo.[progen12-04-2022] progen
    ON
    phub.[OVCP_ID] = progen.[OVCP_ID_JLL_Interface]

), DupID AS(
    Select 
    [OVCP_ID], 
    COUNT([OVCP_ID]) COUNTING
    FROM 
    JoinTB
    GROUP BY 
    OVCP_ID
    HAVING COUNT([OVCP_ID])  > 1
)
    Select 
   *
    FROM 
        JoinTB tb
    JOIN
        DupID dup
    ON 
        tb.[OVCP_ID] = dup.[OVCP_ID]
-- ======================================================================
-- ======================================================================

-- ========================================================================================
SELECT
*
FROM 
dbo.[progen02-05-2022]

SELECT 
*
FROM 
dbo.[Property_hub]
WHERE
[Property_Status] <> 'InActive'

-- ========================================================================================
-- QLD - MURRUMBA DOWNS - Cnr Dohles Rocks and	Castle Hill Medical Centre	Active	17650579
-- QLD - MURRUMBA DOWNS - Cnr Dohles Rocks Rd 	Murrumba Downs Medical & Dental Centre(ForHealth)	Active	17650771
-- ========================================================================================
-- [Property_Name], [Property_Status]
SELECT 
[Property_Name],[Address_2], [Property_Status], [OVCP_ID]
FROM 
dbo.[Property_hub]
WHERE
[PROPERTY_NAME] LIKE '%146 Blunder%'
AND
    [Property_Status] = 'Active'
ORDER BY 
    [Address_2];

SELECT
    [LEASE],[Name], [Owner], [Status], [Component_Area_Leaseable]
FROM 
    dbo.[progen05-04-2022]
WHERE
    [Name] LIKE '%146 Blunder%'
ORDER BY
    [Name]
-- =====================================================================================

SELECT 
    *
FROM 
    dbo.[Property_hub]
WHERE 
    [E1_BU] in ('4849802104',
'4849802358','4849801515','4849800663','4849800580','4849801502','4849800504','4849800064','4849801895','4849801432',
'4849800049','4849803038','4849801048','4849802412','4849803064','4849800736','4849801558','4849803338','4849801328',
'4849803101',
'4849800545',
'4849801971',
'4849803280',
'4849800273',
'4849800914',
'4849800759',
'4849800193',
'4849800593',
'4849800410',
'4849802131',
'4849801460',
'4849801688',
'4849803286',
'4849802076',
'4849801222',
'4849803421',
'4849803049',
'4849802831')


select *
from
    dbo.[Property_hub]
where
    [RecordID] = '18046512'










-- [OVCP_ID], [Client_Property_Code], [E1_BU], [Property_Name], [Address_1], [Address_2], [Property_Size], [Reporting_Business_Unit]
--    in ('17650625', '17650776')
--    = '17650776' , 
-- * [LEASE],[Name], [Status], [OVCP_ID_JLL_INTERFACE] 
--     [RecordID] = 17650783
--    [OVCP_ID] = 17650720
    -- [OVCP_ID_JLL_Interface] = 17650720
-- [BU_Number] = 4849802733

SELECT
    * 
FROM 
    dbo.[progen09-05-2022] 
WHERE


SELECT
    *
FROM
    dbo.[Corrigo]
WHERE
   [Property_Name] LIKE '%2 Willow%' 

    [Customer_Number] = 4463

AND 
    [DBA] LIKE '%PSCP%'


Select 
    [OVCP_ID], [Client_Property_Code], [E1_BU], [Property_Name], [Address_1], [Address_2], [Property_Size], [Reporting_Business_Unit], [Property_Status]
From
    dbo.[Property_hub]
WHERE
    [Property_Name] LIKE '%201 Pacific%' 

    

-- 4849802427
-- 2426
-- 3516
-- 4849802384;4849800127
-- 17650783



-- WHERE 
-- [OVCP_ID_JLL_INTERFACE] = '17650776'
-- 18046458, 17650776, 17650625
-- [Lease] in ('6007707', '6007183', '6008266', '6008212', '6007237', '6007238')
-- ========================================================================================
-- ========================================================================================

-- ======================================================================
-- ======================================================================
-- **** Create a Parition Query ,  Check Same Value in Owner  ****
--  **** Find 

WITH JoinTB as (
    SELECT 
        phub.[OVCP_ID], 
        progen.[Lease], 
        phub.[Property_Name], 
        progen.[Name], 
        phub.[Property_Status],
        progen.[Status],
        phub.[Address_2],
        progen.[Owner]
    FROM 
    dbo.[Property_hub] phub
    JOIN 
    dbo.[progen11-04-2022] progen
    ON
        phub.[OVCP_ID] = progen.[OVCP_ID_JLL_Interface]
    WHERE
        progen.[Status] NOT LIKE '%Terminated%'
    AND
        phub.[Property_Status] <> 'InActive'

), DupID AS(
    Select 
    [OVCP_ID], 
    COUNT([OVCP_ID]) COUNTING
    FROM 
    JoinTB
    GROUP BY 
    OVCP_ID
    HAVING COUNT([OVCP_ID])  > 1
), PartID as (
    Select 
    tb.OVCP_ID,	
    tb.Lease,	
    tb.Property_Name,	
    tb.Name,	
    tb.Property_Status,	
    tb.Status,	
    tb.Address_2,	
    tb.Owner,
        ROW_NUMBER() OVER (
            PARTITION BY
                tb.[OVCP_ID],
                tb.[Owner]
            ORDER BY
                tb.[OVCP_ID]
        ) RowNumber
    FROM 
        JoinTB tb
    JOIN
        DupID dup
    ON 
        tb.[OVCP_ID] = dup.[OVCP_ID]
), DupBusUnit as (
SELECT 
    Distinct [OVCP_ID]     
FROM 
    PartID
WHERE  
    RowNumber > 1 
)SELECT
    *
FROM 
    JoinTB
JOIN
    DupBusUnit
ON 
    JoinTB.OVCP_ID = DupBusUnit.OVCP_ID
ORDER BY 
    JoinTB.[Property_Name], 
    JoinTB.[OWNER]
-- ============================================================================================================================================
-- ============================================================================================================================================

-- ============================================================================================================================================
-- ============================================================================================================================================
SELECT
    TOP 1 *
FROM
dbo.[Property_hub];

SELECT
    TOP 1 *
FROM
dbo.[progen12-04-2022];

-- ============================================================================================================================================
-- ============================================================================================================================================

WITH JOINTB AS (
SELECT 
    pro.[Lease] PROGEN_ID ,
    pro.[OVCP_ID_JLL_INTERFACE] PROGEN_ovcp_id,
    phub.[RecordID] phub_ovcp_id,
    pro.[Name] PROGEN_Name,
    phub.[Property_Name] phub_name,
    pro.[STATUS] PROGEN_STATUS,
    phub.[Property_Status] phub_status,
    value,
    lower(trim(phub.[State_Province])) phub_state,
    lower(trim(phub.[City])) phub_city,
    lower(trim(phub.[Address_1])) phub_addr,
    ROW_NUMBER() OVER(PARTITION by [Lease] order by [Lease]) as ROWNUM,
    pro.[Owner] bu_unit
FROM
    dbo.[progen27-04-2022] pro
JOIN 
    dbo.[Property_hub] phub
ON 
    pro.[OVCP_ID_JLL_Interface] = phub.[RecordID]
CROSS APPLY string_split(pro.[Name], '-')
), PROCESSED_TB AS (
    
SELECT
    PROGEN_ID,
    PROGEN_ovcp_id,
    phub_ovcp_id,
    PROGEN_Name,
    phub_name,
    PROGEN_STATUS,
    phub_status,
    phub_state,
    phub_city,
    phub_addr,
    LOWER(TRIM(replace([1],'#',''))) AS [PROGEN_STATE],
    LOWER(TRIM([2])) AS [PROGEN_CITY],
    LOWER(TRIM([3])) AS [PROGEN_STREET],
    bu_unit
FROM 
    JOINTB
PIVOT
(
    MAX(VALUE)
    FOR ROWNUM in ([1],[2],[3])) as PVT
), V_TB AS (
    SELECT 
    *
    , CASE WHEN [phub_state] = [PROGEN_STATE] THEN 1 ELSE 0 END AS V_STATE
    , CASE WHEN [phub_city] = [PROGEN_CITY] THEN 1 ELSE 0 END AS V_CITY
    , CASE WHEN [phub_addr] = [PROGEN_STREET] THEN 1 ELSE 0 END AS V_STREET
     FROM 
PROCESSED_TB
    
) SELECT 
    *
FROM 
    V_TB
WHERE
    V_STATE = 0 OR V_CITY = 0 
ORDER BY
    V_STATE

-- ============================================================================================================================================
-- ============================================================================================================================================
-- Property hub Left Join Progen  -> to Select what is In Corrigo but not in Progen (Rows should be removed from Progen)
-- ============================================================================================================================================
SELECT 
    *
FROM 
    dbo.[P_vs_C_5.5.2022]

