#encoding=utf-8

from PIL import Image
import sys
import os
import time

from ImageEditor.textEditor import text_editor
from ImageEditor.text_menu_server import *



def get_file():
    """Creates image object from sys.argv or from console. Returns image and filename"""
    try:
        if (len(sys.argv) >= 2):
            filename = sys.argv[1]
            im = Image.open(filename)
            return (im, filename)
        else:
            filename = input("\nWhat file do you want to edit? : ")
            im = Image.open(filename)
            return (im, filename)
    except (IOError):
        print ("\nFile " + filename + " does not exist")
        exit(0)


def print_menu():
    print( """
    ----------------------------------------
    FOLLOW THE STEPS:
     1st - introduce the text
     2nd - introduce the text's position
     3rd - introduce the style

    CONTROLS
    0  - SAVE IMAGE # and CLOSE
    ----------------------------------------
    """)
    

def main():
    print ("------------------------------")
    print ("100BRAINS - TEXT EDITOR")

    im, filename = get_file()
    new_im = prepare_image(filename)
    edits = [] # stores all the edits (image object) so the user can undo effects and filters
    

    print_menu()
    option = "Y"
    while(option=="Y" or option=="y"):
        print ("*-----------------------------------*")
        text = input("TEXT: ")
        pos = input("TEXT POSITION (top, center, bottom, mix): ")
        style = input("STYLE (meme, solid snap, or shaded snap): ")
        new_im = menu_server(None, text, pos, style, new_im)
        edits.append(new_im)
        new_im.show()
        print ("*-----------------------------------*")
        option = input("Do you want to continue writting? (y/N)")

    
    im.save(filename, quality = 100)
    exit(0)
        


#Run the program
main()
