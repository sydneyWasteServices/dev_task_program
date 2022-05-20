EXECUTE dbo.selectColsName N'progen05-05-2022'

EXECUTE dbo.tablesDataType N'Corrigo'

USE 
JLL
GO

SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES;

-- ==========================================================================================================================
-- Progen 
-- Corrigo_Customer_Number Name
-- Lease  Owner Status  Corrigo_Status OVCP_ID_JLL_Interface

-- Cost centre -> SAP_Company_Code, Cost_Centre
-- Lease area analysis -> start_date stop_date Term Option Component_Area_Leaseable Rent_Annual Outgoings_Month , Site_Type
-- ==========================================================================================================================

SELECT 
    [Status], [Stop_Date], [Vacated_Date],*
FROM
    dbo.[progen02-05-2022]
WHERE   
    [OVCP_ID_JLL_Interface] IN (17649540,65006021,17648672,17649313,17649158,17648592,17648992,17648809,17650530,17649859,17650087,79229972,17650475,17649621,95233310,17649754,17649584,17650149,17649399
,23206538,17649810,25643939,17650289,17650348,20456576,17648786,17650196,17650274,95376823,18306022,17649255,17650116,20456593,17648499,17649489,17650435,17648655
,17650280,17648417,17650081,17650375,18046476,17648632,17648742,17649268,17650125,17649642,25699788,54950288)
    -- = 17649822
    -- [Name] LIKE '%FAIRFIELD%';
    -- [OVCP_ID_JLL_Interface] IN (17648786, 17648707, 17649028, 17650375, 17649268, 17650125, 17649642)

SELECT 
  *
FROM
    dbo.[Corrigo]
WHERE
    [BU_Number] in (4849801141,4849803193,4849800273,4849800914,4849800759,4849800193,4849800593,4849800410,4849802131,4849801460,4849801688,4849803286,4849802076,4849801222,4849803421
,4849801355,4849801185,4849801750,4849801000,4849802749,4849801411,4849802796,4849801890,4849801949,4849802540,4849800387,4849801797,4849801875,4849803429,4849802512,4849800856
,4849801717,4849802524,4849800100,4849801090,4849802036,4849800256,4849801881,4849800018,4849801682,4849801976,4849802432,4849800233,4849800343,4849800869,4849801726,
4849801243,4849802803,4849803141)
-- = 4849801423
-- [Property_Name] LIKE '%FAIRFIELD%'   
-- [BU_Number] IN ('4849800387', '4849800308', '4849800629', '4849801976', '4849800869', '4849801726', '4849801243')

SELECT 
    -- *
 [RecordID],[E1_BU], [Property_Name], [Property_Status]
FROM 
    dbo.[Property_hub]
where 
    [OVCP_ID] IN (17649540,65006021,17648672,17649313,17649158,17648592,17648992,17648809,17650530,17649859,17650087,79229972,17650475,17649621,95233310,17649754,17649584,17650149,17649399
,23206538,17649810,25643939,17650289,17650348,20456576,17648786,17650196,17650274,95376823,18306022,17649255,17650116,20456593,17648499,17649489,17650435,17648655
,17650280,17648417,17650081,17650375,18046476,17648632,17648742,17649268,17650125,17649642,25699788,54950288)
    -- [OVCP_ID] = 17648742
    -- [Property_Name]  LIKE '%FAIRFIELD%'
-- [E1_BU] = '4849800007'





















-- ==========================================================================================================================
-- ==========================================================================================================================
-- Check Corrgio Number
-- ==========================================================================================================================
-- ==========================================================================================================================
SELECT 
    [NAME], [OWNER], [STATUS], [START_DATE], [STOP_DATE], [Corrigo_Customer_Number], [CORRIGO_STATUS], [OVCP_ID_JLL_INTERFACE]
FROM
    dbo.[progen09-05-2022]
WHERE   
    -- [OVCP_ID_JLL_Interface] = 21961539
    [Name] LIKE '%44 Corrina%';

SELECT 
  [Customer_Number], [BU_Number], [Property_Name], [DBA]
FROM
    dbo.[Corrigo]
WHERE
    -- [BU_Number] in ('4849800789', '4849803002')
    [Property_Name] LIKE '%44 Corrina%'

SELECT 
  [RecordID],[E1_BU], [Property_Name], [Property_Status]
FROM 
    dbo.[Property_hub]
where 
    -- [RecordID] in (17649188, 21961539)
    [Property_Name] LIKE '%44 Corrina%'











-- ================================================
SELECT 
    TOP 1 *
FROM 
    dbo.[Corrigo]

