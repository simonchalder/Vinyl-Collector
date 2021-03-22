from dotenv import load_dotenv
from tinydb import TinyDB, Query
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QDialog, QApplication
import time

db = TinyDB('./db/db.json')
Record = Query()
cell_text = ''

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Vinyl Collector")
        self.setFixedWidth(1024)
        self.setFixedHeight(600)

        # Set layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Title label

        title_label = qtw.QLabel("Vinyl Collector")
        title_label.setFont(qtg.QFont('Helvetica', 18)) # Change font
        self.layout().addWidget(title_label)

        # Stock Code Entry Box

        rec_artist = qtw.QLineEdit()
        self.layout().addWidget(rec_artist)
        
        rec_title = qtw.QLineEdit()
        self.layout().addWidget(rec_title)

        rec_label = qtw.QLineEdit()
        self.layout().addWidget(rec_label)

        rec_cat_num = qtw.QLineEdit()
        self.layout().addWidget(rec_cat_num)

        rec_genre = qtw.QLineEdit()
        self.layout().addWidget(rec_genre)

        rec_format = qtw.QComboBox()
        rec_format.addItem("LP")
        rec_format.addItem("Double Album")
        rec_format.addItem("Single")
        self.layout().addWidget(rec_format)

        rec_country = qtw.QLineEdit()
        self.layout().addWidget(rec_country)

        rec_year = qtw.QLineEdit()
        self.layout().addWidget(rec_year)

        # Submit Button

        submitButton = qtw.QPushButton("Submit", clicked = lambda: submitButtonClick())
        self.layout().addWidget(submitButton)

        refreshButton = qtw.QPushButton("Refresh", clicked = lambda: showCollection())
        self.layout().addWidget(refreshButton)

        deleteButton = qtw.QPushButton("Delete Selected", clicked = lambda: delRecord())
        self.layout().addWidget(deleteButton)

        collection_table = qtw.QTableWidget(self)
        collection_table.setColumnCount(8)
        collection_table.setRowCount(len(db.all())+2)
        collection_table.setColumnWidth(0, 200)
        collection_table.setColumnWidth(1, 200)
        collection_table.setColumnWidth(2, 120)
        collection_table.setColumnWidth(3, 100)
        collection_table.setColumnWidth(4, 100)
        collection_table.setColumnWidth(5, 100)
        collection_table.setColumnWidth(6, 100)
        collection_table.setColumnWidth(7, 100)
        self.layout().addWidget(collection_table)        

        # Row Allocation

        form_layout.addRow("Artist: ", rec_artist)
        form_layout.addRow("Title: ", rec_title)
        form_layout.addRow("Label: ", rec_label)
        form_layout.addRow("Cat No: ", rec_cat_num)
        form_layout.addRow("Genre: ", rec_genre)
        form_layout.addRow("Format: ", rec_format)
        form_layout.addRow("Country: ", rec_country)
        form_layout.addRow("Year: ", rec_year)
        form_layout.addRow(submitButton)
        form_layout.addRow(refreshButton)
        form_layout.addRow(collection_table)
        form_layout.addRow(deleteButton)
        
        self.show()
        
        # Define functions after show()

        def submitButtonClick():
            newRecord = {}
            newRecord["Artist"] = rec_artist.text()
            newRecord["Title"] = rec_title.text()
            newRecord["Label"] = rec_label.text()
            newRecord["Catalogue_No"] = rec_cat_num.text()
            newRecord["Genre"] = rec_genre.text()
            newRecord["Format"] = rec_format.currentText()
            newRecord["Country"] = rec_country.text()
            newRecord["Year"] = rec_year.text()
            db.insert(newRecord)
            collection_table.setRowCount(len(db.all()))
            showCollection()
            rec_artist.setText('')
            rec_title.setText('')
            rec_label.setText('')
            rec_cat_num.setText('')
            rec_genre.setText('')
            rec_country.setText('')
            rec_year.setText('')
        
        def showCollection():
            tablerow = 0
            results = db.all()
            for item in results:
                line = list(item.values())
                collection_table.setItem(tablerow, 0, qtw.QTableWidgetItem(line[0]))
                collection_table.setItem(tablerow, 1, qtw.QTableWidgetItem(line[1]))
                collection_table.setItem(tablerow, 2, qtw.QTableWidgetItem(line[2]))
                collection_table.setItem(tablerow, 3, qtw.QTableWidgetItem(line[3]))
                collection_table.setItem(tablerow, 4, qtw.QTableWidgetItem(line[4]))
                collection_table.setItem(tablerow, 5, qtw.QTableWidgetItem(line[5]))
                collection_table.setItem(tablerow, 6, qtw.QTableWidgetItem(line[6]))
                collection_table.setItem(tablerow, 7, qtw.QTableWidgetItem(line[7]))
                tablerow+=1

        def clickCell(row, column):
            row = row
            column = column
            global cell_type
            cell_type = column
            cell = collection_table.item(row, column)
            global cell_text
            cell_text = cell.text()
            return cell_text
        
        def delRecord():
            global cell_text
            global cell_type
            if cell_type == 0:
                db.remove(Record.Artist == cell_text)
                
            elif cell_type == 1:
                db.remove(Record.Title == cell_text)

            elif cell_type == 2:
                db.remove(Record.Label == cell_text)

            elif cell_type == 3:
                db.remove(Record.Catalogue_No == cell_text)

            elif cell_type == 4:
                db.remove(Record.Genre == cell_text)

            elif cell_type == 5:
                db.remove(Record.Format == cell_text)

            elif cell_type == 6:
                db.remove(Record.Country == cell_text)

            else:
                db.remove(Record.Format == cell_text)

            collection_table.clearContents()
            collection_table.setRowCount(len(db.all()))
            showCollection()
        
        showCollection()
        collection_table.cellClicked.connect(clickCell)

app = qtw.QApplication([])

mw = MainWindow()

app.exec_()