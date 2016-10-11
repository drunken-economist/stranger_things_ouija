#STATUS: In progress, not functional yet.

# stranger_things_ouija
A replica of the christmas light "ouija" board from Stranger Things.

A raspberry pi 3 acts as a twitter client to find all the tweets with a given hashtag, sanitizes them and splits them into characters, before converting them to a light index and passing along to an arduino for ultimate control of the lights. The arduino takes the indeces and, using some awesome libraries from Adafruit, sends them to a string of WS2812 (or WS2812b) addressable LEDs. 

#Installation

#Wiring

#Usage
1. SSH to your raspi and `git clone https://github.com/drunken-economist/stranger_things_ouija/`
1. Create a new twitter app for yourself: https://apps.twitter.com/, and authorize it to your account. 
1. Open the config file with `nano config.inig`. Copy the `consumer key`, `consumer secret`, `access token` and `access token secret` to the config file. Lastly, update the search term in the config file to reflect whatever content you want to find and display from twitter. This step is wholly optional if you want to just have the lights send pre-made messages instead, or write your own data source.
2. Update the LED mapping on the config. This annoyingly manual because each prop is constructed differently. By default, it's mapped for a string of 50 LEDs with the controller on the Z end, with every other light representing a letter, except for A and B on consecutive lights. TBH the alphabet should have only 25 letters and this would be less messy.


#Troubleshooting
**Nothing lights up at all. Your project is garbage and I want my money back**  
For real though, if you're having issues you can't figure out, shoot me a message, I'm happy to help!

**Only the first 26/50 lights on my string of 50/100 lights works!**  
The config.ini file has light assignments. These are manual to allow you to adjust each them depending on your actual construction. If the config.ini file can't be read, message.py will default to using the leds assigned 0-25 (first 26 lights from the controller)

**This lights work in the initial test, but then turn off and don't light up anymore**  
Is anyone tweeting at them? If not, I suggest making friends to tweet or convincing 4chan to send you messages. If they *are* tweeting at you and no messages are being passed through, log on to your Pi and check the logging info. There might be something useful there if I ever learn my lesson and add good logging

#FAQ
**Why not build the whole thing on the arduino? This seems like overkill**  
Because I'm bad at C and I had the Pi laying around already.

**Okay then, why not build the whole thing on the Pi? This seems like overkill**  
The WS2812 standard requires some pretty precise timing, which the Pi isn't really capable of without some massaging. If you're feeling ambitious, submit it a PR using [jgraff/rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library and I will gleefully merge it without reviewing.
