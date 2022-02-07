# How to test only grep one file 
# Since I am going to rm one file only
ICSV=$(cat '../list.csv' | cut -d, -f1)
for id in $ICSV
do 
    ls ./ | if [ "$(grep -c -w $id)" -gt 1 ]; then 
        # more than one match
        echo $id;
        echo $(ls ./ | grep $id -w); else

        # equal to 1 
        # rm 
        # echo $( ls ./ | grep $id -c -w);
        
        echo $id;
        echo "to remove"
    fi
done

# $(ls ./ | grep $id -w)

# $(ls ./ | grep $id -c)

# issues - the ternary even larger than 1 is True 
# l | grep 1115 -w -c | echo $(( xargs > 1 ))


# 7575




