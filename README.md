# covid-terminal

It gathers data from Wikipedia with beautifulsoup4 and prints a table in the terminal showing infection, death and recovery cases in each country.


### Installation
If you want to try it, try the installation scripts first if you have a debian or arch based distro:

1 - `git clone https://github.com/gon2410/covid-terminal.git`

2 - `cd covid-terminal`

3 - `sudo chmod +x debian_install.sh` / `sudo chmod +x arch_install.sh`

4- `./debian_install.sh` / `./arch_install.sh`

But, if they don't work or you have a different distro then you need:
* python3
* python-pip

..and the following python libraries:
* beautifulsoup4
* lxml
* termtables
* termcolor

After that you need to:

1 - `git clone https://github.com/gon2410/covid-terminal.git`

2 - `cd covid-terminal`

3 - `sudo mv covid.py /usr/bin/covid && sudo chmod +x /usr/bin/covid`
`
 
### Usage
* `covid` - shows table with every country
* `covid north` - shows countries of north america
* `covid south` - shows countries of south america 
* `covid europe` - shows countries of europe
* `covid oceania` - of oceania
* `covid asia` - of asia
* `covid africa` - of africa
