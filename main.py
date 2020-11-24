import os
from PIL import Image

#Current directory
dir = os.path.abspath(os.curdir)

#Find all jpg file and replace metta
for f in os.scandir(dir):
    if f.is_file() and f.path.split('.')[-1].lower() == 'jpg':
        #print(f.path)
        image = Image.open(f.path)
        image.save(f.path)
