#!/usr/bin/env sh

echo 'Installing Dependencies..'

# check if python is installed
if sudo pacman -Qi python > /dev/null; then
    echo 'python is already installed'
else
    sudo pacman -S python
fi

# check if python-pip is installed
if sudo pacman -Qi python-pip > /dev/null; then
    echo 'python-pip is already installed'
else
    sudo pacman -S python-pip
fi

# install python libraries
if python -c 'import termtables' > /dev/null; then
    echo 'termtables is already installed'
else
    pip install termtables
fi

if python -c 'import termcolor' > /dev/null; then
    echo 'termcolor is already installed'
else
    pip install termcolor
fi

if python -c 'import bs4' > /dev/null; then
    echo 'beautifulsoup4 is already installed'
else
    pip install beautifulsoup4
fi

echo 'Done'

# move main file to /usr/bin and make it executable
sudo mv covid.py /usr/bin/covid
sudo chmod +x /usr/bin/covid

echo 'Succesfully Installed'
