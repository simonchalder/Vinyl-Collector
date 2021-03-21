from dotenv import load_dotenv
from tinydb import TinyDB, Query
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

db = TinyDB('./db/db.json')

Record = Query()

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Vinyl Collector")

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

        collection_text = qtw.QTextBrowser(self)
        self.layout().addWidget(collection_text)


        # Row Allocation

        form_layout.addRow("Artist: ", rec_artist)
        form_layout.addRow("Title: ", rec_title)
        form_layout.addRow("Cat No: ", rec_cat_num)
        form_layout.addRow("Label: ", rec_label)
        form_layout.addRow("Genre: ", rec_genre)
        form_layout.addRow("Format: ", rec_format)
        form_layout.addRow("Country: ", rec_country)
        form_layout.addRow("Year: ", rec_year)
        form_layout.addRow(submitButton)
        form_layout.addRow(collection_text)

        self.show()

        # Define functions after show()

        def submitButtonClick():
            newRecord = {}
            newRecord["Artist"] = rec_artist.text()
            newRecord["Title"] = rec_title.text()
            newRecord["Label"] = rec_label.text()
            newRecord["Catalogue No."] = rec_cat_num.text()
            newRecord["Genre"] = rec_artist.text()
            newRecord["Format"] = rec_format.currentText()
            newRecord["Country"] = rec_country.text()
            newRecord["Year"] = rec_year.text()
            db.insert(newRecord)
            showCollection()
        
        def showCollection():
            
            for item in db:
                collection_text.append(str(item))

app = qtw.QApplication([])

mw = MainWindow()

app.exec_()