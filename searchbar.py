import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

model = QtGui.QStringListModel()
model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])

completer = QtGui.QCompleter()
completer.setModel(model)

lineedit = QtGui.QLineEdit()
lineedit.setCompleter(completer)
lineedit.show()

sys.exit(app.exec_())