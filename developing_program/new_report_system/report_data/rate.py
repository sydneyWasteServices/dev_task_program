class Rate:
    # Cardboard has 2 Rate Grima $150, PolyTrade $120 -> design a data structure that fits Flexible input of different tip site
    def __init__(
            self,
            GENERAL_WASTE : float = 0 ,            
            CARDBOARD : float = 0,
            COMINGLED : float = 0,
            ORGANICS : float = 0
            ):

            self.GENERAL_WASTE = GENERAL_WASTE 
            self.CARDBOARD = CARDBOARD
            self.COMINGLED = COMINGLED
            self.ORGANICS = ORGANICS