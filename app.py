# Imports

from dotenv import load_dotenv
from tinydb import TinyDB, Query
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg


# Globals 
db = TinyDB('./db/db.json')
Record = Query()
cell_text = ''

# Class Definition

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # Main window title and dimensions

        self.setWindowTitle("Vinyl Collector")
        self.setFixedWidth(1050)
        self.setFixedHeight(600)

        # Set layout
        form_layout = qtw.QGridLayout()
        self.setLayout(form_layout)

        # Label style variables
        label_font = 'Helvetica'
        label_size = 12

        # Widget creation -----------------------------------------------------------------------------------

        # Artist Label
        artist_label = qtw.QLabel("Artist")
        artist_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(artist_label)

        #Artist input box
        rec_artist = qtw.QLineEdit()
        self.layout().addWidget(rec_artist)

        # Title Label
        title_label = qtw.QLabel("Title")
        title_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(title_label)
        
        # Title input box
        rec_title = qtw.QLineEdit()
        self.layout().addWidget(rec_title)

        # Label label!
        label_label = qtw.QLabel("Label")
        label_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(label_label)

        # Label input box
        rec_label = qtw.QLineEdit()
        self.layout().addWidget(rec_label)

        # Catno label
        catno_label = qtw.QLabel("Catalogue Number")
        catno_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(catno_label)

        # Catno input box
        rec_cat_num = qtw.QLineEdit()
        self.layout().addWidget(rec_cat_num)

        #Genre label
        genre_label = qtw.QLabel("Genre")
        genre_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(genre_label)

        #Genre input box
        rec_genre = qtw.QLineEdit()
        self.layout().addWidget(rec_genre)

        #Format label
        format_label = qtw.QLabel("Format")
        format_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(format_label)

        #Format combobox
        rec_format = qtw.QComboBox()
        rec_format.addItem("LP")
        rec_format.addItem("Double Album")
        rec_format.addItem("Single")
        self.layout().addWidget(rec_format)

        # Country label
        country_label = qtw.QLabel("Country")
        country_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(country_label)

        # Country input box
        rec_country = qtw.QLineEdit()
        self.layout().addWidget(rec_country)

        #Year label
        year_label = qtw.QLabel("Year")
        year_label.setFont(qtg.QFont(label_font, label_size))
        self.layout().addWidget(year_label)

        # Year input box
        rec_year = qtw.QLineEdit()
        self.layout().addWidget(rec_year)

        # Submit Button

        submitButton = qtw.QPushButton("Submit", clicked = lambda: submitButtonClick())
        self.layout().addWidget(submitButton)

        # Refresh Button
        
        refreshButton = qtw.QPushButton("Refresh", clicked = lambda: showCollection())
        self.layout().addWidget(refreshButton)

        # Delete Button
        
        deleteButton = qtw.QPushButton("Delete Selected", clicked = lambda: delRecord())
        self.layout().addWidget(deleteButton)

        # Edit Button
        
        editButton = qtw.QPushButton("Edit Selected", clicked = lambda: editRecord())
        self.layout().addWidget(editButton)

        # Table creation, header labels and row widths

        collection_table = qtw.QTableWidget(self)
        collection_table.setColumnCount(8)
        collection_table.setRowCount(len(db.all())+1)
        collection_table.setHorizontalHeaderLabels(["Artist", "Title", "Label", "Cat No.", "Genre", "Format", "Country", "Year"])
        collection_table.setColumnWidth(0, 200)
        collection_table.setColumnWidth(1, 200)
        collection_table.setColumnWidth(2, 120)
        collection_table.setColumnWidth(3, 100)
        collection_table.setColumnWidth(4, 100)
        collection_table.setColumnWidth(5, 100)
        collection_table.setColumnWidth(6, 100)
        collection_table.setColumnWidth(7, 80)
        self.layout().addWidget(collection_table)        

        # Table Row & Column Allocations

        form_layout.addWidget(artist_label, 0, 0)
        form_layout.addWidget(title_label, 0, 1)
        form_layout.addWidget(rec_artist, 1, 0)
        form_layout.addWidget(rec_title, 1, 1)
        form_layout.addWidget(label_label, 2, 0)
        form_layout.addWidget(catno_label, 2, 1)
        form_layout.addWidget(rec_label, 3, 0)
        form_layout.addWidget(rec_cat_num, 3, 1)
        form_layout.addWidget(genre_label, 4, 0)
        form_layout.addWidget(format_label, 4, 1)
        form_layout.addWidget(rec_genre, 5, 0)
        form_layout.addWidget(rec_format, 5, 1)
        form_layout.addWidget(country_label, 6, 0)
        form_layout.addWidget(year_label, 6, 1)
        form_layout.addWidget(rec_country, 7, 0)
        form_layout.addWidget(rec_year, 7, 1)
        form_layout.addWidget(editButton, 8, 0)
        form_layout.addWidget(submitButton, 8, 1)
        form_layout.addWidget(refreshButton, 10, 0)
        form_layout.addWidget(collection_table, 9, 0, 1, 2)
        form_layout.addWidget(deleteButton, 10, 1)
        
        self.show()
        
        # Define functions after show()

        def submitButtonClick(): # Function called when submit button clicked
            newRecord = {} # Create new empty dictionary 'newRecord'
            newRecord["Artist"] = rec_artist.text() # Take text from input boxes and store in dictionary
            newRecord["Title"] = rec_title.text()
            newRecord["Label"] = rec_label.text()
            newRecord["Catalogue_No"] = rec_cat_num.text()
            newRecord["Genre"] = rec_genre.text()
            newRecord["Format"] = rec_format.currentText()
            newRecord["Country"] = rec_country.text()
            newRecord["Year"] = rec_year.text()
            db.insert(newRecord) # Add the contents of the newRecord object to the database
            collection_table.setRowCount(len(db.all())) # Set number of table rows equal to the number of records in the database
            showCollection() # Call the showCollection function
            rec_artist.setText('') # Clear text from input boxes
            rec_title.setText('')
            rec_label.setText('')
            rec_cat_num.setText('')
            rec_genre.setText('')
            rec_country.setText('')
            rec_year.setText('')
        
        def showCollection(): # Functiona called when refresh button is clicked or called elsewhere
            tablerow = 0 # Create table row number to iterate through table
            results = db.all() # create 'results' object containing all database entries
            for item in results:
                line = list(item.values()) # Iterate through table inserting database records into table
                collection_table.setItem(tablerow, 0, qtw.QTableWidgetItem(line[0]))
                collection_table.setItem(tablerow, 1, qtw.QTableWidgetItem(line[1]))
                collection_table.setItem(tablerow, 2, qtw.QTableWidgetItem(line[2]))
                collection_table.setItem(tablerow, 3, qtw.QTableWidgetItem(line[3]))
                collection_table.setItem(tablerow, 4, qtw.QTableWidgetItem(line[4]))
                collection_table.setItem(tablerow, 5, qtw.QTableWidgetItem(line[5]))
                collection_table.setItem(tablerow, 6, qtw.QTableWidgetItem(line[6]))
                collection_table.setItem(tablerow, 7, qtw.QTableWidgetItem(line[7]))
                tablerow+=1

        def clickCell(row, column): # Function called by signal when the mouse is clicked on a table cell. Identifies which cell was clicked and the text in that cell
            row = row
            column = column
            global cell_type
            cell_type = column
            cell = collection_table.item(row, column)
            global cell_text
            cell_text = cell.text()
            return cell_text
        
        def delRecord(): # Function called when the delete button is clicked
            global cell_text # Takes variables from the clickCell function, identifies which column was clicked on, then removes the corresponding database entry
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
                db.remove(Record.Year == cell_text)

            collection_table.clearContents() # Clear table before reloading database - seems to help table refresh
            collection_table.setRowCount(len(db.all()))
            showCollection()

        def editRecord(): # Function called when edit button is clicked. Uses clickCell function data to identify cell as with delRrecord but then populates entry boxes with database entry
            global cell_text
            global cell_type
            if cell_type == 0:
                search = db.search(Record.Artist == cell_text)
                
            elif cell_type == 1:
                search = db.search(Record.Title == cell_text)

            elif cell_type == 2:
                search = db.search(Record.Label == cell_text)

            elif cell_type == 3:
                search = db.search(Record.Catalogue_No == cell_text)

            elif cell_type == 4:
                search = db.search(Record.Genre == cell_text)

            elif cell_type == 5:
                search = db.search(Record.Format == cell_text)

            elif cell_type == 6:
                search = db.search(Record.Country == cell_text)

            else:
                search = db.search(Record.Year == cell_text)
            
            rec_artist.setText(search[0]["Artist"])
            rec_title.setText(search[0]["Title"])
            rec_label.setText(search[0]["Label"])
            rec_cat_num.setText(search[0]["Catalogue_No"]) 
            rec_genre.setText(search[0]["Genre"])  
            rec_country.setText(search[0]["Country"])
            rec_year.setText(search[0]["Year"])

            db.remove(Record.Title == search[0]['Title']) # Deletes database entry after inputs are populated but does not refresh table until new record is submitted


# Functin call to populate table on app startup
        showCollection()

# Signal creation for clickCell function
        collection_table.cellClicked.connect(clickCell)

# QApplication creation
app = qtw.QApplication([])

# Set style
app.setStyle('Oxygen')

mw = MainWindow()

app.exec_()