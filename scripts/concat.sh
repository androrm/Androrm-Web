ROOT=$PWD/../media/js
TARGET=$ROOT/androrm_concat.js

if [ $1 ] 
then
    TARGET=$1
fi

cat $ROOT/utils.js\
    $ROOT/menu.js\
    $ROOT/initialize.js > $TARGET