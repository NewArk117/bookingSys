from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QComboBox, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget()
        self.list_widget.addItem("Item 1")
        self.list_widget.addItem("Item 2")

        combo_box = QComboBox()
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")
        combo_box.setCurrentIndex(1)

        item_widget = QWidget()
        item_layout = QHBoxLayout()
        self.label1 = QLabel("Item 3")
        item_layout.addWidget(self.label1)
        item_layout.addWidget(combo_box)
        item_widget.setLayout(item_layout)
        
        #item.setData(self.label1)

        item = QListWidgetItem()
        item.setSizeHint(item_widget.sizeHint())
        self.list_widget.addItem(item)
        self.list_widget.setItemWidget(item, item_widget)

        layout = QVBoxLayout()
        self.pushbutton = QPushButton("Push me")
        layout.addWidget(self.list_widget)
        layout.addWidget(self.pushbutton)

        self.pushbutton.clicked.connect(self.pushMe)
        self.setLayout(layout)

    def pushMe(self):
        current_row = self.list_widget.currentRow()
        if current_row:
            if current_row >= 0:
                item = self.list_widget.item(current_row)
                item_widget = self.list_widget.itemWidget(item)
                label = item_widget.findChild(QLabel).text()
                combo_box = item_widget.findChild(QComboBox)
                combo_box_value = combo_box.currentText()
                print(f"Selected option for item {current_row}: {combo_box_value}")
                print(f"Label for item {current_row}: {label}")
        else:
            print("No rows selected")

        message = f'Movie name:  ?\n' 
        date = f"Date is bal"
        text = message + date
        print(text)




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
