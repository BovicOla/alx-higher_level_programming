#!/usr/bin/python3
"""Contains the read_file funtions
"""

def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    """
    with open(filename,"r" encoding="utf-8") as myFile:
        print(myFile.read(), end="")
