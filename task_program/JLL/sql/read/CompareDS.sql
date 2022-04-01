-- Count number of new properties
USE 
JLL
GO


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



-- Lease Number Change

SELECT 
    *
FROM
    dbo.[progen24-03-2022]
WHERE
    [Lease] = 'LA0450'

-- [Name] LIKE '%tyron%'

SELECT 
    *
FROM 
    dbo.[progen21.2.2022]