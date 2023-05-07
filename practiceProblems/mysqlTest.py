from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase
from PyQt4.QtGui import QApplication,QListView,QTableView
import sys

app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setDatabaseName("app")
db.setUserName("root")
db.setPassword("")
db.open()

projectModel = QSqlQueryModel()
projectModel.setQuery("select name from customers",db)

projectView = QTableView()
projectView.setModel(projectModel)

projectView.show()

model = projectView.model()
indexes = projectView.selectionModel().currentIndex().row()

app.exec_()

