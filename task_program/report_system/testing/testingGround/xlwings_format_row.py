import xlwings as xw 


wb = xw.Book()

ws = wb.sheets[0]

print(ws[])
# list_val = [1,2,3,4]


# # row, col
# r = 2

# c = 1


# ws.range((r,c)).value = list_val

# print(ws.range((r,c)))


# range('A3:A26').api.Font.Size = 15

# xlwings.load(index=1, header=1)


ws.range("A1").end('right').column