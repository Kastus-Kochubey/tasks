import sys
from time import sleep

from PIL import Image
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # QApplication, QMessageBox, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import *  # QMouseEvent, QKeyEvent, QPainter, QPaintEvent, QColor

# pyuic5 ImageManagerUI.ui -o UI.py
'''новое окно выбора даты в setSearchDateTimeLayout
buttons
добавление новых изображений
распределение изображений на gridLayout

добавение новых тегов, их присваивание к изображению
'''


# class ImageManager(QWidget):
class ImageManager(QMainWindow):
    def __init__(self):
        super(ImageManager, self).__init__()

        self.setMouseTracking(True)

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)

        # values
        self.isExpandedMode = True
        self.data = open('data.txt').readlines()

        # layouts declaration
        self.mainLayout = QHBoxLayout(self)

        self.gridLayout = QGridLayout()
        self.verticalLayout = QVBoxLayout()
        self.searchLineLayout = QHBoxLayout()
        self.searchPeriodDateTimeLayout = QHBoxLayout()
        self.setSearchDateTimeLayout = QHBoxLayout()
        self.layoutForAdd = QHBoxLayout()

        # widgets declaration
        self.defaultImage = QLabel()
        self.searchImage = QLabel()
        self.systemText = QLabel('Поиск по времени')
        self.searchLine = QLineEdit()

        self.buttonBefore = QPushButton('До')
        self.buttonAfter = QPushButton('После')
        self.buttonPeriod = QPushButton('В период')
        self.turnModeButton = QPushButton('—')
        self.addImageButton = QPushButton('Add image')
        self.addTagButton = QPushButton('Add tag')
        self.dateSelectionWindowButton = QPushButton('Выбрать')

        self.searchDateTime = QDateTimeEdit(QDateTime.currentDateTime())
        self.searchResultList = QListView()
        self.menuSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.mainSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mainSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.mainSpacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # distribution
        '''self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)         # -------------------------------------
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.defaultImage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.searchResultList.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)'''

        self.mainWidget.setLayout(self.mainLayout)

        self.mainLayout.addLayout(self.gridLayout)
        self.mainLayout.addItem(self.mainSpacer)
        self.mainLayout.addItem(self.mainSpacer2)
        self.mainLayout.addItem(self.mainSpacer3)
        self.mainLayout.addLayout(self.verticalLayout)

        self.verticalLayout.addWidget(self.turnModeButton, 0, Qt.AlignRight)
        self.verticalLayout.addLayout(self.searchLineLayout)
        self.verticalLayout.addLayout(self.searchPeriodDateTimeLayout)
        self.verticalLayout.addLayout(self.setSearchDateTimeLayout)
        self.verticalLayout.addWidget(self.searchResultList)
        self.verticalLayout.addItem(self.menuSpacer)
        self.verticalLayout.addLayout(self.layoutForAdd)

        self.layoutForAdd.addWidget(self.addImageButton, 0, Qt.AlignRight)
        self.layoutForAdd.addWidget(self.addTagButton)

        self.gridLayout.addWidget(self.defaultImage)

        self.setSearchDateTimeLayout.addWidget(self.searchDateTime)
        self.setSearchDateTimeLayout.addWidget(self.dateSelectionWindowButton, 0, Qt.AlignLeft)

        self.searchLineLayout.addWidget(self.searchLine)
        self.searchLineLayout.addWidget(self.searchImage)

        self.searchPeriodDateTimeLayout.addWidget(self.systemText)
        self.searchPeriodDateTimeLayout.addWidget(self.buttonBefore)
        self.searchPeriodDateTimeLayout.addWidget(self.buttonAfter)
        self.searchPeriodDateTimeLayout.addWidget(self.buttonPeriod)

        # setting images                            _____________________
        diction = {}
        self.searchImage.setPixmap(QPixmap('searchImage.png'))
        self.defaultImage.setPixmap(QPixmap('defaultImage.png'))

        # setting sizes
        self.searchResultList.hide()

        self.turnModeButton.setMaximumSize(QSize(24, 24))
        self.addImageButton.setFixedSize(100, 28)
        self.addTagButton.setFixedSize(100, 28)
        self.dateSelectionWindowButton.setMaximumWidth(70)
        self.searchDateTime.setMaximumWidth(125)
        for i in (self.buttonPeriod, self.buttonAfter, self.buttonBefore):
            i.setMaximumWidth(80)
        self.searchLine.setMaximumWidth(300)
        self.searchResultList.setMaximumWidth(400)
        # self.searchDateTime.setMaximumWidth(200)
        # self.searchLine.setMaximumSize(QSize(300, 50))
        # self.searchResultList.setMaximumWidth(300)
        # self.searchDateTime.setMaximumWidth(300)
        # self.buttonBefore.setMaximumWidth(40)
        #
        # self.verticalLayout.setSizeConstraint(QLayout.sizeConstraint())

        # setting buttons
        self.turnModeButton.clicked.connect(self.turnMode)
        self.addImageButton.clicked.connect(self.addNewImage)
        # self.buttonBefore.clicked.connect()
        # self.buttonAfter.clicked.connect()
        # self.buttonPeriod.clicked.connect()

        self.addNewImage()

    def turnMode(self):
        self.turnModeButton.setText('□' if self.isExpandedMode else '—')
        for i in (self.searchLine, self.buttonAfter,
                  self.buttonBefore, self.buttonPeriod,
                  self.searchImage, self.systemText,
                  self.searchDateTime, self.dateSelectionWindowButton):
            i.hide() if self.isExpandedMode else i.show()
        self.isExpandedMode = not self.isExpandedMode

    def addNewTag(self):
        newTag, okPressed = QInputDialog.getText(self, 'Добавление нового тега', 'Введите название тега')

    def addNewImage(self):
        # image = Image.open(filePath)
        filePath = QFileDialog.getOpenFileName(self, 'Выбор изображения', '',
                                               'Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
        # Image.open(filePath).save(f'{filePath.split(".")[0].split("/")[-1]}.png')
        global exe
        exe = AddNewImageDialog(filePath)
        exe.show()

    def mouseMoveEvent(self, e: QMouseEvent):
        # self.statusBar().showMessage(f'{e.x()}, {e.y()}')
        self.statusBar().showMessage(str(self.searchResultList.size()))


class AddNewImageDialog(QWidget):
    def __init__(self, filePath):
        super(AddNewImageDialog, self).__init__()
        self.filePath = filePath
        self.mainLayout = QHBoxLayout(self)
        self.verticalLayout = QVBoxLayout()
        self.selectedImage = QLabel()
        self.searchTagLine = QLineEdit()
        self.searchResultList = QListWidget()
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.addTagButton = QPushButton('Присвоить тег изображению')

        self.mainLayout.addWidget(self.selectedImage)
        self.mainLayout.addLayout(self.verticalLayout)
        self.verticalLayout.addWidget(self.searchTagLine)
        self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.addTagButton)

        self.setLayout(self.mainLayout)
        self.selectedImage.setPixmap(resizeImage(filePath, 500, 300))

        self.searchTagLine.textChanged.connect(self.searchTag)

    def searchTag(self):
        self.searchResultList.clear()
        # search
        self.verticalLayout.insertWidget(1, self.searchResultList)
        self.searchResultList.addItem('123456789')

