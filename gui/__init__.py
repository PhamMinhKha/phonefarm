from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtSql import QSqlTableModel, QSqlQueryModel
import ldhelper
import random
import gui.xuly as xuly


class Gui(object):
    def __init__(self, tableDeviverse):
        self.tableDeviverse:QSqlQueryModel = tableDeviverse
        self.xuly = xuly.Xuly()
    def clickne(self, selected, delsected):
        for ix in selected.indexes():
            print('select cell location Row: {0}, column: {1}'.format(ix.row(), ix.column()))
            value=ix.sibling(ix.row(),ix.column()).data()
            print(value)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableDevive = QtWidgets.QTableView(self.centralwidget)
        self.tableDevive.setGeometry(QtCore.QRect(0, 230, 801, 311))
        self.tableDevive.setObjectName("tableDevive")
        self.tableDevive.setModel(self.tableDeviverse)
        self.tableDevive.selectionModel().selectionChanged.connect(self.clickne)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 131, 91))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(11, 11, 61, 16))
        self.label.setObjectName("label")
        self.somayldplayer = QtWidgets.QSpinBox(self.groupBox)
        self.somayldplayer.setGeometry(QtCore.QRect(80, 10, 33, 19))
        self.somayldplayer.setProperty("value", 1)
        self.somayldplayer.setObjectName("somayldplayer")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 150, 171, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_selectDevice = QtWidgets.QLabel(self.groupBox_2)
        self.label_selectDevice.setGeometry(QtCore.QRect(10, 20, 35, 10))
        self.label_selectDevice.setObjectName("label_selectDevice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 18))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuLDPlayer = QtWidgets.QMenu(self.menubar)
        self.menuLDPlayer.setObjectName("menuLDPlayer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionT_o_m_y_m_i = QtGui.QAction(MainWindow)
        self.actionT_o_m_y_m_i.setObjectName("actionT_o_m_y_m_i")
        self.menuLDPlayer.addAction(self.actionT_o_m_y_m_i)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuLDPlayer.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ktool"))
        self.groupBox.setTitle(_translate("MainWindow", "LDPlayer"))
        self.label.setText(_translate("MainWindow", "Số máy chạy"))
        self.pushButton.setText(_translate("MainWindow", "Tạo thêm máy"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Nhiệm vụ"))
        self.label_selectDevice.setText(_translate("MainWindow", "TextLabel"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuLDPlayer.setTitle(_translate("MainWindow", "LDPlayer"))
        self.actionT_o_m_y_m_i.setText(_translate("MainWindow", "Tạo máy mới"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())

