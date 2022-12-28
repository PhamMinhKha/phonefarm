from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlResult
import sys


class Database:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./database/phonefarm.db")
        if not self.db.open():
            print("Failed to open database")
            sys.exit(1)

    def model(self, table):
        projectModel = QSqlQueryModel()
        projectModel.setQuery("select * from devices")
        # data = projectModel.query().exec()
        print(projectModel.record(0).value("sonhiemvu"))
        return projectModel