def resizeImage(path: str, newWidth: int, newHeight: int):
    return QPixmap(path).scaled(newWidth, newHeight)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageManager()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

'''self.horizontalLayout = QHBoxLayout(self)
           self.horizontalLayout.setObjectName("horizontalLayout")
           self.gridLayout = QGridLayout()
           self.gridLayout.setObjectName("gridLayout")
           self.defaultImage = QLabel(self)
           self.defaultImage.setText("")
           self.defaultImage.setObjectName("defaultImage")
           self.gridLayout.addWidget(self.defaultImage, 0, 0, 1, 1)
           self.horizontalLayout.addLayout(self.gridLayout)
           self.verticalLayout = QVBoxLayout()
           self.verticalLayout.setObjectName("verticalLayout")
           self.turnModeButton = QPushButton(self)
           sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
           sizePolicy.setHorizontalStretch(0)
           sizePolicy.setVerticalStretch(0)
           sizePolicy.setHeightForWidth(self.turnModeButton.sizePolicy().hasHeightForWidth())
           self.turnModeButton.setSizePolicy(sizePolicy)
           self.turnModeButton.setMaximumSize(QSize(28, 28))
           self.turnModeButton.setObjectName("turnModeButton")
           self.verticalLayout.addWidget(self.turnModeButton, 0, Qt.AlignRight)
           self.horizontalLayout_2 = QHBoxLayout()
           self.horizontalLayout_2.setObjectName("horizontalLayout_2")
           self.searchLine = QLineEdit(self)
           sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
           sizePolicy.setHorizontalStretch(0)
           sizePolicy.setVerticalStretch(0)
           sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
           self.searchLine.setSizePolicy(sizePolicy)
           self.searchLine.setObjectName("searchLine")
           self.horizontalLayout_2.addWidget(self.searchLine)
           self.searchImage = QLabel(self)
           sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
           sizePolicy.setHorizontalStretch(0)
           sizePolicy.setVerticalStretch(0)
           sizePolicy.setHeightForWidth(self.searchImage.sizePolicy().hasHeightForWidth())
           self.searchImage.setSizePolicy(sizePolicy)
           self.searchImage.setMinimumSize(QSize(24, 24))
           self.searchImage.setText("")
           self.searchImage.setObjectName("searchImage")
           self.horizontalLayout_2.addWidget(self.searchImage)
           self.verticalLayout.addLayout(self.horizontalLayout_2)
           self.horizontalLayout_3 = QHBoxLayout()
           self.horizontalLayout_3.setObjectName("horizontalLayout_3")
           self.systemText = QLabel(self)
           sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
           sizePolicy.setHorizontalStretch(0)
           sizePolicy.setVerticalStretch(0)
           sizePolicy.setHeightForWidth(self.systemText.sizePolicy().hasHeightForWidth())
           self.systemText.setSizePolicy(sizePolicy)
           self.systemText.setObjectName("systemText")
           self.horizontalLayout_3.addWidget(self.systemText)
           self.buttonBefore = QPushButton(self)
           self.buttonBefore.setObjectName("buttonBefore")
           self.horizontalLayout_3.addWidget(self.buttonBefore)
           self.buttonAfter = QPushButton(self)
           self.buttonAfter.setObjectName("buttonAfter")
           self.horizontalLayout_3.addWidget(self.buttonAfter)
           self.buttonPeriod = QPushButton(self)
           self.buttonPeriod.setObjectName("buttonPeriod")
           self.horizontalLayout_3.addWidget(self.buttonPeriod)
           self.verticalLayout.addLayout(self.horizontalLayout_3)
           self.dateTime = QDateTimeEdit(self)
           self.dateTime.setObjectName("dateTime")
           self.verticalLayout.addWidget(self.dateTime)
           self.searchResultList = QListView(self)
           sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
           sizePolicy.setHorizontalStretch(0)
           sizePolicy.setVerticalStretch(0)
           sizePolicy.setHeightForWidth(self.searchResultList.sizePolicy().hasHeightForWidth())
           self.searchResultList.setSizePolicy(sizePolicy)
           self.searchResultList.setMaximumSize(QSize(16777215, 150))
           self.searchResultList.setObjectName("searchResultList")
           self.verticalLayout.addWidget(self.searchResultList)
           spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
           self.verticalLayout.addItem(spacerItem)
           self.horizontalLayout.addLayout(self.verticalLayout)
           # MainWindow.setCentralWidget(self)
           # self.menubar = QMenuBar(MainWindow)
           # self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 26))
           # self.menubar.setObjectName("menubar")
           # MainWindow.setMenuBar(self.menubar)
           # self.statusbar = QStatusBar(MainWindow)
           # self.statusbar.setObjectName("statusbar")
           # MainWindow.setStatusBar(self.statusbar)'''
