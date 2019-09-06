# ML² Face Emotion Result

## Access Jetson board via SSH
If you want to access to Jetson from your computer via SSH, you can follow the step below:
1. Install X server program
 - [Xquartz](https://www.xquartz.org/) for Mac.
 - [Xming](http://www.straightrunning.com/XmingNotes/) for Window.
 - [X11](https://help.ubuntu.com/community/ServerGUI) for Ubuntu.
 2. `ssh -X nvidia@[your board WIFI IP]` with password `nvidia`.
 3. Now you can run access to the board and use anything from the board!