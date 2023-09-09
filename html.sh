#!/bin/bash

CWD=`pwd`
filename=$1

snap run firefox --headless --screenshot --window-size=600,448 file://$CWD/$filename
python3 image.py screenshot.png
