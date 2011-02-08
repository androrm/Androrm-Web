#!/bin/sh
cd ../androrm/ || exit 1

cd $OLDPWD

# Mac: prevent creation of . files resulting from extended attributes
export COPYFILE_DISABLE=true

tar cvzf androrm.tar.gz  --exclude='androrm/assets' \
                         --exclude='*.tmproj' \
                         --exclude="*.json" \
                         --exclude="Sendinel/compress.sh" \
                         --exclude='*.pyc' \
                         --exclude='.DS_Store' \
                         --exclude='.gitignore' \
                         ../androrm

echo "Done"

