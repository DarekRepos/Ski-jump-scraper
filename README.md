# Ski-jump-scraper

Copies contents from the ski jump website and save to external file

Events are saved to SkiEvents.txt file, the program create this file when user erase it.

Note that there must be some ski events to see results in the file

## Python version
tested with Python 3.10.6

## How to install in python 3
python3 -m pip install -r requirements.txt

## How to run

python3 scrapeskisite.py

## Run Python script at startup in Ubuntu if you want check the ski events on the system startup

**1. Copy repository files to your Desktop**

**2. Copy the python file to /bin:**

```
sudo cp -i  ~/Desktop/scrapeskisite.py /bin
```

**3. Add A New Cron Job:**

```
sudo crontab -e
```

Scroll to the bottom and add the following line (after all the #'s):

```commandline
reboot python ~/Desktop/scrapeskisite.py &
```

The “&” at the end of the line means the command is run in the background and it won’t stop the system booting up.

**4. Test it:**

```commandline
sudo reboot
```

