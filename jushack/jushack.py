# coding: utf8
import os
from os.path import expanduser
import subprocess
import serial
import serial.tools.list_ports
import sys
import time
import warnings

MAX_JUS = 1
MIN_JUS = 1

class JusHack:

    extra_size_dict = {
        u'petit': 1,
        u'grand': 2,
}
    jus_size_dict = {
        u'petit': 1,
        u'grand': 2,
}
    """
    ok
    """
 
    @staticmethod
    def compute_value(jus_size):
        print("preparing: %i %s %s %s" % (jus_size))
        size = JusHack.jus_size_dict.get(jus_size,
                                                JusHack.jus_size_dict[u''])
        return size 
    @classmethod
    def __init__(self, locale = "EN_US", extra = False):
        arduino_ports = [
                    p.device
                        for p in serial.tools.list_ports.comports()
                        for x in range (0, 10)
                        if 'ttyUSB%d' % x  in p.name or "ttyACM%d" % x in p.name]
        if not arduino_ports:
                raise IOError("No Arduino found")
        if len(arduino_ports) > 1:
                warnings.warn('Multiple Arduinos found - using the first')
        self.ser = serial.Serial(
                            port=arduino_ports[0],
                            baudrate = 9600
                        )
        if (extra):
            JusHack.jus_size_dict = JusHack.extra_size_dict
            
    @classmethod
    def pour(self, jus_size):
        jus_size =jus_size.encode('utf8')
        number = max(number, MIN_JUS)
        number = min(number, MAX_JUS)
        print(jus_size)
        value = JusHack.compute_value(jus_size, u'')
        print(value)
        self.ser.write('B%dE\n'%(value))

    
if (__name__ == "__main__"):
    c = JusHack();
    c.jus("normal", "petit",1)
    c.pour("normal", "grand",2)
    