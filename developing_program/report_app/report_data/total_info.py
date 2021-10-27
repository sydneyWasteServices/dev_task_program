class Total_info:
    def __init__(
        self,
        income : float = 0,
        fixed_revenue : float = 0,
        
        gw_waste_edge_weight : float = 0,
        gw_suez_weight : float = 0,
        gw_suez_bring_forward_weight : float = 0,
        gw_var_we_suez : float = 0,
        gw_suez_cost : float = 0, 
        gw_suez_bring_forward_cost : float = 0,
        gw_total_suez_cost : float = 0,
        
        co_waste_edge_weight : float = 0,
        co_actual_weight : float = 0,
        co_var_we_actual_weight : float = 0,
        co_cost: float = 0,

        cb_waste_edge_weight : float = 0,
        cb_actual_weight : float = 0,
        cb_var_we_actual_weight : float = 0,
        cb_cost: float = 0,

        driver_salary : float = 0,

        mv_fuel : float = 0,
        mv_rego : float = 0,
        mv_tolls : float = 0,
        mv_insurance : float = 0,
        mv_rm_cc : float = 0, 
        mv_rm_cb : float = 0, 
        mv_rm_mc : float = 0, 
        mv_rm_tyres : float = 0, 
        mv_labour : float = 0, 
        mv_others : float = 0, 
        general_admin_ga : float = 21463
    ):
        self.income = income
        self.fixed_revenue = fixed_revenue

        self.gw_waste_edge_weight = gw_waste_edge_weight
        self.gw_suez_weight = gw_suez_weight
        self.gw_suez_bring_forward_weight = gw_suez_bring_forward_weight
        self.gw_var_we_suez = gw_var_we_suez
        self.gw_suez_cost = gw_suez_cost
        self.gw_suez_bring_forward_cost = gw_suez_bring_forward_cost
        self.gw_total_suez_cost = gw_total_suez_cost

        self.co_waste_edge_weight = co_waste_edge_weight
        self.co_actual_weight = co_actual_weight
        self.co_var_we_actual_weight = co_var_we_actual_weight
        self.co_cost = co_cost

        self.cb_waste_edge_weight = cb_waste_edge_weight
        self.cb_actual_weight = cb_actual_weight
        self.cb_var_we_actual_weight = cb_var_we_actual_weight
        self.cb_cost = cb_cost

        self.driver_salary = driver_salary

        self.mv_fuel = mv_fuel
        self.mv_rego = mv_rego
        self.mv_tolls = mv_tolls
        self.mv_insurance = mv_insurance
        self.mv_rm_cc = mv_rm_cc
        self.mv_rm_cb
        self.mv_rm_mc
        self.mv_rm_tyres
        self.mv_labour
        self.mv_others
        self.general_admin_ga
       