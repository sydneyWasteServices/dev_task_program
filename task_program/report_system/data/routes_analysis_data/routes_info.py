class Routes_info:
    def __init__(
            self,
            rev_type : str,
            total_inc: float,
            total_weight: float,
            booking_price_series: object,
            tipping_weight_series: object,
            rate : float = 0):

        self.rev_type = rev_type
        self.total_inc = total_inc
        self.total_weight = total_weight
        self.booking_price_series = booking_price_series
        self.tipping_weight_series = tipping_weight_series
        self.rate = rate
        
# Pick routes weight & rate From series key
    

