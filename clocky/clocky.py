'''
  ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖▗▄▄▖ ▗▖ ▗▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖
    █  ▐▛▚▖▐▌▐▌     █  ▐▌ ▐▌▐▌ ▐▌▐▌     █    █  ▐▌ ▐▌▐▛▚▖▐▌▐▌
    █  ▐▌ ▝▜▌ ▝▀▚▖  █  ▐▛▀▚▖▐▌ ▐▌▐▌     █    █  ▐▌ ▐▌▐▌ ▝▜▌ ▝▀▚▖
  ▗▄█▄▖▐▌  ▐▌▗▄▄▞▘  █  ▐▌ ▐▌▝▚▄▞▘▝▚▄▄▖  █  ▗▄█▄▖▝▚▄▞▘▐▌  ▐▌▗▄▄▞▘

https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky_readme.md

'''

from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK, WHITE
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import datetime
import time
import random

class Clocky(plugins.Plugin):
    __author__ = 'Boris Badenov https://github.com/B0r1s-B4d3n0v'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Turns pwnagotchi display into a cheeky "desk clock" while the unit remains fully functional.'

    def __init__(self):
        self._ready = False
        self._agent = None
        self._agent_da = None
        self._next = 0
        self._slide_dir = "left"
        self._slide_x = 70
        self._start = time.time()
        self._state = 0
        self._uiItems = None
        self._uiItemsPos = dict()

    def on_loaded(self):
        self._stop_deauth = self.options.get('stop_deauth', False)
        self._movement = self.options.get('movement', 'slide') # slide | random

        self._time_format = self.options.get('time_format', '%I:%M %p')
        self._day_format = self.options.get('day_format', '%a')
        self._date_format = self.options.get('date_format', '%m/%d') # %m/%d/%y

        self._face_position = self.options.get('face_position', (70, 5) )
        self._time_position = self.options.get('time_position', (70, 65) )
        self._day_position = self.options.get('day_position', (70, 95) )
        self._date_position = self.options.get('date_position', (112, 95) )
        logging.info(f"[{self.__class__.__name__}] plugin loaded")

    def on_ui_setup(self, ui):
        self._uiItems = ui._state._state
        try:
            for ui_item_name in self._uiItems:
                self._uiItemsPos[ui_item_name] = self._uiItems[ui_item_name].xy
                self._uiItems[ui_item_name].xy = (-1000, -1000)
            self._uiItemsPos['day']  = (self._day_position[0],  self._day_position[1])
            self._uiItemsPos['time'] = (self._time_position[0], self._time_position[1])
            self._uiItemsPos['date'] = (self._date_position[0], self._date_position[1])
        except Exception as err:
            logging.error(f"[{self.__class__.__name__}] Error saving UI positions: {err} | {self._uiItems}")

        ui.add_element('day',  LabeledValue(color=BLACK, label='', value='', position=(self._day_position[0],  self._day_position[1]),  label_font=fonts.Huge, text_font=fonts.Huge))
        ui.add_element('time', LabeledValue(color=BLACK, label='', value='', position=(self._time_position[0], self._time_position[1]), label_font=fonts.BoldBig, text_font=fonts.BoldBig))
        ui.add_element('date', LabeledValue(color=BLACK, label='', value='', position=(self._date_position[0], self._date_position[1]), label_font=fonts.Huge, text_font=fonts.Huge))
        self._ready = True
        # self.clear()

    def on_ready(self, agent):
        self._agent = agent
        if self._stop_deauth == True:
            self._agent_da = agent._config['personality']['deauth']
            agent._config['personality']['deauth'] = False



    def on_ui_update(self, ui):
        if self._ready:
            with ui._lock:
                now = datetime.datetime.now()
                try:
                    if self._movement == "random":
                        if time.time() > self._next:
                            self._next = int(time.time()) + 3
                            self._state = (self._state + 1) % 3

                            x = random.randint(0, 70)
                            y = random.randint(-5, 5)
                            self._uiItems['day'].xy  = (x,    self._uiItemsPos['day'][1]+y)
                            self._uiItems['time'].xy = (x,    self._uiItemsPos['time'][1]+y)
                            self._uiItems['date'].xy = (x+50, self._uiItemsPos['date'][1]+y)
                            self._uiItems['face'].xy = (x,    self._uiItemsPos['face'][1]+y)

                            if self._state == 2:
                                self._uiItems['day'].color  = BLACK
                                self._uiItems['time'].color = WHITE
                                self._uiItems['date'].color = BLACK
                            elif self._state == 1:
                                self._uiItems['day'].color  = WHITE
                                self._uiItems['time'].color = BLACK
                                self._uiItems['date'].color = BLACK
                            else:
                                self._uiItems['day'].color  = BLACK
                                self._uiItems['time'].color = BLACK
                                self._uiItems['date'].color = WHITE

                    else:
                        if self._slide_x <= 0:
                            self._slide_dir = "right"
                        elif self._slide_x >= 70:
                            self._slide_dir = "left"


                        if self._slide_dir == "left":
                            x = self._slide_x - 5
                        else:
                            x = self._slide_x + 5

                        self._slide_x = x
                        self._uiItems['day'].xy  = (x,    self._uiItemsPos['day'][1]-10)
                        self._uiItems['time'].xy = (x,    self._uiItemsPos['time'][1]-25)
                        self._uiItems['date'].xy = (x+95, self._uiItemsPos['date'][1]-10)
                        self._uiItems['face'].xy = (x+45, 5)

                    ui.set('day',  now.strftime(self._day_format))
                    ui.set('time', now.strftime(self._time_format))
                    ui.set('date', now.strftime(self._date_format))

                except Exception as err:
                    logging.warn(f"[{self.__class__.__name__}] Error on ui update: {err} | {self._uiItems}")

    def on_unload(self, ui):
        with ui._lock:
            try:
                for ui_item_name in self._uiItemsPos:
                    self._uiItems[ui_item_name].xy = self._uiItemsPos[ui_item_name]
            except Exception as err:
                logging.error(f"[{self.__class__.__name__}] Error resitting UI positions: {err} | {self._uiItems}")

            try:
                if self._stop_deauth == True:
                    self._agent._config['personality']['deauth'] = self._agent_da
            except Exception as err:
                logging.error(f"[{self.__class__.__name__}] Error resetting deauth: {err} | {self._agent_da}")


            ui.remove_element('day')
            ui.remove_element('time')
            ui.remove_element('date')
            logging.info(f"[{self.__class__.__name__}] plugin unloaded")

    def clear(self):
        from pwnagotchi.ui.hw.libs.waveshare.epaper.v2in13_V3.epd2in13_V3 import EPD
        self._display = EPD()
        self._display.Clear(0xFF)
