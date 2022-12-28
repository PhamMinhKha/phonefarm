import database 
import kautohelper
import ldhelper
import otphelper
from gui import Gui
from PyQt6 import QtCore, QtWidgets

#khởi động ứng dụng5
db = database.Database();
tableDevices = db.model("devices")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Gui(tableDevices)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
