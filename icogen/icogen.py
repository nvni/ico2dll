
from PIL import Image
import os

def getIco(filename):
  
    name = filename.split('.')[0]
    img = Image.open(filename)
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save(f'{name}.ico', sizes=icon_sizes, quality=90)
   
    # img.show()
    img.close()

listFile = os.listdir('png')
for i in listFile:
    a = i.split('.')
    if(os.path.isfile(os.path.join(os.getcwd(),'png', i))):
        try:
            getIco(os.path.join('png',i))
            # os.rename(os.path.join(os.getcwd(), i), os.path.join(
            #     os.getcwd(), a[0]+'.'+str(a[len(a)-1])))
        except FileExistsError:
            print(os.path.join(os.getcwd(), i))
