import sys
from time import sleep

from PIL import Image
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # QApplication, QMessageBox, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import *  # QMouseEvent, QKeyEvent, QPainter, QPaintEvent, QColor

# pyuic5 ImageManagerUI.ui -o UI.py
'''
поиск избражений по тегу или по имени
документация
ширина/высоты таблицы
'''


class ImageManager(QMainWindow):
    def __init__(self):
        super(ImageManager, self).__init__()

        self.setMouseTracking(True)

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)

        # values
        self.isExpandedMode = True
        self.isNameSearchMode = True
        # try:
        #     self.data = open('data.txt').readlines()
        # except FileNotFoundError:
        #     open('data.txt', mode='w')

        # layouts declaration
        self.mainLayout = QHBoxLayout(self)

        self.gridLayout = QGridLayout()
        self.table = QTableWidget(1, 4)

        self.verticalLayout = QVBoxLayout()
        self.searchLineLayout = QHBoxLayout()
        self.turnSearchModeLayout = QHBoxLayout()
        self.layoutForAdd = QHBoxLayout()

        # widgets declaration
        self.defaultImage = QLabel()
        self.systemText = QLabel('Поиск по')
        self.searchLine = QLineEdit()

        self.searchButton = QPushButton(QIcon(QPixmap('searchImage.png')), '')
        self.turnModeButton = QPushButton('—')
        self.addImageButton = QPushButton('Add image')
        self.addTagButton = QPushButton('Add tag')
        self.turnSearchModeButton = QPushButton('имени')

        self.searchResultList = QListWidget()
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

        # self.mainLayout.addLayout(self.gridLayout)
        self.mainLayout.addWidget(self.table)

        # self.mainLayout.addItem(self.mainSpacer)
        # self.mainLayout.addItem(self.mainSpacer2)
        # self.mainLayout.addItem(self.mainSpacer3)
        self.mainLayout.addLayout(self.verticalLayout)

        self.verticalLayout.addWidget(self.turnModeButton, 0, Qt.AlignRight)
        self.verticalLayout.addLayout(self.searchLineLayout)
        self.verticalLayout.addLayout(self.turnSearchModeLayout)
        self.verticalLayout.addWidget(self.searchResultList)
        self.verticalLayout.addItem(self.menuSpacer)
        self.verticalLayout.addLayout(self.layoutForAdd)

        self.layoutForAdd.addWidget(self.addImageButton, 0, Qt.AlignRight)
        self.layoutForAdd.addWidget(self.addTagButton)

        # self.gridLayout.addWidget(self.defaultImage)
        self.table.setCellWidget(0, 0, self.defaultImage)

        self.searchLineLayout.addWidget(self.searchLine)
        self.searchLineLayout.addWidget(self.searchButton)

        self.turnSearchModeLayout.addWidget(self.systemText, 0, Qt.AlignRight)
        self.turnSearchModeLayout.addWidget(self.turnSearchModeButton)

        # setting images                            _____________________
        diction = {}
        self.defaultImage.setPixmap(QPixmap('defaultImage.png'))

        # setting sizes
        self.searchResultList.hide()

        self.searchButton.setMaximumSize(QSize(24, 24))
        self.turnModeButton.setMaximumSize(QSize(24, 24))
        self.addImageButton.setFixedSize(100, 28)
        self.addTagButton.setFixedSize(100, 28)
        self.turnSearchModeButton.setFixedSize(60, 28)
        for i in range(4):
            self.table.setColumnWidth(i, 250)
        self.table.setSelectionMode(0)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.searchLine.setMaximumWidth(300)
        self.searchResultList.setMaximumWidth(400)

        # setting buttons
        self.turnModeButton.clicked.connect(self.turnMode)
        self.addImageButton.clicked.connect(self.addNewImage)
        self.addTagButton.clicked.connect(self.addNewTag)
        self.searchButton.clicked.connect(self.searchImageByTag)
        self.turnSearchModeButton.clicked.connect(self.turnSearchMode)

        self.displayImages()

        # self.addTagButton.setIcon(QIcon(QPixmap('defaultImage.png')))  # -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    def searchImageByTag(self):
        searchQuery = self.searchLine.text()

        searchResult = []
        if searchQuery:
            for i in open('data.txt', encoding='utf-8').readlines():
                i = i.lower()
                if searchQuery in i:
                    if searchQuery == i:
                        searchResult.insert(0, i)
                    searchResult.append(i)
        self.searchResultList.show()
        self.searchResultList.addItems(searchResult)

    def turnSearchMode(self):
        if self.isNameSearchMode:
            self.turnSearchModeButton.setText('тегу')
        else:
            self.turnSearchModeButton.setText('имени')
        self.isNameSearchMode = not self.isNameSearchMode

    def displayImages(self):
        lines = open('data.txt', encoding='utf-8').readlines()
        self.table.setRowCount(len(lines) // 4 + 1 * bool(len(lines) % 4))
        for j in range(len(lines) // 4 if (len(lines) % 4 == 0) else len(lines) // 4 + 1):
            # print('j', j)
            for i in range(min(len(lines), 4)):
                # print('i', i)
                lines_index = (min(j * min(len(lines), 4) + i, len(lines) - 1))
                print(j, i)

                image_button = QPushButton()
                image_button.setFixedSize(250, 200)
                image_button.setIcon(QIcon(resizeImage(getImagePath(lines[lines_index]), 250, 200)))
                image_button.setIconSize(QSize(250, 200))
                # image_button.clicked.connect(lambda: ImageEditing(lines[lines_index]))  # (lines[lines_index])
                image_button.clicked.connect(lambda: self.callImageEditing(lines[lines_index], lines_index))  # (lines[lines_index])

                self.table.setCellWidget(j, i, image_button)
        for i in range(self.table.rowCount()):
            self.table.setRowHeight(i, 200)

    def callImageEditing(self, line, index):
        global editingWindow
        editingWindow = ImageEditing(line, index)
        editingWindow.show()

    # def callImageEditing(self, sender):
    #     ImageEditing(sender)

    def turnMode(self):
        self.turnModeButton.setText('□' if self.isExpandedMode else '—')
        for i in (self.searchLine, self.addTagButton,
                  self.addImageButton, self.searchButton,
                  self.systemText, self.turnSearchModeButton):
            i.hide() if self.isExpandedMode else i.show()
        self.isExpandedMode = not self.isExpandedMode

    def addNewTag(self):
        newTag, okPressed = QInputDialog.getText(self, 'Новый тег', 'Введите новый тег')
        if okPressed:
            print(newTag, file=open('tags.txt', mode='a+t', encoding='utf-8'))

    def addNewImage(self):
        filePath = QFileDialog.getOpenFileName(self, 'Выбор изображения', '',
                                               'Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
        line = f'{filePath}:Введите имя:'
        print(line, file=open('data.txt', mode='a+t', encoding='utf-8'))

        global editingWindow
        editingWindow = ImageEditing(line)
        editingWindow.show()
        # ImageEditing(filePath)

    def mouseMoveEvent(self, e: QMouseEvent):
        # self.statusBar().showMessage(f'{e.x()}, {e.y()}')
        self.searchResultList.hide()


class ImageEditing(QWidget):
    def __init__(self, dataline, index = None):
        super(ImageEditing, self).__init__()
        self.indexInFile = index
        self.tags = []
        global qwery
        qwery = 0

        self.dataLine = dataline
        self.mainLayout = QHBoxLayout(self)
        self.verticalLayout = QVBoxLayout()
        self.enterNameLayout = QHBoxLayout()
        self.searchTagLayout = QHBoxLayout()
        self.tagsLabel = QLabel('\n'.join(getImageTagsList(self.dataLine)))
        self.enterNameLayoutText = QLabel('Имя:')
        self.searchTagLayoutText = QLabel('Тег:')
        self.selectedImage = QLabel()
        self.searchTagLine = QLineEdit()
        self.enterNameLine = QLineEdit('Введите имя')
        self.searchResultList = QListWidget()
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.addTagButton = QPushButton('Присвоить тег изображению')
        self.saveImageButton = QPushButton('Сохранить')

        self.mainLayout.addWidget(self.selectedImage)
        self.mainLayout.addLayout(self.verticalLayout)
        self.verticalLayout.addLayout(self.enterNameLayout)
        self.verticalLayout.addWidget(self.tagsLabel)
        self.verticalLayout.addLayout(self.searchTagLayout)

        self.verticalLayout.addWidget(self.searchTagLine)
        self.verticalLayout.addWidget(self.addTagButton)
        self.verticalLayout.addWidget(self.searchResultList)
        self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.saveImageButton)

        self.enterNameLayout.addWidget(self.enterNameLayoutText)
        self.enterNameLayout.addWidget(self.enterNameLine)

        self.searchTagLayout.addWidget(self.searchTagLayoutText)
        self.searchTagLayout.addWidget(self.searchTagLine)

        self.setLayout(self.mainLayout)
        # print(filePath)
        print(getImagePath(self.dataLine), 123456789)
        self.selectedImage.setPixmap(resizeImage(getImagePath(self.dataLine), 600, 400))

        self.searchTagLine.textChanged.connect(self.searchTag)
        # self.addImageButton.clicked.connect(self)
        self.addTagButton.clicked.connect(self.AddTagToImage)
        self.searchResultList.itemClicked.connect(self.ChooseTag)
        self.saveImageButton.clicked.connect(self.saveImage)
        self.enterNameLine.textChanged.connect(lambda: self.enterNameLine.clear())

        self.searchResultList.hide()

    def saveImage(self):
        with open('data.txt', encoding='utf-8', mode='r+t' if self.indexInFile else 'at') as file:
            if self.indexInFile:
                file.seek(self.indexInFile)
            print(self.tags, 123)
            file.write(f'{getImagePath(self.dataLine)}:{self.enterNameLine.text()}:{";".join(self.tags)}')
        self.close()

    def searchTag(self):
        self.searchResultList.clear()
        self.searchResultList.show()
        # search

        searchQuery = self.searchTagLine.text().lower()
        searchResult = []
        if searchQuery:
            for i in open('tags.txt', encoding='utf-8', mode='r+t').readlines():
                i = i.lower()
                if searchQuery in i:
                    if searchQuery == i:
                        searchResult.insert(0, i)
                    searchResult.append(i)
        self.searchResultList.addItems(searchResult)

        self.verticalLayout.insertWidget(1, self.searchResultList)

    def ChooseTag(self):
        self.searchTagLine.setText(self.searchResultList.item(self.searchResultList.currentRow()).text())

    def AddTagToImage(self):
        tag = self.searchTagLine.text()
        if tag in map(lambda x: x.lower(), open('tags.txt', encoding='utf-8').readlines()):
            self.tags.append(tag.rstrip('\n'))
            self.searchResultList.hide()
            self.searchTagLine.clear()
            self.searchResultList.clear()
            self.tagsLabel.setText('\n'.join(self.tags))


def resizeImage(path: str, newWidth: int, newHeight: int):
    return QPixmap(path).scaled(newWidth, newHeight)


def getImageName(line: str):
    return line.split('/')[-1].split(':')[0]


def getImagePath(line: str):
    return ':'.join(line.split(':')[0:2])


def getImageTagsList(line: str):
    return line.split(':')[-1].split(';')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageManager()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
