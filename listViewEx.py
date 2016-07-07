from PyQt4 import Qt,QtGui
import sys

# Create a Qt application
app = Qt.QApplication(sys.argv)

# Our main window will be a QListView
list = QtGui.QListView()
list.setWindowTitle('Example List')
list.setMinimumSize(600, 400)

# Create an empty model for the list's data
model = QtGui.QStandardItemModel(list)

# Add some textual items
foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]

for food in foods:
    # create an item with a caption
    item = QtGui.QStandardItem(food)

    # add a checkbox to it
    item.setCheckable(True)

    # Add the item to the model
    model.appendRow(item)

# Apply the model to the list view
list.setModel(model)

# Show the window and run the app
list.show()
app.exec_()