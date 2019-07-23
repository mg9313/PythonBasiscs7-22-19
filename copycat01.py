#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/student/pyb/5g_research/")

shutil.copy("test1.txt", "test1.copy")

os.chdir("/home/student/pyb/")


shutil.copytree("5g_research/", "5g_research_backup/")



