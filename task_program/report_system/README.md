# Report system

#### important 
            => Weekly reporting period from Wednesday to Tuesday
        
    ##### Data Frame notes
            => Waste Edge Booking table's Price was not correct prior to 01 Jan 2020, 
                since we were not using it to invoice our client.
            => Some rows does not have Lat and Lng, will need to update its lat lng


    ### Date : 12.4.2021 Visy - Include Visy in Weekly summary

        We subcontracted from Visy by 2 runs

            1. No Fees on 0 Act Amt
            2. Every bins is fixed price of 
                10.77 + GST
            3. No Tipping fee is being charged


    ### 19.3.2021
        
        ####Tipping Tonnage discrepancy 

            There are discrepency between the actual tipping Ton(From Szue & ) and Waste Edge App tipping ton.

            Roughly, General Waste has 13 to 20 tons less against the actual, and cardboard has around 10 tons.


            

    ### Date : 28.1.2021

    Need to rearrange the app. 

    ### Date : 19.01.2021 

    Description :
        This app is to generate weekly financial management report automatcatly, 
        the app design pricinipal is based on features, 
        Revenue class is to manage query and filtering Dataframe by requirements,
        WE_transform is to transform data from WasteEdge's dataframes, 
        testing doesn't relate to the app, it is experiment ground.



    Few question / issues :
        1. Since the Fix income are shown on $0, 
        we are going to figure out how to allocate the fix income back to trucks or routes


    Planning to build :
        Automation class => for auto generting reports
        log class => to generate log reports relate to automation errors / resources usage / how much query has been done, etc.  
        odbc connection class => connecting our own SQL db 
        External API connection class => Connecting to WasteEdge or other external services


    ## Build try catch :
        After I have Log report class / feature,
        I shall have try catch for 
            1. Excel build failure
            2. Connection failure
        
        and then print ***log reports*** 


    ## Build test case
        1. Try Catch Log report printing
        2. expected title and number in correct position
            in few different situation
        3. Give some extreme data to run it, and see what happen

        ****Unit test of DF Smaller then one week and 13days(not enough 2 weeks)****
        
        


    Date : 20/01/2021

        *****Minor Adjustment*****

    Report outlook positioning class => By Route Number figure 
            => format_report_content_rev_by_route_num()

    ***Print money figure per selected key, rather than the entire figure val array***

         Money figures Offset Left 4 by the starting of 
         To make 100% sure the figure is matching the route 
         use for loop or list comp to each out the money figure
         correspond it to the route number
         but I will just list it out, as time constriant

    **Make sure I am generating 7 days of data ** 
        1. How to make sure the dataframe is in 7 days? 
        2. Any warning on the spreadsheet if it's not enough for 7 days?
        
        ```
        3. How to check First row and the row of the frame
        ```


    ### Set up Database, End point for Revenue type and information,and Database arhictect
        
        For now, ***Just an excel endpoint for them to enter and rev_information the data ***
            Excel endpoint to Local DB     

        Set up local database 

        Web app for Meta Data : 
            Endpoint for Metadata infor => rev type information => 
                End of the day build web app to manage internal data information

            

            


    
