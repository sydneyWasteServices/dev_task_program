# Route name 
# Route Position 

# Route : [income,
#  fix Revenue,
#  WasteEdge_Weight,
#  Suez_Weight, 
# LastWeek_bring forward,
# ]


class General_waste_info():
    def __init__(
        self,
        total_income : float,
        route_info : list = [],
        address_in_total_sheet : object = {},
        address_in_local_sheet : object = {}
        
    ):
        self.total_income = total_income
        # self.routes_income = routes_income
        self.address_in_total_sheet = address_in_total_sheet
        self.address_in_local_sheet = address_in_local_sheet
    
