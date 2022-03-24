-- Use intersect compare two dataset
-- progen15-02-2022
-- progen09-03-2022

-- progen14-03-2022
-- progen17-03-2022
-- progen22-03-2022

-- List Table
SELECT TABLE_NAME  FROM INFORMATION_SCHEMA.TABLES;

USE JLL 
GO

-- Check Status
SELECT 
*
FROM 
dbo.[progen24-03-2022]
WHERE 
[Name] LIKE '%WA - AUSTRALIND - Shop 24, Australind S/C, Old Coast Rd ACC 2%'


SELECT 
[Component_Area_Leaseable]
FROM 
dbo.[progen23-03-2022]
WHERE 
[Name] LIKE '%Dalgleish St%'

-- Component_Area_Leaseable

-- [OVCP_ID_JLL_Interface] = 0
-- AND 
-- [Lease] IN ('LA0440', 'LA0441')
-- [Corrigo_Customer_Number] = 0 
-- [Lease] = '6008680'
-- ('6008504', '6004821', '6007973')


-- Check 0 in Corrigo Customer Number
SELECT 
*
FROM 
dbo.[progen22-03-2022]
WHERE 
[OVCP_ID_JLL_Interface] = 0


-- ===========================================================================
-- To Find out Terminated Property and Stop Date Prior 22.03.2022
-- ===========================================================================
SELECT 
[Lease] , [Name], [Status], [Start_Date] , [Stop_Date]
FROM 
dbo.[progen09-03-2022]
WHERE 
[Stop_Date] < '20220322'
AND 
[STATUS] LIKE '%Terminated%'
ORDER BY 
[STATUS]
-- ===========================================================================

-- ===========================================================================
-- 2414
SELECT 
COUNT (*) [15-2-2022]
FROM 
dbo.[progen15-02-2022];

-- 2397
SELECT 
COUNT (*) [22-3-2022]
FROM 
dbo.[progen22-03-2022];


--  two tables have in common
-- Common 2346
SELECT 
[Lease]
FROM 
dbo.[progen15-02-2022]
INTERSECT
SELECT 
[Lease]
FROM 
dbo.[progen22-03-2022];

-- Will show us all the rows of the Original  not in the Revised 
-- In progen15-02-2022 Not In progen22-03-2022
-- Supposer to be deleted sites
SELECT 
[Lease]
FROM 
dbo.[progen15-02-2022]
EXCEPT
SELECT 
[Lease]
FROM 
dbo.[progen22-03-2022];

-- In progen22-03-2022 Not In progen15-02-2022
-- Suppose to be new site
SELECT 
[Lease]
FROM 
dbo.[progen22-03-2022]
EXCEPT
SELECT 
[Lease]
FROM 
dbo.[progen15-02-2022]

