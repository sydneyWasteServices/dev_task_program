import os 
import psutil    
# "someProgram" in (p.name() for p in psutil.process_iter())

# process = [p.name() for p in psutil.process_iter()]

# print(process)
# # os.stat(location_of_file)W


# # If you really want to get all the items containing abc, use

# matching = [s for s in some_list if "abc" in s]
process = [p.name() for p in psutil.process_iter()]

with open('helloworld.txt','a') as f:
    f.write(str(process))
    f.close()


    