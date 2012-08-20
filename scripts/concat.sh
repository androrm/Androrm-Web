ROOT=$PWD/../media/js
TARGET=$ROOT/androrm_concat.js

if [ $1 ] 
then
    TARGET=$1
fi

cat $ROOT/lib/prototype.js\
	$ROOT/lib/jquery.min.js\
	$ROOT/no_conflict.js\
	$ROOT/lib/boostrap.min.js\
	$ROOT/utils.js\
    $ROOT/initialize.js > $TARGET