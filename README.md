# Ski-jump-scraper

This script copies contents from the Ski Jump website and saves them to an external file.

Events are saved to the "SkiEvents.txt" file; the program creates this file when the user erases it.

**Note that** there must be some ski events to see results in the file.

## Python version
tested with Python 3.10.6

## How to run (example for POSIX platform)
Clone or download this repository

Create virtual enviroment
`python -m venv venv`

Activate virtual enviroment
`source venv/bin/activate`

Install required packages 
`python3 -m pip install -r requirements.txt`

Run script command
`python3 scrapeskisite.py`

You should have created a file named "SkiEvents.txt."
[<img src="examples/examples.png">](http://example.com/)

## Contributing
issue tracker: https://github.com/DarekRepos/Ski-jump-scraper/issues

## License
MIT License

[License file](https://github.com/DarekRepos/Ski-jump-scraper/blob/master/LICENSE)
