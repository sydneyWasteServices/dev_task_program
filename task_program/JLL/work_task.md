##### High - Priority
    - Filter condition also add 
- if Corrigo number has Progen Active & Terminate -> filter that out 

                |
- Reconiliation V
    1. Get all OVCP ID and Corrigo 0 n Progen
    2. Prelimit filter 0 and find inactive 

- Develop ML model to compare `Progen Address column` and `Corrigo Address Column`


- Complete a list for Questions -> Progen Corrigo
- Off-Site Record anything has Petra in Off-list
- Turn off Corrigo Site where (PAT-LAV / DI-HIS) is duplicate
- Corrigo Data Rec -->  Corrigo Over Progen
- Property Hub Data Rec ->  Property Hub Over Progen
- Progen terminate over Corrigo & Property Hub
- Site exist in Property Hub & Corrigo, but Not in Progen


##### Mid - Priority
- LightHouse - clean the exception
- Corrigo Work Order Dataset to Local DB
- Off & On site database - What has been on & off -> Comparing with different period of db and Stopped date 
- Data Alert - Cost Centre Different with Corrigo
- Data Alert - Progen SAP Company code with Corrigo


##### Low - Priority & Note
- ForHealth work order - check how many work order has been created ForHealth

- Also fill Alternative Lease
- Asset life cycle chart, usually every 10 years
- lighthouse rule - monitor submit Grosvenor document
- Remove personnels From ASA
- Build Grosvenor Asset Lifecycle
    1. Data Analysis 
        - Stage Grosvenor data to local database
- How to fit Nick's -> EDGE HELP DESK -> 81 Subtype / Subtype standard 

- Automation 
    - Write Program check Data feed -> save attachment to Sharedrive 
        Upload system - automatic upload to sharedrive  - check power Auto / powertask
    - Program loop through Petra and write dataset
        - issue - has python capture all the emails?
        - Check duplicate data between instruction

-- Learning
    - Docker
    - Airflow
    - shell_script
        - if else  dones't work as expected
        - count plus plus
    - React / whatever frontend -> for Clock in / out App
    1. Alytrex  
    2. PowerBI dashboard 
        - On & Off Site analysis, On / Off Ratio, geographic Map for On / Off site
        - 
    3. 

-- Build Chart Tips
    - Look like a Table
    - Has Total amount figure Column
    - Red dot / underlie Red line On Negative figure
    - Chart build for Finance - Just Excel spreadsheet and comparsion -> expand button go -> go gurlarity
    - Capex Items in work order - custom fields  Capex/Opex 
        How to build chart
        ----------------------------------
        1. chart is detail 
        2. individual client gurlarity 
        3. Why are we spending more or less than last year.(is that normal fluctuation)
        ----------------------------------
----------------------------------------------------------------------
-- Note
    - Car Park -> 197-199 Merrylands Rd, we don't need to deal with it
    - SubLease - 9.2 d - walk away from the lease 
    - Carpark - is ownwer responsiblility
    - Exceute AFL, Agree for Lease
    - AFL - In negotiation
    - Pre-lease 
        - could be occupied, no lease yet
        - could be in negotiate stage
        - Have to see the actual lease 
        - Whitsunday Radiology  buyout option
        - Has the business incorporated to Healius
    - Pick all duplicate instructions and save it in 
        https://jll2.sharepoint.com/teams/AU_CS_Accounts/Healius/Forms/AllItems.aspx?e=2%3AvRssvo&at=9&id=%2Fteams%2FAU%5FCS%5FAccounts%2FHealius%2F09%20Information%20and%20Data%2F08%20Progen%2Fduplicate%5Finstructions&viewid=a4d68629%2Dc1e7%2D4f62%2D8552%2D22709f22cdd3
    - Overholding Negotiation Notification
        - Progen -> Status -> Overholding means The lease period has been expired, it is holding it month by month, it should be re-negotiated and extend
    
Critical Site Definition
- imaging centre
- stand-alone pathology
- laboratory site
- any other site where Healius are responsible for the Essential Safety Measures

Money should invest
____________________________
1. Money invest to Build Clock in / out App 
2. Money invest to scrape Data app - Typescript
3. Money invest to invest create Docker Image where I can install latest R verion with Jupter notebook

########################################################################################################


The 1-3 Park st St Port Macquirie was actually 

a duplication of the Medical Centre 

with the address 

Cnr Part St & Hastings St.  

It was deactivated some time ago as part of a process to get rid of duplications.

The customer is inactive in Corrigo but property is still active.  Suggest this site should be deactivated.

