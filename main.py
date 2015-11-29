from evdev import InputDevice, categorize, ecodes
from evdev import InputDevice, list_devices

import os
import subprocess

devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
	print(dev.fn, dev.name, dev.phys)

dev = InputDevice('/dev/input/event0')

scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r',
    20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
    50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

capscodes = {
    0: None, 1: u'ESC', 2: u'!', 3: u'@', 4: u'#', 5: u'$', 6: u'%', 7: u'^', 8: u'&', 9: u'*',
    10: u'(', 11: u')', 12: u'_', 13: u'+', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'{', 27: u'}', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u':',
    40: u'\'', 41: u'~', 42: u'LSHFT', 43: u'|', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u'<', 52: u'>', 53: u'?', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

#setup vars
x = ''
caps = False
store = False

def write_file(message):
	fichier = open("data.txt", "w")
	fichier.write(message)
	fichier.close()

def upload_file():
	pass

def get_key(code):
	code = data.scancode 
	return u'{}'.format(scancodes.get(data.scancode)) or u'UNKNOWN:[{}]'.format(data.scancode)

def audio(k):
	subprocess.call(["mpg321", "http://translate.google.com/translate_tts?tl=fr&client=tw-ob&q=%s" % k])

for event in dev.read_loop():
	if event.type == ecodes.EV_KEY:
		data = categorize(event)
		if data.keystate == 1:#key down
			key_lookup = get_key(data.scancode)
			print data.scancode,key_lookup
			audio(key_lookup)
			if (data.scancode == 21):#KEY Y
				store = True 
			if store:
				x = x + key_lookup  # Print it all out!
			if(data.scancode == 28):#KEY entree
                		print "message => " + x
				write_file(x)
				x = ''
				store = False
