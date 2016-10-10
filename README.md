# stranger_things_ouija
A replica of the christmas light "ouija" board from Stranger Things.

A raspberry pi 3 acts as a twitter client to find all the tweets with a given hashtag, sanitizes them and splits them into characters, before converting them to a light index and passing along to an arduino for ultimate control of the lights. The arduino takes the indeces and, using some awesome libraries from Adafruit, sends them to a string of WS2812 (or WS2812b) addressable LEDs. 

#Installation

#Wiring

#Usage

#FAQ
**Why not build the whole thing on the arduino? This seems like overkill**
Because I'm bad at C and I had the Pi laying around already.

**Okay then, why not build the whole thing on the Pi? This seems like overkill**
The WS2812 standard requires some pretty precise timing, which the Pi isn't really capable of without some massaging. If you're feeling ambitious, submit it a PR using [jgraff/rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library and I will gleefully merge it without reviewing.
