from PyQt6.QtSql import QSqlTableModel, QSqlQueryModel
import database
import kautohelper
import ldhelper
import otphelper
from gui import Gui
from PyQt6 import QtCore, QtWidgets
import threading
import time
import thirdparty.traodoisub as TraoDoiSub

IconHeart = './assets/images/heart.png'
IconIsHeart = './assets/images/isHeart.png'

adb = kautohelper.AutoADB()
# khởi động ứng dụng5
db = database.Database()
tableDevices = db.model("devies")


adb = kautohelper.AutoADB()
listDevice = adb.GetDevices()

def control_device(x):
    #   # Use subprocess to run adb commands for the specified device
    while True:
        TDS = TraoDoiSub.Traodoisub()
        data = TDS.getNV("tiktok_like")
        # print(data['data'])
        print('Lấy data: ',data)
        if "error" in data:
            TDS.nhanXu("TIKTOK_LIKE", "TIKTOK_LIKE_API")
            time.sleep(3)
            data = TDS.getNV("tiktok_like")
        for v in data['data']:
            adb.OpenUrl(v["link"])
            # time.sleep(3)
            if(adb.FindImage(x, IconIsHeart) == False):
                if(adb.FindImage(x, IconHeart)):
                    adb.ClickImage(x, IconHeart)
                    time.sleep(3)
                    print(x, 'click ne')
                    res = TDS.postNV("TIKTOK_LIKE_CACHE",v["id"])
                    if(res["cache"] >= 10):
                        time.sleep(1)
                        print(data["cache"])
                        TDS.nhanXu("TIKTOK_LIKE", "TIKTOK_LIKE_API")
            # adb.Swipe(x, 250, 600, 250, 300, 250)
            # time.sleep(3)
        print(x, 'lập')
        

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
    MainWindow = QtWidgets.QMainWindow()
    ui = Gui(tableDevices)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