-- ==========================================================================================================================
-- ==========================================================================================================================
-- Validate 
-- Check Duplicate Corrigo Number in Progen
-- System Flag Potential Off-site  -> use Progen compare with Corrigo / Property Hub and Terminated status in Progen 
SELECT 
    [Lease],[Corrigo_Customer_Number], [OVCP_ID_JLL_INTERFACE], [STATUS] PROGEN_STATUS, [CORRIGO_STATUS], [NAME], [OWNER],[START_DATE], [STOP_DATE]
FROM
    dbo.[progen05-05-2022]
WHERE 
    [Name] LIKE '%74 McCoy%'
    -- [Lease] = 'LA0069'

SELECT 
  [Customer_Number] Corrigo_Customer_Number, [BU_Number], [Property_Name], [DBA], [Historical_Status], [corrigo_status]
FROM
    dbo.[Corrigo]
WHERE
    -- [Property_Name] LIKE '%40 Rudloc%'
    [Customer_Number] = 659
    -- in (2328, 3701)

AND
    [Historical_Status] <> 1

SELECT 
  [RecordID],[E1_BU], [Property_Name], [Property_Status]
FROM 
    dbo.[Property_hub]
where 
    [Property_Name] LIKE '%122 spencer%'
AND
    [Property_Status] = 'Active'
    -- [RecordID] in (17649188, 21961539)





























-- ==========================================================================================================================
-- ==========================================================================================================================
-- Check incorrect corrigo number
-- ==========================================================================================================================
-- ==========================================================================================================================
-- Code Explaination :


-- 1. Extract Corrigo Number from Corrigo  and match it with Progen Corrigo Number
-- 2. Match State, Suburb and address with both and Give result and V_state V_City V_Street


-- ==========================================================================================================================

WITH JOINTB AS (
    SELECT 
    p.[Lease] PROGEN_LEASE_ID,
    P.[Corrigo_Customer_Number] PROGEN_CORRIGO_NUMBER, 
    C.[Customer_Number] CORRIGO_NUMBER,
    P.[OVCP_ID_JLL_Interface] PROGEN_OVCP_ID,
    P.[Name] PROGEN_PROPERTY_NAME,
    C.[Property_Name] CORRGIO_PROPERTY_NAME,
    P.[STATUS] PROGEN_STATUS,
    P.[Corrigo_Status] PROGEN_CORRIGO_STATUS,
    C.[corrigo_status],
    lower(trim(C.[State_Prov])) CORRIGO_STATE,
    lower(trim(C.[City_Town])) CORRIGO_CITY,
    lower(trim(C.[Address_1])) CORRIGO_ADDR,
    value,
    ROW_NUMBER() OVER(PARTITION by [Lease] order by [Lease]) as ROWNUM
FROM
    dbo.[progen02-05-2022] P
JOIN
    dbo.[Corrigo] C
ON
    P.[Corrigo_Customer_Number] = C.[Customer_Number]
CROSS APPLY string_split([Name], '-')
), PROCESSED_TB AS (
SELECT
    PROGEN_LEASE_ID,
    PROGEN_CORRIGO_NUMBER,
    CORRIGO_NUMBER,
    PROGEN_OVCP_ID,
    PROGEN_PROPERTY_NAME,
    CORRGIO_PROPERTY_NAME,
    PROGEN_STATUS,
    PROGEN_CORRIGO_STATUS,
    corrigo_status,
    CORRIGO_STATE,
    CORRIGO_CITY,
    CORRIGO_ADDR,
    LOWER(TRIM(replace([1],'#',''))) AS [PROGEN_STATE],
    LOWER(TRIM([2])) AS [PROGEN_CITY],
    LOWER(TRIM([3])) AS [PROGEN_STREET]
FROM 
    JOINTB
PIVOT
(
    MAX(VALUE)
    FOR ROWNUM in ([1],[2],[3])) as PVT
), V_TB AS (
    SELECT 
    *
    , CASE WHEN [Corrigo_state] = [progen_state] THEN 1 ELSE 0 END AS V_STATE
    , CASE WHEN [CORRIGO_CITY] = [PROGEN_CITY] THEN 1 ELSE 0 END AS V_CITY
    , CASE WHEN [CORRIGO_ADDR] = [PROGEN_STREET] THEN 1 ELSE 0 END AS V_STREET
     FROM 
PROCESSED_TB
    
) SELECT 
    *
FROM 
    V_TB
WHERE
    V_STATE = 0 OR V_CITY = 0


-- ==========================================================================================================================
-- This query can not Compare Corrigo number which is not exist in corrigo,  e.g. 3596
-- ==========================================================================================================================

