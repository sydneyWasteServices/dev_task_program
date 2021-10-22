f = open("usa_stock.txt","r")
list_usa_stock = f.readlines()

list_usa_stock = [stock_code.replace("\n", "") for stock_code in list_usa_stock]
print(len(list_usa_stock)) 


list_usa_stock = list(set(list_usa_stock))
print(len(list_usa_stock))
f.close()

new_file = open("new_usa_stock.txt","w")

new_file.write(str(list_usa_stock))

new_file.close()