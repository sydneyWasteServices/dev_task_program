USE JLL 
GO

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES;

-- DROP TABLE [JLL].dbo.[progen18-05-2022]

-- [Corrigo_Customer_Number],[OVCP_ID_JLL_Interface] ,[Lease], [Name], [Owner], [Status], [Start_Date], [Stop_Date], [Occupancy], [Vacated_Date], [Term], [Option], [Option_Name]
SELECT
    *
FROM
    dbo.[progen12-05-2022]
WHERE
    ([Corrigo_Customer_Number] = 0 OR [OVCP_ID_JLL_Interface] = 0)
AND
    ([Status] LIKE '%Active%' OR [Status] LIKE '%Overholding%')
AND
    [Status] NOT LIKE '%Terminated%'
AND
    [Status] NOT LIKE '%Pre-Lease%'


-- ====================================================================================================================
-- ====================================================================================================================
-- Check Progen addr
SELECT 
    [Corrigo_Customer_Number], [Status],*
FROM
    dbo.[progen18-05-2022]
WHERE
    [Name] LIKE '%Lyrebird%'


    -- [Corrigo_Customer_Number] = 1293
    -- [Cost_Centre] = 535888


SELECT *
FROM dbo.[Corrigo] 
WHERE [Customer_Number] = 16


























-- ====================================================================================================================
-- Check addr
-- Row 216

SELECT 
    [Corrigo_Customer_Number], [Status],*
FROM
    dbo.[progen18-05-2022]
WHERE
    [Name] LIKE '%20 Henning%'


    -- [Corrigo_Customer_Number] = 1084
    -- [Cost_Centre] = 535888
    -- [Customer_Number],[Property_Name],[Historical_Status], [DBA]
SELECT
    [Customer_Number],
    *
FROM
    dbo.[Corrigo]
WHERE
    [Property_Name] LIKE '%20 Henning%'
AND 
    [Historical_Status] <> 1

    -- [Customer_Number] = 4288

SELECT
    [Property_Name], [OVCP_ID], [Property_Status]
FROM
    dbo.[Property_hub]
WHERE 
    [Property_Name] LIKE '%20 Henning%'



-- Why 
SELECT
            C.[Customer_Number] Corrigo_Customer_Number_IN_CORRIGO_SYS
        FROM
            dbo.[Corrigo] C
        LEFT JOIN
            dbo.[progen17-05-2022] P
        ON
            C.[Customer_Number] = P.[Corrigo_Customer_Number]
        WHERE 
            (lower(P.[Status]) LIKE '%pre%' OR lower(P.[Status]) LIKE '%active%') 
        AND 
            P.[Corrigo_Customer_Number] <> 0






























-- ====================================================================================================================
-- ====================================================================================================================
-- Still active in Corrigo,  but Not in Progen, terminated and inactive
-- ====================================================================================================================

