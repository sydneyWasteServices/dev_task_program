import xlwings as xw

wb = xw.Book()
ws = wb.sheets[0]

ws.range("A1").value = 1

start = ws.range("A1")

ws.range("A2").value = "block"





def recursive_check(cell_check):

    if cell_check.value is None:
        cell_check.value = 2
    else:
        new_cell = cell_check.offset(row_offset=1)
        print("hit")
        return recursive_check(new_cell) 

recursive_check(start)
