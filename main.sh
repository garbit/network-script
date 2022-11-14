#!/bin/bash

read -p "enter public IP: " PUBLIC1
echo "... searching for public object"
OBJECTNAME=$(grep -B 1 $PUBLIC1 testfile1 | grep "object network" | cut -d ' ' -f3)
echo "     found $OBJECTNAME"
echo "... converting public object to internal object"
INTERNALOBJECT=$(grep $OBJECTNAME testfile1 | grep nat | cut -d ' ' -f5)
echo "     found $INTERNALOBJECT"
INTERNALHOST=$(grep -A 1 "^object network $INTERNALOBJECT$" testfile1 |  grep host)
echo "... internal object maps to $INTERNALHOST"
