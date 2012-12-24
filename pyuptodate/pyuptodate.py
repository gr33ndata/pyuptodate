#!python
# A small script to check all installed Python modules and update them
# Code inspired by Ramana Varanasi @sramana9
# Run with sudo if needed

# Author Tarek Amr (@gr33ndata)

import pip
from subprocess import call

VERBOSE = True

def printv(msg):
    if VERBOSE: print msg

def update():
    for dist in pip.get_installed_distributions():
        try:
            printv('\nUpdating %s:' % dist.project_name)
            call("pip install --upgrade " + dist.project_name, shell=True)
            printv('----------')
        except:
            pass

if __name__ == '__main__':

    update()
