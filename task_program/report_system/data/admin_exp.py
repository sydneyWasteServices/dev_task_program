# General 

class Admin_exp:
    def __init__(
            self,
            ga: float = 0.0218,
            bp: float = 0.011,
            oc: float = 0.0243):

        self.ga = [["General & Administration", ga], [0, 7]]
        self.bp = [["Business Promotion", bp], [0, 7]]
        self.oc = [["Occupancy Cost", oc], [0, 7]]


