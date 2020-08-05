#!/usr/bin/env sh

echo 'Installing Dependencies..'

sudo pacman -S python3

pip install selenium
pip install termtables
pip install termcolor
pip install beautifulsoup4

echo 'Done'

sudo mv covid.py /usr/bin/covid
sudo chmod +x covid

echo 'Succesfully Installed'
