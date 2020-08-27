# covid-terminal

It gathers info from Wikipedia using web-scraping and prints a table showing countries and their infection, death and recovery cases.

### Installation 
1) Install `python3` and `python-pip` (or `python3-pip`).
2) Clone the repository.
3) Change directory: `cd covid-terminal`.
4) Run `sudo pip3 install -r requirements.txt` to install the python libraries.
5) Move `covid.py` as `covid` to `/usr/bin/` and make it executable: `sudo mv covid.py /usr/bin/covid && sudo chmod +x /usr/bin/covid`.


### Usage
- `covid` - shows all the counties.
- `covid north` - shows north-american countries.
- `covid south` - shows south-american countries.
- `covid central`.
- `covid europe`.
- `covid oceania`.
- `covid asia`.
- `covid africa`.
