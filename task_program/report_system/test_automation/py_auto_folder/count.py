import time
import ast

f = open("./data.txt", "r")
 
# ======================
usa_stock_list= f.readlines()
usa_stock_list = [stock_code.replace("\n", "")for stock_code in usa_stock_list]
usa_stock_list = set(usa_stock_list)
print(len(usa_stock_list))
print(len(usa_stock_list)/2)

# 1826
# 3651


# usa_stock_list = ast.literal_eval(usa_stock_list)

with open("./stock_code.txt", "w") as file:
    file.write(str(usa_stock_list))
    # print(usa_stock_list)
    f.close()

# ======================

# with open("./stock_code.txt", "r") as file:
#     usa_stock_list = file.readlines()[0]
#     usa_stock_list = ast.literal_eval(usa_stock_list)
#     print(len(usa_stock_list))

#     # f.close()




# import signal 
# NOT to interrupt by SignalINT

# signal.signal(signal.SIGINT, handler)
# type()
# usa_stock_list = list(usa_stock_list)
# sec = 0

# while True:
#     # print("\r{}".format(sec), end="")
#     print(sec)
#     time.sleep(1)
#     sec += 1