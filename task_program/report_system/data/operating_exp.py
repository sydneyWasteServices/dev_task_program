
class Operating_exp:
    def __init__(
            self,
            gw: float = 275,
            cm: float = 190,
            org: float = 240,
            cws: float = 0.03,
            cgt: float = 0.0132,
            others: float = 0.003):

        self.gw = [["General Waste Tipping", gw], [0, 6]]
        self.cm = [["Comingled", cm], [0, 6]]
        self.org = [["Organics", org], [0, 6]]
        self.cws = [["Contracting Waste Service", cws], [0, 7]]
        self.cgt = [["Contracting Grease Trap", cgt], [0, 7]]
        self.others = [["Others", others], [0, 7]]
    
    def get_rate(self, rev_type : str):
        switcher = {
            'GENERAL_WASTE' : self.gw[0][1],
            'COMINGLED' : self.cm[0][1]
        }
        return switcher.get(rev_type, "Invalid match")


