#Se define
import sys

def arg(*args):
    for arg in args:
        print(arg)

arg(sys.argv)