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

