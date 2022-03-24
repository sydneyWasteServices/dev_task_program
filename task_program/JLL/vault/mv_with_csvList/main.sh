#=========================================================================== 
ICSV=$(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1)
for id in $ICSV
do
# if statement if [ condition ]
# one space with condition
    if[ ls "/c/Users/Gordon.Tang/OneDrive - JLL/My files/MC_doc/4018" | grep ${id} ]
then
# cp if has "-t" the become target path , if no -t the grep become target path 
    ls "/c/Users/Gordon.Tang/OneDrive - JLL/My files/MC_doc/4018" | grep ${id} | xargs cp -r -t ~/Desktop/MC_docu/4018
fi
done
#=================================================================== 


# Cut / split  the  ls files name  
#=================================================================== 
# To iterate file in the folder 
for f in *
do
    echo $f | cut -d- -f2
done
#=================================================================== 

# if else statement - example , greater than 
#=================================================================== 
l | grep 1115 -w -c | if [[ xargs -gt 1 ]]
then 
echo $(xargs)
else
echo  "no"
fi
#=================================================================== 

# bash ternary return 
$(( a < b ? a : b )).

#=================================================================== 
# xargs
# cut

# if statement if [ condition ]
# one space with condition

# for id in $(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1)
# do
# # cp if has "-t" the become target path , if no -t the grep become target path 
#     ls | grep ${id} | xargs cp -r -t ~/Desktop/MC_docu/4018
# done


# for filename  in $(ls "/c/Users/Gordon.Tang/OneDrive - JLL/My files/Healius LA Transition Out/4011"); do 
#     for id in $(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1); do
#          if [[ ${id} ]]; then
#             echo 
#          fi 
#     done  
# done


# # C:\Users\Gordon.Tang\Desktop\MC_docu

# # print foldername
# # ============================
# # step 1 
# # present dircetory    cur_dir=$(pwd)
# # for filename in $(ls "$cur_dir"); do echo ${filename}; done
# # ============================


# # To split Folder / file name in a slow way
# #  declare present_dir in var   cur_dir=$(pwd)
# # for filename in $(ls "$cur_dir"); do
# #   echo ${filename} | cut -d_ -f1
# # done


# # for id in $(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1); do
# #     if[[${id} == **]]
# #     echo  
# # done

# for filename in $(ls "$cur_dir"); do 
#     for id in $(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1); do
#         if[[ $(echo ${filename} | cut -d_ -f1) -eq ${id} ]]; then
#             echo ${filename}
#         fi
#     done
# done 


# for id in $(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1); do 
     
#  done



