#!/bin/sh

ROOT=$PWD/../media/js

DEBUG=$ROOT/androrm_debug.js
CONCAT=$ROOT/androrm_concat.js
TARGET=$ROOT/androrm.js

if [ $1 ]
then

    if [ $1 = "debug" ]
    then
    
        concat.sh $DEBUG
        
    fi

else
    
    concat.sh $CONCAT
    
    java -jar $ROOT/lib/yuicompressor.jar $CONCAT -o $TARGET
    
    rm $CONCAT
    
fi