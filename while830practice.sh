
#!/bin/bash

x=3

while
        ((x<12))
do

        echo loop $x
        date >date.$x
        ((x=x+1))
done