WITH JOIN_TB_C_ACTIVE AS (
    SELECT
    C.[Customer_Number] Corrigo_Customer_Number_IN_CORRIGO_SYS, 
    P.[Corrigo_Customer_Number] Corrigo_Customer_Number_IN_PROGEN,
    C.[Property_Name] Property_Name_IN_CORRIGO_SYS,
    P.[Name] Property_Name_IN_PROGEN,
    C.[DBA] DBA_IN_CORRIGO_SYS,
    P.[Owner] DBA_IN_PROGEN,
    C.[Historical_Status] AS [Historical_Status_IN_CORRIGO_SYS(0 is active, 1 is inactive)],
    lower(P.[Status]) Status_IN_PROGEN,
    P.[Start_Date] Lease_start_date_IN_PROGEN,
    P.[Stop_Date] Lease_stop_date_IN_PROGEN,
    P.[Occupancy] Lease_Occupancy_date_IN_PROGEN,
    P.[Vacated_Date] Lease_Vacated_date_IN_PROGEN,
    P.[Lease] LeaseID_IN_PROGEN,
    C.[BU_Number] Bu_number_IN_CORRIGO_SYS,
    C.[Property_Number] PRY_IN_CORRIGO_SYS,
    C.[cost_centre] cost_centre_IN_CORRIGO_SYS,
    P.[cost_centre] cost_centre_IN_PROGEN
FROM
    dbo.[Corrigo] C
LEFT JOIN
    dbo.[progen18-05-2022] P
ON
    C.[Customer_Number] = P.[Corrigo_Customer_Number]
WHERE
-- Filter out where Customer number has active and Terminated status in Progen
C.[Customer_Number] NOT IN 
    (
        SELECT
            C.[Customer_Number] Corrigo_Customer_Number_IN_CORRIGO_SYS
        FROM
            dbo.[Corrigo] C
        LEFT JOIN
            dbo.[progen17-05-2022] P
        ON
            C.[Customer_Number] = P.[Corrigo_Customer_Number]
        WHERE 
            (lower(P.[Status]) LIKE '%pre%' OR lower(P.[Status]) LIKE '%active%') 
        AND 
            P.[Corrigo_Customer_Number] <> 0
    )
AND 
    C.[Historical_Status] = 0
), NOT_IN_PROGEN AS (   
    Select 
        *, 
        ROW_NUMBER() OVER(PARTITION by [Corrigo_Customer_Number_IN_CORRIGO_SYS] order by [Corrigo_Customer_Number_IN_CORRIGO_SYS]) as ROWNUM
    FROM
        JOIN_TB_C_ACTIVE
    CROSS APPLY 
        string_split(Property_Name_IN_CORRIGO_SYS, '-')
    WHERE
        (Status_IN_PROGEN LIKE '%terminated%' OR Status_IN_PROGEN LIKE '%inactive%' OR Status_IN_PROGEN IS NULL)
) SELECT 
    *,
    TRIM([1]) AS [STATE]
    -- TRIM([2]) AS [CITY],
    -- TRIM([3]) AS [STREET]
FROM 
    NOT_IN_PROGEN
PIVOT
    (MAX(VALUE)
    FOR ROWNUM in ([1],[2],[3])) as PVT


--     Status_IN_PROGEN NOT LIKE 'pre-lease'
-- AND
-- -- pre-lease / inactive
-- addr -> Lake Rd The Grange Medical Centre, Space Name -> Ground Floor 


-- ====================================================================================================================
-- Look for zero OVCP & Corrigo
-- ====================================================================================================================
-- -> With # Phrase 3 cease trading, ready to terminate(phrase 3 or 4)

-- Phrase 1 - ready to operate with prior renovation, fitting

-- Active / Inactive -> May not pay rent, still active
-- Vacated / Inactive -> phrase 3 - no waste collection service 
-- Overholding / Inactive - phrase 2, still operate, stop service on particalar date
-- Overholding / Active -> phrase 2 -Trading
-- Pre-Lease / Inactive - phrase 1 - set up - no work order
-- Active / Active -> phrase 2 Trading
-- terminated / inactive - phrase 4 - wind down the site - deactivate

-- ====================================================================================================================
-- Find 0 OVCP ID & Corrigo number
-- ====================================================================================================================
-- Issues Active is being filter out


SELECT 
    [ID],
    [Lease],
    [Corrigo_Customer_Number], 
    [OVCP_ID_JLL_INTERFACE], 
    lower([STATUS]),
    [NAME], 
    [OWNER],
    [START_DATE], 
    [STOP_DATE]
FROM
    dbo.[progen18-05-2022]
WHERE
    [Corrigo_Customer_Number] = 2413


--     [NAME] LIKE '%%'
--     lower(trim([STATUS])) = 'active / active'
-- AND [Corrigo_Customer_Number] = 0
    -- LIKE '%active%'
    --  )
 
    
    
    
--     [STATUS] LIKE '%Active%'
-- AND
--     [STATUS] NOT LIKE '%Terminated%'
-- AND

