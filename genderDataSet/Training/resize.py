import os
from PIL import Image


basePath='/home/cyclones/Desktop/Bitirme-Tezi/genderDataSet/Training/'


files = os.listdir(os.curdir)
files.remove('resize.py')


print(files)

for file in (files):
    count = len(os.listdir(file))
    os.mkdir('resize'+file)
    images = os.listdir(os.curdir+'/'+file)
    for i in images:
        fullPath=(basePath+file+'/'+i)
        image = Image.open(fullPath)
        image = image.resize((127,127))
        image.save('resize'+file+'/'+str(i)+'.jpg')