SELECT 
    P.[Lease],
    C.[BU_Number] BU_number,
    C.[Customer_Number] CORRIGO_NUMBER,
    P.[Corrigo_Customer_Number] PROGEN_CORRIGO_NUMBER,
    C.[Property_Name] CORRIGO_PROPERTY_NAME,
    P.[Name] PROGEN_PROPERTY_NAME,
    C.[DBA] CORRIGO_BU_UNIT,
    P.[Owner] PROGEN_BU_UNIT,
    C.[corrigo_status] CORRIGO_STATUS,
    P.[Status] PROGEN_STATUS,
    C.[site_comment]
FROM 
    dbo.[Corrigo] C
LEFT JOIN
    dbo.[progen05-05-2022] P
ON
    C.Customer_Number = P.Corrigo_Customer_Number
WHERE
    P.[Corrigo_Customer_Number] IS NULL
AND
    C.[corrigo_status] IS NULL
AND 
    C.[DBA] IN ('ALLIED', 'CORP', 'DEN-COR', 'EYE-CLC', 'GP', 'MC', 'OCC-HEL', 'SKIN', 'SPE-SER','TR')
-- ==========================================================================================================================
-- Corrigo Left Join Progen  -> to Select what is In Corrigo but not in Progen (Rows should be removed from Progen)
-- Property hub Left Join Progen  -> to Select what is In Corrigo but not in Progen (Rows should be removed from Progen)
-- Or use Intercept
-- ==========================================================================================================================



-- ==========================================================================================================================
-- JOIN Corrigo Progen Reconciliation DS to Progen DS
-- ==========================================================================================================================

SELECT 
    P.[Lease],
    P.[Name],
    P.[Owner],
    P.[Owner_Name],
    P.[Owner_Group],
    P.[Owner_Group_Name],
    P.[Land],
    P.[Land_Name],
    P.[Land_Group],
    P.[Land_Group_Name],
    P.[Building],
    P.[Building_Name],
    P.[Building_Group],
    P.[Building_Group_Name],
    P.[Service_Region],
    P.[Section],
    P.[Section_Name],
    P.[Section_Group],
    P.[Section_Group_Name],
    P.[Suite],
    P.[Suite_Name],
    P.[Suite_Group],
    P.[Suite_Group_Name],
    P.[Annexe],
    P.[Annexe_Name],
    P.[Annexe_Group],
    P.[Annexe_Group_Name],
    P.[Type],
    P.[Status],
    P.[Lease_Group],
    P.[Lease_Group_Name],
    P.[Lease_a_c],
    P.[Lease_a_c_Name],
    P.[Start_Date],
    P.[Stop_Date],
    P.[Occupancy],
    P.[Vacated_Date],
    P.[Term],
    P.[Option],
    P.[Option_Name],
    P.[IFRS16_Profile],
    P.[Component_Area_Leaseable],
    P.[Rent_Annual],
    P.[Outgoings_Annual],
    P.[Other_Annual],
    P.[Rent_Month],
    P.[Outgoings_Month],
    P.[Other_Month],
    P.[Bank_Guarantee_Amount],
    P.[Bank_Guarantee_Expiry_Date],
    P.[Bank_Guarantee_Expiry_Date_Event],
    P.[Bank_Guarantee_Received],
    P.[Bank_Guarantee_Registry],
    P.[Bank_Guarantee_Bank],
    P.[Bank_Guarantee_Branch],
    P.[Bank_Guarantee_Returned],
    P.[Bond_a_c],
    P.[Bond_Amount],
    P.[Bond_Received],
    P.[Bond_Registry],
    P.[Bond_Bank],
    P.[Bond_Branch],
    P.[Bond_Refunded],
    P.[Bond_Comments],
    P.[Version],
    P.[SAP_Company_Code],
    P.[Company_Entity],
    P.[Gross_Net],
    P.[Site_Type],
    P.[Region],
    P.[Cost_Centre],
    P.[Termination_Reason],
    P.[Corrigo_Customer_Number],    
    P.[OVCP_ID_JLL_Interface],
    PCrecon.[Correct_Corrigo_For_Progen] CORRECT_Corrigo_Number
FROM 
    dbo.[P_vs_C_5.5.2022] PCrecon
JOIN
    dbo.[progen05-05-2022] P
ON  
    PCrecon.[PROGEN_LEASE_ID] = P.[Lease]
WHERE
    PCrecon.[Correct_Corrigo_For_Progen] <> 0




AND
    PCrecon.[PROGEN_LEASE_ID] NOT IN ('LA0149', 'LA0144', 'LA0002','TE0000', 'LA0147', 'LA0148', 'LA0005')



