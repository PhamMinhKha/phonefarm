import kautohelper
from PIL import Image
from threading import Thread
myImage = Image.open('./assets/images/b.png')
IconHeart = './assets/images/heart.png'
IconIsHeart = './assets/images/isHeart.png'

adb = kautohelper.AutoADB()
listDevice = adb.GetDevices()
for x in listDevice:
    # adb.Swipe(x, 0, 0, 250, 400, 1000)
    while True:
        print(adb.FindImage(x, IconIsHeart))
        if(adb.FindImage(x, IconIsHeart) == False):
            if(adb.FindImage(x, IconHeart)):
                adb.ClickImage(x, IconHeart)
        adb.Swipe(x, 250, 600, 250, 300, 250)
    # adb.Install(x, './assets/images/apk/tiktok-27-3-3.apk')



print(listDevice)