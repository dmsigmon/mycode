#! /usr/bin/env python3

import os 
import shutil

shutil.copy("example1.txt", "movedfile.txt")

os.chdir("/home/student")
shutil.copy("myprintedinfo", "copiedfile,txt")
