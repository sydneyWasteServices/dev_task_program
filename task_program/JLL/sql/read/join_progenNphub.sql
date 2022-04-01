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
    dbo.[progen30.3.2022] progen
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
dbo.[progen30.3.2022]


-- ========================================================================================
-- ========================================================================================
-- [Property_Name], [Property_Status]
SELECT 
    [Property_Name], [Property_Status], [OVCP_ID]
FROM 
    dbo.[Property_hub]
WHERE
    [PROPERTY_NAME] LIKE '%Darlinghurst%'
AND
    [Property_Status] = 'Active'
ORDER BY 
    [PROPERTY_NAME]
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
    dbo.[progen30.3.2022] progen
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
-- ======================================================================
-- ======================================================================


-- , PartTbID AS (    )SELECT
--     PartTbID.*
-- FROM
--     PartTbID




