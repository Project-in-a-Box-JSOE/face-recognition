"""
helloTerminal.py

ECE196 Face Recognition Project
Author: Brian Henriquez

The following is a algorithmic breakdown of how this function should work...
Using a main function:
    1) Print out the current time for the next ten seconds
    2) Terminate with a "Goodbye, World"
"""
from datetime.datetime import now
from time import time

def printCurTime():
    ''' Use a loop to print the current time for 10 seconds'''
    startTime = time()
    while(time() < startTime + 10):
        # Your code here
        pass

def printMethod():
    ''' Prints the final message '''
    pass

# Use the "main" module if declaration here along with the completed functions
