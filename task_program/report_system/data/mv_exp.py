# Motor Vehicle Expense

class Mv_exp:
    def __init__(
            self,
            fuel: float = 0.03,
            rego: float = 0.0046,
            tolls: float = 0.0086,
            insurance: float = 0.0122,
            rm_cc: float = 0.0178,
            rm_cb: float = 0.013,
            rm_m: float = 0.0006,
            rm_ty: float = 0.0039,
            wcl: float = 0.012,
            others: float = 0.0024):

        self.fuel = [["MV - Fuel", fuel], [0, 7]]
        self.rego = [["MV - Rego", rego], [0, 7]]
        self.tolls = [["MV - Tolls", tolls], [0, 7]]
        self.insurance = [["MV - Insurance", insurance], [0, 7]]
        self.rm_cc = [["Repair & Maintenance - Cab & Chassic", rm_cc], [0, 7]]
        self.rm_cb = [["Repair & Maintenance - Compactor / Body", rm_cb], [0, 7]]
        self.rm_m = [["Repair & Maintenance - Misc. Cosumables", rm_m], [0, 7]]
        self.rm_ty = [["Repair & Maintenance - Tyres", rm_ty], [0, 7]]
        self.wcl = [["Workshop Contractor Labour", wcl], [0, 7]]
        self.others = [["MV exp - Others", others], [0, 7]]
