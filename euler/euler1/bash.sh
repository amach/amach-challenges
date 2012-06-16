#!/bin/bash

SUM=0

for (( i=1; i<1000; i++ ))
do
    if ((  ${i} % 3 == 0 || ${i} % 5 == 0  )) ; then
        SUM=$(( ${SUM} + ${i} ))
    fi
done

echo $SUM
