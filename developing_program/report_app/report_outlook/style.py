import xlwings as xw


class Style:
    def __init__(self):
        pass

    def color_cell(self):
        pass

    def percentify_cell(self):
        pass

    def accountify_cell(self):
        pass

    def size(self):
        pass

    def boldify(self, wb: object, font_size: int, ws_name: str, cell: str):

        target_cell = wb.sheets[ws_name].range(cell)
        target_cell.api.Font.Size = font_size
        target_cell.api.Font.Bold = True

    def fonts_arialify(
            self,
            wb: object,
            ws_name: str):

        ws = wb.sheets[ws_name]
        ws.range("A:DA").api.Font.Name = "Arial"
