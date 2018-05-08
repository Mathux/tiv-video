# tiv-video
Terminal video viewer. Use a program like tiv (Terminal image viewer) to show a video in a terminal.

I thanks a lot Stefan Haustein for his programm : https://github.com/stefanhaustein/TerminalImageViewer.

## Python dependencies
- cv2
- argparse


### Installation for python 2
```bash
pip install --user cv2
pip install --user argparse
```

## External dependencies

- tiv

### Installation

Follow this tutorial: https://github.com/stefanhaustein/TerminalImageViewer


## Usage 

```bash
usage: tiv-video [-h] [--tiv TIV] [--tmp TMP] [--sys-mode] vid

Read and show a video in a terminal, default args in config.py

required arguments:
  vid         video file

optional arguments:
  --tiv TIV   tiv programm, default: /usr/local/bin/tiv
  --tmp TMP   tmp file, default: /tmp/__tivid__.jpg
  --sys-mode  if it is not working try with this mode
```

## Control

- Press **space** to **play**/**pause**
- Press **q** or **esc** to quit
- *Experimental*: 
  - Press **right arrow** to speed up x2
  - Press **left arrow** to put the normal speed


## TODO/NOTE

- Add more features
  - Change speed in Runtime
  - Backward
  - Play sound :p


## Icons

<div>Icons made by <a href="https://www.flaticon.com/authors/daniel-bruce" title="Daniel Bruce">Daniel Bruce</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
