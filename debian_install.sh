#!/usr/bin/env sh

echo 'Installing Dependencies..'

# check if python is installed
if ! dpkg -s python3 >/dev/null 2>&1; then
    sudo apt-get install python3
else
    echo 'python3 is already installed'
fi

# check if python-pip is installed
if ! dpkg -s python3-pip >/dev/null 2>&1; then
    sudo apt-get install python3-pip
else
    echo 'python-pip is already installed'
fi

# install python libraries
if python3 -c 'import termtables' > /dev/null; then
    echo 'termtables is already installed'
else
    pip3 install termtables
fi

if python3 -c 'import termcolor' > /dev/null; then
    echo 'termcolor is already installed'
else
        pip3 install termcolor
fi

if python3 -c 'import bs4' > /dev/null; then
    echo 'beautifulsoup4 is already installed'
else
    pip3 install beautifulsoup4
fi

echo 'Done'

# move main file to /usr/bin and make it executable
sudo mv covid.py /usr/bin/covid
sudo chmod +x /usr/bin/covid

echo 'Succesfully Installed'
