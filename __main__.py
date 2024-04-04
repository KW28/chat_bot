from plugins import test
from virtual_assistant import VirtualAssistant
import sys

def main():
    sys.dont_write_bytecode = True
    #VirtualAssistant().run()
    test.tree_display('')


if __name__=='__main__':
    main()