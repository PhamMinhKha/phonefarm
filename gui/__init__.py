from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtSql import QSqlTableModel, QSqlQueryModel


class Gui(object):
    def __init__(self, tableDeviverse):
        self.tableDeviverse = tableDeviverse
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableDevive = QtWidgets.QTableView(self.centralwidget)
        self.tableDevive.setGeometry(QtCore.QRect(0, 230, 801, 311))
        self.tableDevive.setObjectName("tableDevive")
        self.tableDevive.setModel(self.tableDeviverse)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 131, 91))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 61, 17))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 10, 84, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.somayldplayer = QtWidgets.QSpinBox(self.widget)
        self.somayldplayer.setProperty("value", 1)
        self.somayldplayer.setObjectName("somayldplayer")
        self.horizontalLayout.addWidget(self.somayldplayer)
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
        self.pushButton.setText(_translate("MainWindow", "Tạo thêm máy"))
        self.label.setText(_translate("MainWindow", "Số máy chạy"))
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