-- OR 
--     [OVCP_ID_JLL_INTERFACE] = 0 



SELECT
    top 1 *
FROM
    dbo.[Corrigo]

SELECT
    [status], *
FROM
    dbo.[progen11-05-2022]
WHERE
    [NAME] LIKE '%58 Campbell%'

-- VIC - WEST BRUNSWICK - 58-58A Melville Road
-- NSW - BALLINA - 85 Tamar Street

-- ====================================================================================================================
-- ====================================================================================================================

-- ,
-- [Corrigo_Customer_Number_IN_CORRIGO_SYS],
-- [DBA_IN_CORRIGO_SYS]
-- AND
--     [DBA_IN_CORRIGO_SYS] NOT IN (
--                                 'DEN-COR'
--                                 ,'MC'
--                                 ,'ALLIED'
--                                 ,'GP'
--                                 ,'OCC-HEL'
--                                 ,'TR'
--                                 ,'SPE-SER'
--                                 ,'SKIN',
--                                 'DSU-COR',
--                                 'EYE-CLC')
-- AND
--     [Corrigo_Customer_Number_IN_CORRIGO_SYS] NOT IN ()



-- 72-80 Lake Rd 
-- AND 
--     [Property_Name_IN_CORRIGO_SYS] LIKE '%Lake%'




-- ====================================================================================================================
-- Corrigo Number over Progen Corrigo Number
-- ====================================================================================================================

WITH JOIN_TB AS (
    SELECT
    C.[Customer_Number] Corrigo_Customer_Number_IN_CORRIGO_SYS, 
    P.[Corrigo_Customer_Number] Corrigo_Customer_Number_IN_PROGEN,
    C.[Property_Name] Property_Name_IN_CORRIGO_SYS,
    P.[Name] Property_Name_IN_PROGEN,
    C.[DBA] DBA_IN_CORRIGO_SYS,
    P.[Owner] DBA_IN_PROGEN,
    C.[Historical_Status] AS [Historical_Status_IN_CORRIGO_SYS(0 is active, 1 is inactive)],
    P.[Status] Status_IN_PROGEN,
    P.[Start_Date] Lease_start_date_IN_PROGEN,
    P.[Stop_Date] Lease_stop_date_IN_PROGEN,
    P.[Occupancy] Lease_Occupancy_date_IN_PROGEN,
    P.[Vacated_Date] Lease_Vacated_date_IN_PROGEN,
    P.[Lease] LeaseID_IN_PROGEN,
    C.[BU_Number] Bu_number_IN_CORRIGO_SYS,
    C.[Property_Number] PRY_IN_CORRIGO_SYS,
    C.[cost_centre] cost_centre_IN_CORRIGO_SYS,
    P.[cost_centre] cost_centre_IN_PROGEN
FROM
    dbo.[Corrigo] C
LEFT JOIN
    dbo.[progen17-05-2022] P
ON
    C.[Customer_Number] = P.[Corrigo_Customer_Number]
WHERE
    P.[Corrigo_Customer_Number] IS NULL
AND
    C.[Historical_Status] = 0
OR
    P.[Status] LIKE '%Terminated%'
), 
    STILL_ACTIVE_TABLE AS (
SELECT
    P.[Corrigo_Customer_Number] STILLACTIVE
FROM
    dbo.[Corrigo] C
LEFT JOIN
    dbo.[progen10-05-2022] P
ON
    C.[Customer_Number] = P.[Corrigo_Customer_Number]
WHERE
    P.[Status] LIKE '%active%'
)SELECT 
    *
FROM
    JOIN_TB
LEFT JOIN 
    STILL_ACTIVE_TABLE
ON 
    JOIN_TB.[Corrigo_Customer_Number_IN_PROGEN] =  STILL_ACTIVE_TABLE.[STILLACTIVE]
WHERE
    STILL_ACTIVE_TABLE.[STILLACTIVE] IS NULL
ORDER BY 
    [Property_Name_IN_CORRIGO_SYS]




