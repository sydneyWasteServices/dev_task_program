
LIST_CSV=$1
MEDI_DOCU_IDs=$(cat "$LIST_CSV" | cut -d, -f1)

for id in $MEDI_DOCU_IDs
do  
    # if [ ls "$(pwd)" | grep ${id} ]
    # then    
            # echo ${id}
    ls | grep ${id} | xargs -0 -d"\n" cp -r -t ../medi_documents    
    # fi
done


# main

# ICSV=$(cat /c/Users/Gordon.Tang/Desktop/MC_docu/mc_list.csv | cut -d, -f1)
# for id in $ICSV
# do
# # if statement if [ condition ]
# # one space with condition
#     if[ ls "/c/Users/Gordon.Tang/OneDrive - JLL/My files/MC_doc/4018" | grep ${id} ]
# then
# # cp if has "-t" the become target path , if no -t the grep become target path 
#     ls "/c/Users/Gordon.Tang/OneDrive - JLL/My files/MC_doc/4018" | grep ${id} | xargs cp -r -t ~/Desktop/MC_docu/4018
# fi
# done


# medi_list.csv