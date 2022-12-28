import database 
import kautohelper
import ldhelper
import otphelper
from gui import Gui
from PyQt6 import QtCore, QtWidgets
import threading
import time

IconHeart = './assets/images/heart.png'
IconIsHeart = './assets/images/isHeart.png'

#khởi động ứng dụng5
db = database.Database();
tableDevices = db.model("devices")


adb = kautohelper.AutoADB()
listDevice = adb.GetDevices()

def control_device(x):
  # Use subprocess to run adb commands for the specified device
  while True:
    # if(adb.FindImage(x, IconIsHeart) == False):
    #     if(adb.FindImage(x, IconHeart)):
    #         adb.ClickImage(x, IconHeart)
    adb.Swipe(x, 250, 600, 250, 300, 250)
    time.sleep(3)
    


threads = []
for device_id in listDevice:
    print(device_id)
    t = threading.Thread(target=control_device, args=(device_id,))
    threads.append(t)

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Gui(tableDevices)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
