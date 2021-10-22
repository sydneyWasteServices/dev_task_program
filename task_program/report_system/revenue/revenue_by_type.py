from revenue.revenue import Revenue
from revenue.rev_types import Rev_types


# pass current resampled df  resampled_df[date_key]
class Revenue_by_type(Revenue):
    def __init__(self,
                 select_date_df: object):
        super().__init__()
        self.select_date_df = select_date_df

    def df(
            self,
            rev_type: str):

      # routes => return list of routes
        routes = Rev_types[rev_type].value
      #   isin list of routes
        routes_row = self.select_date_df['Route number'].isin(routes)
        return self.select_date_df[routes_row]


    def routes_name(
            self,
            rev_type: str):

        # Catch Total
        # if Total
        routes = Rev_types[rev_type].value

        result = (self.select_date_df
                  .pipe(lambda data: data.groupby('Route number').Price.sum())
                  .pipe(lambda data: data.filter(routes))
                  .pipe(lambda data: data.index)
                  )
        return list(result)

    def routes_inc(
        self,
        rev_type: str):

        # Catch Total
        # if Total

        routes = Rev_types[rev_type].value
        result = (self.select_date_df
                  .pipe(lambda data: data.groupby('Route number').Price.sum())
                  .pipe(lambda data: data.filter(routes))
        )
        return list(result)

    def total_inc(
            self,
            rev_type: str):

        if Rev_types[rev_type].value == "total":
            result = self.select_date_df.Price.sum()
            return result
        else:
            routes = Rev_types[rev_type].value
            result = (self.select_date_df
                      .pipe(lambda data: data.groupby('Route number').Price.sum())
                      .pipe(lambda data: data.filter(routes))
                      .pipe(lambda data: data.sum())
                      )
            return result
    # routes_inc_series =>  returns numpy object
    def routes_inc_series(
            self,
            rev_type: str):
        
        routes = Rev_types[rev_type].value

        if routes == "total":
            result = self.select_date_df.groupby('Route number').Price.sum()
            return result
        else:
            
            result = (self.select_date_df
                    .pipe(lambda data: data.groupby('Route number').Price.sum())
                    .pipe(lambda data: data.filter(routes))
                    )
            return result

    