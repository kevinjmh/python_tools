import sys

import SQLhelper
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow


class MainWindows(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.ui = SQLhelper.Ui_MainWindow()
        self.ui.setupUi(self)

    def genSQL(self):
        print(self.ui.tabWidget.currentIndex())

        phoneNum = self.ui.lineEdit.text()

        out = "phoneNum=" + phoneNum
        self.ui.textBrowser.setText(out)

        import clipboard
        clipboard.copy(out)  # now the clipboard content will be string "abc"
        text = clipboard.paste()  # text will have the content of clipboard
        print(text)





if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainWindows()
    myDlg.show()
    sys.exit(myapp.exec())
