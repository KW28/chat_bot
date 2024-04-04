import sys
from plugin import plugin

@plugin('quit')
def quit(s):
    sys.exit()