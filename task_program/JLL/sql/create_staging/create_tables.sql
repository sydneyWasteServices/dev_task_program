-- JLL
-- Insert new table 
USE 
JLL
GO

-- TRUNCATE TABLE [JLL_Healius_Data_Management].[TEST].[JDE] 
CREATE DATABASE JLL

USE JLL
GO

CREATE SCHEMA STAGE;

CREATE SCHEMA CORRIGO;

CREATE SCHEMA HEALIUS;


-- Create Database / Schema / Testing import CSV 
-- =====================================================================
CREATE DATABASE JLL_Healius_Data_Management

CREATE SCHEMA TEST;

select * from TEST.[import_JLLFEED_02-Feb-2022]

-- =====================================================================
-- Display table TEST JDE
SELECT * FROM 
    [JLL_Healius_Data_Management].[TEST].[JDE] 
where Business_Unit = 4849801436

SELECT * FROM 
    [JLL_Healius_Data_Management].[TEST].[PROGEN]

-- =====================================================================
-- Insert into new table 
SELECT * INTO 
    [JLL_Healius_Data_Management].[HEALIUS].[PROGEN]
FROM
    [JLL_Healius_Data_Management].[TEST].[PROGEN] 


SELECT 
    *
FROM 
    [JLL_Healius_Data_Management].[HEALIUS].[PROGEN]

SELECT *
FROM 
    [JLL_Healius_Data_Management].[CORRIGO].[WORK_ORDER]

-- ========================================================
-- Export Table information
USE 
JLL_Healius_Data_Management
GO

Select [Comp]
FROM 
INFORMATION_SCHEMA.Columns
WHERE 
TABLE_SCHEMA = 'TEST'
AND
TABLE_NAME = 'PROGEN'
ORDER BY ORDINAL_POSITION

SELECT 
*
FROM 
dbo.[progen17-03-2022]
