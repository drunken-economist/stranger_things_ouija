import ConfigParser
config = ConfigParser.ConfigParser()
config.read("./config.ini")

def message_to_array(message):
    message_array = list(message)
    indices = [] 
    for this_char in message_array:
        this_led = led_index(this_char)
        if this_led != None:
            indices.append(this_led)
    return indices

def led_index(in_char):
    ascii_value = ord(in_char)
    if ascii_value > 96 and ascii_value < 123:
        ascii_value -= 32 #converts all chars to ucase ascii
    if ascii_value < 65 or ascii_value > 90:
        return None #bail out if it's a non-letter character

    try:
        led_index = config.get('led_assign', chr(ascii_value))
    except:
        led_index = ascii_value - 65

    return led_index
