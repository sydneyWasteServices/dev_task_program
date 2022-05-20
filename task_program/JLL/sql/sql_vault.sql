-- ==========================================================================================================================
-- ==========================================================================================================================
-- ==========================================================================================================================

WITH JOINTB AS (
    
), DUPID AS (
    SELECT 
        PROGEN_CORRIGO_NUMBER,
        COUNT(PROGEN_CORRIGO_NUMBER) COUNTING
    FROM
        JOINTB
    GROUP BY
        PROGEN_CORRIGO_NUMBER
        HAVING COUNT(PROGEN_CORRIGO_NUMBER) > 1
) SELECT 
    *
FROM
    JOINTB TB 
JOIN 
    DUPID DUP
ON 
    TB.[PROGEN_CORRIGO_NUMBER] = DUP.[PROGEN_CORRIGO_NUMBER]

-- Final check in Property Hub and Corrigo with Progen
-- if state or City not match
-- =============================================================

WITH PROGEN_NAME AS (

SELECT 
    [Lease],
    [Name], 
    value,
    ROW_NUMBER() OVER(PARTITION by [Lease] order by [Lease]) as ROWNUM
FROM
    dbo.[progen27-04-2022]
CROSS APPLY string_split([Name], '-')
)SELECT 
    [Lease],
    [NAME],
    LOWER(TRIM([1])) AS [STATE],
    LOWER(TRIM([2])) AS [CITY],
    LOWER(TRIM([3])) AS [STREET]
FROM 
    PROGEN_NAME
PIVOT
(
    MAX(VALUE)
    FOR ROWNUM in ([1],[2],[3])) as PVT