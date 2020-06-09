
#!/bin/bash

echo -n "Print message?"

valid=0

while
[ $valid == 0 ]
do
        read ans
        case $ans in
        yes|YES|y|Y ) echo Thank you for teaching us this quarter
                      echo The message
                      valid=1
                      ;;
        [nN][o0]    ) echo Not going to print the Message
                      valid=1;;
        *           ) echo Yes or No of some form please;;
        esac

done
