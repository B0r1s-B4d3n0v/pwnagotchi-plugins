# Instructions

> [!NOTE]
> Clocky can take 5 seconds to kick in! Patience!.

## Download Clocky

https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky.py

## Companion Button plugins

If you want Clocky to be triggered by a button check out my Github page for [clocky_btn.py](https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky_btn.py) - and follow the instructions at the top of that file as well. It's not required - but certainly beneficial.

You can also enable or disable Clocky via config.toml or WebGUI

Config `/etc/pwnagotchi/config.toml`\
WebGUI [http://10.0.0.2:8080/plugins](http://10.0.0.2:8080/plugins)

These config settings are all _optional_ - and loaded with the defaults.

config.toml
```
main.plugins.clocky.enabled = false
main.plugins.clocky.stop_deauth = false        # Do you want to stop dauthing while in Clocky mode?
main.plugins.clocky.movement = 'slide'         # Slide: Everything slides left and right.
                                               # Random: Moves up and down and side to side.
main.plugins.clocky.time_format = '%I:%M %p'
main.plugins.clocky.day_format = '%a'
main.plugins.clocky.date_format = '%m/%d'
main.plugins.clocky.face_position = (70, 5)
main.plugins.clocky.time_position = (70, 65)
main.plugins.clocky.day_position = (70, 95)
main.plugins.clocky.date_position = (112, 95)
```

> [!IMPORTANT]
> If you change the date / time format you will likely have to change the positions as well!.\
> The positions are *starting* positions - they will move.

<br /><br /><hr /><br /><br />

# Date & Time

## Formatting

If you need help with date / time format strings

[Python Date & Time Formatting](https://www.w3schools.com/python/python_datetime.asp)

## Fixing your Pi's clock.

1. First thing you have to do is set your timezone SSH into your Pi. Copy and past the following with your own timezone

    `sudo timedatectl set-timezone America/Chicago`

2. Setting the date / time
   - If you have an internet connection you can sync your system clock with NTP

        `sudo timedatectl set-ntp on`

   - if you do NOT have internet connection you can set your system clock manually with - note: 24hr clock format

        `sudo date --set="14 MAR 2025 13:14:15"`

3. However you set the date / time you can verify by just typing the word date.

    `date`
