from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlResult 
import sys
class Database:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.db")
        if not self.db.open():
            print("Failed to open database")
            sys.exit(1)
       
    def model(self, table):
        projectModel = QSqlQueryModel()
        projectModel.setQuery(("select * from {0}").format(table),self.db)
        return projectModel