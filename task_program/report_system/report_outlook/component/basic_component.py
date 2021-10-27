import xlwings as xw
from report_outlook.component.style import Style
from datetime import timedelta 

class Basic_component:
    def __init__(self):
        pass

    def open_wb(self):
        return xw.Book()

    def add_sheets(
            self,
            wb: object,
            ws_names: list):

        num_req_ws = len(ws_names)
        num_exist_sheets = len(wb.sheets)

        if num_req_ws > num_exist_sheets:
            add_num_sheets = num_req_ws - num_exist_sheets
            [wb.sheets.add() for n in range(add_num_sheets)]

        for i, wsname in enumerate(ws_names):
            wb.sheets[i].name = wsname

    def fonts_arialify(
            self,
            wb: object,
            ws_name: str):

        ws = wb.sheets[ws_name]
        ws.range("A:DA").api.Font.Name = "Arial"

    def header_title(
            self,
            wb: object,
            ws_name: str,
            report_title: str = "Weekly Financial Report Summary",
            cell_loc: str = "A1"):

        title_cell = wb.sheets[ws_name].range(cell_loc)

        title_cell.value = f"{report_title} - {ws_name}"
        
        title_cell.api.Font.Size = 13
        title_cell.api.Font.Bold = True

    def date_title(
            self,
            wb: object,
            ws_name: str,
            date: str,
            date_descr: str = "Start at",
            cell_loc: str = "A2"):

        date_cell = wb.sheets[ws_name].range(cell_loc)
        date_cell.value = f"{date_descr} : {date}"

        date_cell.api.Font.Size = 13
        date_cell.api.Font.Bold = True


    def beautify_left_columns(self, wb, ws_name: str):
        ws = wb.sheets[ws_name]
        ws.range('A1').column_width = 1.0
        ws.range('B1').column_width = 3.14
        ws.range('C1').column_width = 3.14

    # Anchor cell => The first Bold title (Start Income Session)
    # Anchor cell =>B5

    # session_title_cell => pointing to wb.sheets[ws_name].range(cell_loc)
    # cell_loc should be type string or Object( wb.sheets[ws_name].offset() )
    # cell_loc => string | .offset()
    def session_title(
            self,
            wb: object,
            ws_name: str,
            session_title: str,
            cell_loc: str):

        session_title_cell = wb.sheets[ws_name].range(cell_loc)
        session_title_cell.value = session_title

        session_title_cell.api.Font.Size = 13
        session_title_cell.api.Font.Bold = True

# cell_loc => string | .offset()
    def subtitle(
            self,
            wb: object,
            ws_name: str,
            subtitle: str,
            cell_loc: str):

        subtitle_cell = wb.sheets[ws_name].range(cell_loc)
        subtitle_cell.value = f"{subtitle} :"

        subtitle_cell.api.Font.Size = 11
        subtitle_cell.api.Font.Bold = True

    # table_headers => list of string
    # y , x
    # row, column
    def table_headers(
            self,
            wb: object,
            ws_name: str,
            table_headers: list,
            cell_loc: str):

        start_cell = wb.sheets[ws_name].range(cell_loc)
        start_cell.value = table_headers
        self.table_headers_format(wb, ws_name, cell_loc)

    def table_headers_format(
            self,
            wb: object,
            ws_name: str,
            start_cell_loc: str):

        ws = wb.sheets[ws_name]
        start_cell = ws.range(start_cell_loc)

        start_cell_row = start_cell.row
        start_cell_col = start_cell.column

        end_cell_col = start_cell.end("right").column

        # +1 to print that much times of the column(x)
        for i in range(start_cell_col, end_cell_col+1):
            ws.range((start_cell_row, i)).api.Font.Bold = True

    def fill_items_downward(
            self,
            wb: object,
            ws_name: str,
            items: object = {},
            cell_loc: str = ""):

        if items.__dict__ == {}:
            print(f"{ws_name} items is empty")
            return 0
        else:
            item_dict = items.__dict__

        if cell_loc == "":
            print(f"inc / exp items start cell is {cell_loc}")
            return 0

        cells = []
        item_start_cell = wb.sheets[ws_name].range(cell_loc)

        item_keys = item_dict.keys()

        #           Infor                   Column Offset by
        #            title          Figure  offset by 0 , 6
        # {"gw": [["General Waste", 9999],[0, 6]] }

        for item in item_keys:

            item_info = item_dict[item][0]
            item_col_offset = item_dict[item][1]

            if len(item_info) != len(item_col_offset):
                print("info does not match offset coordinates")
                return 0
            else:

                target_cell = self.check_empty_cell(item_start_cell)

                for i, itemName in enumerate(item_info):

                    cells.append(target_cell)

                    self.fill_item_sideward(
                        wb,
                        ws_name,
                        itemName,
                        item_col_offset[i],
                        target_cell)

        return cells

# {itemName : [[infor1, infor2], [1columns, 3 columns]]}
# e.g Value as Array [infor1, infor2] , leftward of [1columns, 3 columns ]
# Item1          9999
    def fill_item_sideward(
            self,
            wb: object,
            ws_name: str,
            itemName: str,
            offsetBy: int,
            cell_loc: object):

        cell_loc.offset(column_offset=offsetBy).value = itemName

# ==============
    def check_empty_cell(self, target_cell: object):

        if target_cell.value is None:
            return target_cell
        else:
            new_target_cell = target_cell.offset(row_offset=1)
            return self.check_empty_cell(new_target_cell)

        # new_cell_loc = cell_loc.end("down").column + 1
# ==============

    def session_total(
            self,
            itemName: str,
            figure: float = 0,
            cell_loc: object = {}):

        session_total_name = f"Total {itemName}"

        session_total_title = cell_loc.offset(row_offset=2)
        session_total_title.value = session_total_name
        session_total_title.api.Font.Bold = True

        session_total = session_total_title.offset(column_offset=8)
        session_total.value = figure
