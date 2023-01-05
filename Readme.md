## Nautilus Hider
#### Easily hide files and foler in nautilus file manager

### Background motivation
There are certain auxiliary files that are necessary for certain programs to function properly, but may not be necessary for humans to view. It is often best to keep these files hidden. However, hiding files in [Nautilus file manager](https://en.wikipedia.org/wiki/GNOME_Files) can be difficult. There are two options: (a) You can rename the file by adding a `.` to the beginning of the file name, but this may cause issues with certain programs. (b) You can create a `.hidden` file and include the name of the file within it. However, this method requires the exact full name of the file, glob patterns do not work, and it also does not work for subdirectories. This code streamlines the process of creating `.hidden` files by adding a right-click context menu option.


### Installation:
Simply download and run the [`nautilusHider.py`](https://github.com/Koushikphy/Nautilus-Hider/blob/main/natilusHider.py) python code. This will install the necessary scripts in the nautilus scripts folder. Additionally, you can specify certain file patterns in the python code that you always want to be hidden."


### Usage:
To hide a file, right click on it and select `Scripts` > `nhider` > `hide.py`. Alternatively, you can choose `hideAll.py` to hide all files that match the patterns specified in the python code. To make all hidden files visible again, select `unhideAll.py` or simply delete the `.hidden` file from the current directory.
