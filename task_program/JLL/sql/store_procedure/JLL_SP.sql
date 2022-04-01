-- SP s
-- tablesDataType
-- listAllTable
-- selectColsName

USE 
JLL
GO
DROP TABLE dbo.[progen8.2.2022]
EXEC tablesDataType 'Property_hub'

-- list SP 
Select [NAME] from sysobjects where type = 'P' and category = 0;

-- List Table
SELECT TABLE_NAME  FROM INFORMATION_SCHEMA.TABLES;

-- List views
Select [NAME] from sysobjects where type = 'V' and category = 0;

-- Query Table Data Columns Type  

IF EXISTS (
        SELECT type_desc, type
        FROM sys.procedures WITH(NOLOCK)
        WHERE NAME = 'tablesDataType'
            AND type = 'P'
      )
     DROP PROCEDURE dbo.tablesDataType
GO

CREATE PROCEDURE dbo.tablesDataType
    @tableName NVARCHAR(500)
AS
    SELECT 
        c.name 'Column Name',
        t.Name 'Data type',
        c.max_length 'Max Length',
        c.precision ,
        c.scale ,
        c.is_nullable,
        ISNULL(i.is_primary_key, 0) 'Primary Key'
    FROM    
        sys.columns c
    INNER JOIN 
        sys.types t ON c.user_type_id = t.user_type_id
    LEFT OUTER JOIN 
        sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id
    LEFT OUTER JOIN 
        sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
    WHERE
        c.object_id = OBJECT_ID(@tableName)
Go

EXECUTE  dbo.tablesDataType N'progen17-03-2022'



-- Select Column name ONLY
IF EXISTS (
        SELECT type_desc, type
        FROM sys.procedures WITH(NOLOCK)
        WHERE NAME = 'selectColsName'
            AND type = 'P'
      )
     DROP PROCEDURE dbo.selectColsName
GO
create PROCEDURE dbo.selectColsName
    @tableName NVARCHAR(500)
AS

SELECT 
        c.name 'Column Name'
    FROM    
        sys.columns c
    WHERE
        c.object_id = OBJECT_ID(@tableName)


-- EXECUTE  dbo.tablesDataType N'progen17-03-2022'


SELECT 
        c.name 'Column Name',
        t.Name 'Data type',
        c.max_length 'Max Length',
        c.precision ,
        c.scale ,
        c.is_nullable,
        ISNULL(i.is_primary_key, 0) 'Primary Key'
    FROM    
        sys.columns c
    INNER JOIN 
        sys.types t ON c.user_type_id = t.user_type_id
    LEFT OUTER JOIN 
        sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id
    LEFT OUTER JOIN 
        sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
    WHERE
        c.object_id = OBJECT_ID('progen17-03-2022')
    ORDER BY
        t.Name
    