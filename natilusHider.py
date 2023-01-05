from pathlib import Path 
import os 


filePatternToHide = [
    "*.out",
]



home = str(Path.home())


rootDir = f"{home}/.local/share/nautilus/scripts/nhider"


os.makedirs(rootDir,exist_ok=True)


hidFile = f"{rootDir}/hide.py"
unhidFile = f"{rootDir}/unhideAll.py"
hidallFile = f"{rootDir}/hideAll.py"



# create a `.hidden` file and hide the selected files
with open(hidFile,'w') as f:
    f.write('''#!/usr/bin/env python

import os, sys

hidPath = f"{os.getcwd()}/.hidden"

filesToHide ='\\n' + '\\n'.join(sys.argv[1:])

with open(hidPath, 'a' if os.path.exists(hidPath) else 'w') as f:
    f.write(filesToHide)
''')


# just delet the `.hidden` file
with open(unhidFile,'w') as f:
    f.write('''#!/usr/bin/env python

import os

hidPath = f"{os.getcwd()}/.hidden"
if os.path.exists(hidPath):
    os.remove(hidPath)
''')




# glob the pattern and hide 
with open(hidallFile,'w') as f:
    f.write(f'''#!/usr/bin/env python

import os
from glob import glob

hidPath = f"{{os.getcwd()}}/.hidden"

filePtrn = {filePatternToHide}

ff = []
for p in filePtrn:
    ff += glob(p)

filesToHide ='\\n' + '\\n'.join(ff)

with open(hidPath, 'a' if os.path.exists(hidPath) else 'w') as f:
    f.write(filesToHide)
''')


os.chmod(hidFile,0o766)
os.chmod(unhidFile,0o766)
os.chmod(hidallFile,0o766)