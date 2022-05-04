import os
from PIL import Image


basePath='/home/cyclones/Desktop/Bitirme-Tezi/genderDataSet/Training/male'


files = os.listdir(os.curdir)
files.remove('gender-dataset-link.txt')



for file in (files):
    os.mkdir("resize"+file)
    count = len(os.listdir(file))
    for i in range(count):
        fullPath=(basePath+file+'/'+str(i+1)+'.jpg')
        image = Image.open(fullPath)
        image = image.resize((127,127))
        image.save('resize'+file+'/'+str(i)+'.jpg')







