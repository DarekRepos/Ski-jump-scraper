# Ski-jump-scraper

Copies contents from the ski jump website and save to external file

Events are saved to SkiEvents.txt file, the program create this file when user erase it.

Note that there must be some ski events to see results in the file

# Run Python script at startup in Ubuntu if you want check the ski events on the system startup

**Copy repository files to your Desktop**

**Copy the python file to /bin:**

```
sudo cp -i  ~/Desktop/scrapeskisite.py /bin
```

**Add A New Cron Job:**

```
sudo crontab -e
```

Scroll to the bottom and add the following line (after all the #'s):

```commandline
reboot python ~/Desktop/scrapeskisite.py &
```

The “&” at the end of the line means the command is run in the background and it won’t stop the system booting up.

**Test it:**

```commandline
sudo reboot
```

