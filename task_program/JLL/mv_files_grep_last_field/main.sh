# How to test only grep one file 
# Since I am going to rm one file only
ICSV=$(cat '../list.csv' | cut -d, -f1)
for id in $ICSV
do 
    ls ./ | if [ "$(grep -c -w $id)" -gt 1 ]; then 
        # more than one match
        echo $id;
        echo $(ls ./ | grep $id -w); else
        ls ./ | grep -w $id | xargs -d '\n' rm
    fi
done
# let "COUNT+=1"
# echo $COUNT
# COUNT=$[$COUNT +1]
# let COUNT++
# echo $COUNT
# equal to 1 -> rm
# -0 -d "\n" -exec rm
# $(ls ./ | grep $id -w)
# echo $( ls ./ | grep $id -c -w);
# $(ls ./ | grep $id -c)
# issues - the ternary even larger than 1 is True 
# l | grep 1115 -w -c | echo $(( xargs > 1 ))
# /c/Users/Gordon.Tang/Desktop/codes/repo/dev_task_program/task_program/JLL/mv_files_grep_last_field/main.sh
