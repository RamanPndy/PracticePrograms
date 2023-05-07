from PyQt4 import  QtGui,Qt,QtSql,QtWebKit
import sys,MySQLdb,urllib

class A(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("dancebook")
        self.db.setUserName("root")
        self.db.setPassword("")
        self.db.open()

        self.projectModel = QtSql.QSqlQueryModel()
        self.projectModel.setQuery("select name from dance",self.db)

        self.projectView = QtGui.QListView()
        self.projectView.setModel(self.projectModel)

        # self.projectView.show()

        self.web = QtWebKit.QWebView(self)
        self.pic = QtGui.QLabel("picture")

        self.web.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.projectView)
        self.layout.addWidget(self.web)
        self.layout.addWidget(self.pic)
        self.setLayout(self.layout)

        self.setMinimumHeight(700)

        self.projectView.clicked.connect(self.getData)
        self.projectView.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border:1px solid rgb(255, 170, 255);")

    def getData(self):
        index = self.projectView.selectedIndexes()[0]
        crawler = self.projectModel.itemData(index)
        dance_name = crawler[0].toString()

        db = MySQLdb.connect("localhost","root","","dancebook" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        sql = "SELECT pioneer,pioneer_name,video,about_pioneer,about_dance FROM dance WHERE name = '%s'"%(dance_name)
        cursor.execute(sql)

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()

        print data
        pic = data[0]
        video = data[2]

        img_data = urllib.urlopen(pic).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_data)
        self.pic.setPixmap(pixmap)

        self.web.setHtml(video)
        self.web.show()
        db.close()



if __name__=="__main__":
    app = Qt.QApplication(sys.argv)
    a = A()
    a.show()
    app.exec_()
