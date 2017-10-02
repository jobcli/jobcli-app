#!/bin/env/bash
cd $HOME/Projects/jobcli-app/

SCRIPTVERSION=$(gsed -ne 's/.*version_option(\x27\([^ ]*\)\x27.*/\1/p' jobcli.py)
SETUPVERSION=$(gsed -ne 's/.*version=\x27\([^ ]*\)\x27.*/\1/p' setup.py)

# echo "script version: "$SCRIPTVERSION
# echo "setup version: "$SETUPVERSION

# Check that versions are consistent
## in setup.py and jobcli.py
if [ "$SCRIPTVERSION" != "$SETUPVERSION" ]
then
    echo 'Different version numbers in setup.py and jobcli.py'
else
    PIPVERSION=$(pip3 search jobcli | gsed -ne 's/^jobcli (\([^ ]*\)).*$/\1/p')
    # echo "pip version: "$PIPVERSION

    if [ "$SCRIPTVERSION" == "$PIPVERSION" ]
    then
        echo 'This version has already been deployed to PyPI'
    else
        #1 Generate distribution and wheel
        python3 setup.py sdist &&
        python3 setup.py bdist_wheel --universal &&

        #2 Upload to PyPI
        twine upload "dist/jobcli-"$SCRIPTVERSION*

        #3 pip update
        # pip3 install jobcli --upgrade
    fi
fi

