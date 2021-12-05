from pip._vendor.distlib.compat import raw_input

import tkinter.filedialog
import os

plik=open(tkinter.filedialog.askopenfilename(),"r")
tesk=str(plik)
print(tesk)
n= 0
if plik.readable():
    print("File content:")
    tekst= plik.readlines()
    print(tekst)
    for l in tekst:
       n+=1
    print(n)

# file existence check
print(os.path.exists(tesk))

# list the files
print(os.listdir("C:/"))

from pathlib import Path
p = Path('C:/') # if you want to write to current directory
with open(p / 'AutoMapaSetupLog.txt', 'w') as f:
  f.write('test message')
