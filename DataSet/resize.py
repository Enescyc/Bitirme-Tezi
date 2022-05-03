import os
from PIL import Image


basePath='/home/cyclones/Desktop/Bitirme-Tezi/DataSet/'


files = os.listdir(os.curdir)
files.remove('resize.py')


for file in (files):
    os.mkdir("resize"+file)
    count = len(os.listdir(file))
    size=20
    if count <20:
        size=count
    for i in range(size):
        fullPath=(basePath+file+'/'+str(i+1)+'.jpg')
        image = Image.open(fullPath)
        image = image.resize((127,127))
        image.save('resize'+file+'/'+str(i)+'.jpg')







