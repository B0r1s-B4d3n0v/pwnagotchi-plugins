# Instructions

> [!NOTE]
> Clocky can take 5 seconds to kick in! Patience!.

## Download Clocky

https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky.py

## Download Clocky_btn

https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky_btn.py


> [!IMPORTANT]
> This plugin (clocky_btn.py) must be enabled at all times if you want the button to enable / disable [Clocky](https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky.py).


## Usage

This script is best triggered with your PiSugar Power Manager and these instructions will pertain to that. I will add normal GPIO buttons at some point, but not right now.


> [!NOTE]
> You can use one button function or two.\
> ie: Single Tap can both start and stop Clocky.\
> ie: Single Tap to start, Double Tap to stop.

### For Single Tap to start and stop

1. Go to your Power Manager in your browser: [http://10.0.0.2:8421](http://10.0.0.2:8421)
2. Change Single Tap to "Custom Shell" and click the "Edit" button
3. Copy and paste the line below into the text field.

    `sudo curl http://10.0.0.2:8080/plugins/clocky_btn?able=en`

4. That's it. You're done. 
   - Tap once to start
   - Tap again to stop.
    
> [!NOTE]
> Clocky can take 5 seconds to kick in! Patience!. 

### For Single Tap to Start and Double Tap to Stop

1. Go to your Power Manager in your browser: http://10.0.0.2:8421
2. Change Single Tap to "Custom Shell" and click the "Edit" button
3. Copy and paste the line below into the text field.

    `sudo curl http://10.0.0.2:8080/plugins/clocky_btn?able=en`

4. Now change Double Tap to "Custom Shell" and click the "Edit" button
5. Copy and paste the line below into the text field.

    `sudo curl http://10.0.0.2:8080/plugins/clocky_btn?able=dis`

6. That's it. You're done.
   - Tap once to start.
   - Double Tap to stop.

> [!NOTE]
> Clocky can take 5 seconds to kick in! Patience!. 
   
# Config.toml

`main.plugins.clocky_btn.enabled = true`
