#!/bin/bash

echo -n "Print message?"

valid=0

while
[ $valid == 0 ]
do
	read ans
	case $ans in
	yes|YES|y|Y ) echo will print the message
		      echo The message
		      valid=1
		      ;;
	[nN][o0]    ) echo will not print the message
		      valid=1;;
	*	    ) echo Yes or No of some form please;;
	esac
done
