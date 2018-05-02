# tiv-video
Terminal video viewer. Use a program like tiv (Terminal image viewer) to show a video in a terminal.

I thanks a lot Stefan Haustein for his programm : https://github.com/stefanhaustein/TerminalImageViewer.

## Python dependencies
- cv2
- argparse

### Installation
```bash
pip install cv2
pip install argparse
```

## External dependencies

- tiv

### Installation

Follow this tutorial: https://github.com/stefanhaustein/TerminalImageViewer


## Usage 

```bash
./tiv-video [-h] [-t TIV] [-v VID] [-s SPEED] [--tmp TMP]
```

## Control

- Press **space** to **play**/**pause**
- Press **q** or **esc** to quit

## TODO/NOTE

Be careful, for now: all your input are given to your shell after the execution of this programm. 

- Fix this annoying problem
- Add more features
  - Play, pause logo. 
  - Change speed in Runtime
  - Backward
  - Play sound :p
