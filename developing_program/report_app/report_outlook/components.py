import xlwings as xw
from report_outlook.style import Style


class Components:
    def __init__(self):
        return

    def report_header_title(self,
                            wb: object,
                            ws_name: str,
                            report_title: str = "Weekly Financial Report Summary",
                            cell: str = "A1"):
        style = Style()

        style.boldify(wb, 13, ws_name, cell)

        target_cell = wb.sheets[ws_name].range(cell)

        target_cell.value = report_title

    def period_header_title(self,
                            wb: object,
                            ws_name: str,
                            start_date: str,
                            end_date: str,
                            period_title: str = "For the period of ",
                            cell: str = "A2"):

        style = Style()

        style.boldify(wb, 13, ws_name, cell)

        target_cell = wb.sheets[ws_name].range(cell)

        target_cell.value = f"{period_title} {start_date} to {end_date}"

    def session_title(self, 
                      wb: object,
                      ws_name: str,
                      cell: str,
                      size : int,
                      session_title: str = "",
                      isBold : bool = True):
        
        style = Style()

        if isBold:
            style.boldify(wb, size, ws_name, cell)

            target_cell = wb.sheets[ws_name].range(cell)

            target_cell.value = session_title

        else:

            target_cell = wb.sheets[ws_name].range(cell)

            target_cell.api.Font.Size = size

            target_cell.value = session_title
