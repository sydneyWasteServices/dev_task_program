from report_outlook.component.basic_component import Basic_component


class Complex_component(Basic_component):
    def __init__(self):
        super().__init__()
        return

    def report_formating(
            self,
            wb: object,
            ws_name: str):

        super().fonts_arialify(wb, ws_name)
        super().beautify_left_columns(wb, ws_name)
            

    def report_headers(
            self,
            wb: object,
            ws_name: str,
            date: str = "dd/mm/yyyy",
            endDate: str = "dd/mm/yyyy",
            header: str = ""):

       
        super().header_title(wb, ws_name, header)
        super().date_title(wb, ws_name, date)
        super().date_title(wb, ws_name, endDate, "End at", "A3")



    # items {gw: [["General Waste", "9000"], [0, 1]], cm }
    def session(self,
                wb: object,
                ws_name: str,
                session_header: str = "",
                is_inc: bool = True,
                table_headers: list = [],
                items: object = {},
                anchor_row: int = 6):

        if anchor_row == 6 :
            print(f"Please Aware Session {session_header} Cell in B6 ")
        # Anchor cell in B6
        session_title_cell = wb.sheets[ws_name].range((anchor_row, 2))
        session_title_cell.value = session_header
        session_title_cell.api.Font.Bold = True
        session_title_cell.api.Font.Size = 13

        subtitle_cell = session_title_cell.offset(row_offset=1)

        if is_inc is True:
            super().subtitle(wb,ws_name,"Add",subtitle_cell)
        else:
            super().subtitle(wb,ws_name,"Less",subtitle_cell)

        if table_headers != []:
            # Offset column 6
            header_table_start_cell = subtitle_cell.offset(column_offset=6)

            super().table_headers(
                wb,
                ws_name,
                table_headers,
                header_table_start_cell)

        session_item_start_cell = subtitle_cell.offset(row_offset=1, column_offset=1)

        item_cells = super().fill_items_downward(
            wb,
            ws_name,
            items,
            session_item_start_cell)

        end_cell = item_cells[-1]

        super().session_total(session_header, 0, end_cell)

    
        