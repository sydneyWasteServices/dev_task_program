USE 
JLL
GO

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES;

-- =========================================================================================================================================
-- Progen Compare - using Except 
-- Previous vs Current Progen Data
-- Current vs Previous Progen Data
-- =========================================================================================================================================
-- Count Number of Difference Rows
SELECT
    COUNT(*)
FROM
    (SELECT
            [Lease]
        FROM
            dbo.[progen28-03-2022]
        WHERE 
            [Status] NOT LIKE '%Pre-Lease%'
    EXCEPT
        SELECT
            [Lease]
        FROM
            dbo.[progen15-02-2022]
) 
temp;

-- Get new properties
-- =========================================================================================================================================
Select 
    *
FROM
    [progen01-04-2022]
WHERE 
[progen01-04-2022].[Lease] in (             
    SELECT
        [Lease]
    FROM
        dbo.[progen01-04-2022]
    WHERE 
        [Status] NOT LIKE '%Pre-Lease%'
EXCEPT
    SELECT
        [Lease]
    FROM
        dbo.[progen15-02-2022])
ORDER BY 
    [Lease]


Select 
    *
FROM
    [progen28-03-2022]
WHERE 
[progen28-03-2022].[Lease] in (             
    SELECT
        [Lease]
    FROM
        dbo.[progen28-03-2022]
    WHERE 
        [Status] NOT LIKE '%Pre-Lease%'
EXCEPT
    SELECT
        [Lease]
    FROM
        dbo.[progen24-03-2022])
ORDER BY 
    [Lease]


-- =========================================================================================================================================
-- Check Duplicate Lease ID
-- =========================================================================================================================================
WITH CHECK_TB AS (
    SELECT 
        [Lease]
    FROM 
        dbo.[progen05-05-2022]
    GROUP BY
        [Lease]
    HAVING
        COUNT(*) > 1 
)
SELECT 
    *
FROM 
    dbo.[progen05-05-2022] OG_TB
JOIN 
    CHECK_TB
ON
    OG_TB.[Lease] = CHECK_TB.[Lease]
