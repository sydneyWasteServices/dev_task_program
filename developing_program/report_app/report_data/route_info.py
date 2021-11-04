class Route_info():
    def __init__(
        self,
        route_name : str,
        address_in_total_sheet : object= {},
        address_in_local_sheet : object = {},
        income : float = 0,
        portion_total_income : float = 0,
        portion_total_uos_income : float = 0,
        fix_reveune : float = 0,

        gw_waste_edge_weight : float = 0,
        gw_suez_weight : float = 0, 
        gw_var_on_waste_edge_to_suez_weight : float = 0, 
        gw_suez_cost : float = 0 ,
        gw_waste_edge_cost : float = 0,

        cm_waste_edge_weight : float = 0 ,
        cm_actual_weight : float = 0 ,
        cm_var_on_waste_edge_to_actual : float = 0 ,
        cm_cost : float = 0 ,

        cb_waste_edge_weight : float = 0 ,
        cb_actual_weight : float = 0 ,
        cb_var_on_waste_edge_to_actual : float = 0 ,
        cb_cost : float = 0 ,


        uos_fix_revenue : float = 0,
        uos_gw_income: float = 0,
        uos_gw_income_portion: float = 0,
        uos_cm_income: float = 0,
        uos_cm_income_portion: float = 0,
        uos_cb_income: float = 0,
        uos_cb_income_portion: float = 0,


        uosgw_waste_edge_weight: float = 0,
        uosgw_suez_weight: float = 0,
        uoscb_waste_edge_weight: float = 0,
        uoscb_actual_weight: float = 0,
        uoscm_waste_edge_weight: float = 0,
        uoscm_actual_weight: float = 0,

        driver_salary : float = 0 ,

        mv_fuel : float = 0 ,
        mv_rego : float = 0 ,
        mv_tolls : float = 0 ,
        mv_insurance : float = 0 ,
        mv_rm_cc : float = 0 ,
        mv_rm_cb : float = 0 ,
        mv_rm_mc : float = 0 ,
        mv_rm_tyre : float = 0 ,
        labour : float = 0 ,
        mv_others : float = 0 ,

        general_admin_ga : float = 0

    ):
        self.route_name = route_name 
        self.address_in_total_sheet = address_in_total_sheet
        self.address_in_local_sheet = address_in_local_sheet
        self.income = income
        self.portion_total_income = portion_total_income
        self.fix_reveune = fix_reveune
        self.gw_waste_edge_weight = gw_waste_edge_weight
        self.gw_suez_weight = gw_suez_weight
        self.gw_var_on_waste_edge_to_suez_weight = gw_var_on_waste_edge_to_suez_weight
        self.gw_suez_cost = gw_suez_cost
        self.gw_waste_edge_cost = gw_waste_edge_cost



        self.cm_waste_edge_weight = cm_waste_edge_weight
        self.cm_actual_weight = cm_actual_weight
        self.cm_var_on_waste_edge_to_actual = cm_var_on_waste_edge_to_actual
        self.cm_cost = cm_cost 

        self.cb_waste_edge_weight = cb_waste_edge_weight
        self.cb_actual_weight = cb_actual_weight
        self.cb_var_on_waste_edge_to_actual = cb_var_on_waste_edge_to_actual
        self.cb_cost = cb_cost

        self.driver_salary = driver_salary

        self.mv_fuel = mv_fuel
        self.mv_rego = mv_rego
        self.mv_tolls = mv_tolls
        self.mv_insurance = mv_insurance
        self.mv_rm_cc = mv_rm_cc
        self.mv_rm_cb = mv_rm_cb
        self.mv_rm_mc = mv_rm_mc
        self.mv_rm_tyre = mv_rm_tyre
        self.labour = labour
        self.mv_others = mv_others

        self.general_admin_ga = general_admin_ga




