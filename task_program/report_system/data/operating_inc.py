
# fr => Fixed Revenue
# cb_rr => CardBoard Recycling Rebate

class Operating_inc:
    def __init__(
            self,
            total: float,
            gw: float,
            cb: float,
            cm: float,
            sub: float,
            uos: float,
            fr: float = 0,
            cb_rr: float= 100 ):
            
            self.total = [["Total", total], [0, 8]]
            self.gw = [["General Waste", gw], [0,8]]
            self.cb = [["Carboard", cb], [0,8]]
            self.cm = [["Comingled", cm], [0,8]]
            self.sub = [["Subcontractor", sub], [0,8]]
            self.uos = [["UOS", uos], [0,8]]
            self.fr = [["Fixed Revenue", fr], [0,8]]
            self.cb_rr = [["CardBoard Recycling Rebate", cb_rr], [0,6]]
        
    def get_rate(self, rev_type : str):
        return self.cb
