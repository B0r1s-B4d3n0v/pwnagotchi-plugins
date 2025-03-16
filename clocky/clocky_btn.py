'''
  ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖▗▄▄▖ ▗▖ ▗▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖
    █  ▐▛▚▖▐▌▐▌     █  ▐▌ ▐▌▐▌ ▐▌▐▌     █    █  ▐▌ ▐▌▐▛▚▖▐▌▐▌
    █  ▐▌ ▝▜▌ ▝▀▚▖  █  ▐▛▀▚▖▐▌ ▐▌▐▌     █    █  ▐▌ ▐▌▐▌ ▝▜▌ ▝▀▚▖
  ▗▄█▄▖▐▌  ▐▌▗▄▄▞▘  █  ▐▌ ▐▌▝▚▄▞▘▝▚▄▄▖  █  ▗▄█▄▖▝▚▄▞▘▐▌  ▐▌▗▄▄▞▘

https://github.com/B0r1s-B4d3n0v/pwnagotchi-plugins/blob/main/clocky/clocky_btn_readme.md

'''

import logging
import pwnagotchi.plugins as plugins
import pwnagotchi.plugins as toggle

class ClockyBtn(plugins.Plugin):
    __author__ = 'Boris Badenov https://github.com/B0r1s-B4d3n0v'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Button de/activation for my Clocky plugin - see instructions at the top of the file or on GitHub'

    def __init__(self):
        self._ready = False
        self._state = None
        self._msg = None

    def on_loaded(self):
        self._ready = True
        logging.info(f"[{self.__class__.__name__}] plugin loaded")

    def on_webhook(self, path, request):
        if self._ready:
            en_dis_able = request.args.get('able')

            # This allows Clocky to work off of a single button / command
            # if it's already enabled, and you enable it again - it disables it.
            if en_dis_able == "en" and self._state == "en":
                en_dis_able = "dis"

            if en_dis_able == "en":
                # Super Stealth Sammy Squirrel activate!
                toggle.toggle_plugin("clocky", enable=True)
                logging.info(f"[{self.__class__.__name__}] => enabling Clocky")
                self._state = "en"
                self._msg = "Clocky Now Enabled"

            elif en_dis_able == "dis":
                # Does not seem to hurt anything to disabled a disabled plugin
                toggle.toggle_plugin("clocky", enable=False)

                if self._state == "en":
                    logging.info(f"[{self.__class__.__name__}] => disabling Clocky")
                else:
                    logging.error(f"[{self.__class__.__name__}] Clocky was not enabled!")
                    self._msg = "Clocky was not enabled!"
                self._state = "dis"
                self._msg = "Clocky Now Disabled"

        # Lets play nice and give a proper response.
        from flask import make_response
        response = make_response(self._msg)
        response.status_code = 200
        response.headers['Content-Type'] = 'text/plain'
        return response
