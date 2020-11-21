import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  # QApplication, QMessageBox, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import *  # QMouseEvent, QKeyEvent, QPainter, QPaintEvent, QColor

'''
документация
'''

global imagesInLine
imagesInLine = 5
class ImageManager(QMainWindow):
    """"""

    def __init__(self):

        """Инициализация:\n
                создание и настройка интерфейса"""
        super(ImageManager, self).__init__()
        try:
            with open('data.txt') as check:
                pass

            with open('tags.txt') as check:
                pass
        except FileNotFoundError:
            with open('data.txt', mode='w') as check:
                pass

            with open('tags.txt', mode='w') as check:
                pass

        self.setWindowTitle('Менеджер изображений')
        self.setMouseTracking(True)

        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)

        # values
        self.isExpandedMode = True
        self.isNameSearchMode = True
        self.imageButtonsDict = {}

        # layouts declaration
        self.mainLayout = QHBoxLayout(self)

        self.gridLayout = QGridLayout()
        self.table = QTableWidget()

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
        self.mainWidget.setLayout(self.mainLayout)

        self.mainLayout.addWidget(self.table)
        self.mainLayout.addItem(self.mainSpacer)

        self.mainLayout.addLayout(self.verticalLayout)

        self.verticalLayout.addWidget(self.turnModeButton, 0, Qt.AlignRight)
        self.verticalLayout.addLayout(self.searchLineLayout)
        self.verticalLayout.addLayout(self.turnSearchModeLayout)
        self.verticalLayout.addWidget(self.searchResultList)
        self.verticalLayout.addItem(self.menuSpacer)
        self.verticalLayout.addLayout(self.layoutForAdd)

        self.layoutForAdd.addWidget(self.addImageButton, 0, Qt.AlignRight)
        self.layoutForAdd.addWidget(self.addTagButton)

        # self.table.setCellWidget(0, 0, self.defaultImage)

        self.searchLineLayout.addWidget(self.searchLine)
        self.searchLineLayout.addWidget(self.searchButton)

        self.turnSearchModeLayout.addWidget(self.systemText, 0, Qt.AlignRight)
        self.turnSearchModeLayout.addWidget(self.turnSearchModeButton)

        # setting images                            _____________________
        # diction = {}
        # self.defaultImage.setPixmap(QPixmap('defaultImage.png'))

        # setting sizes
        # self.setMaximumHeight(1000)
        self.searchResultList.hide()

        self.searchButton.setMaximumSize(QSize(24, 24))
        self.turnModeButton.setMaximumSize(QSize(24, 24))
        self.addImageButton.setFixedSize(100, 28)
        self.addTagButton.setFixedSize(100, 28)
        self.turnSearchModeButton.setFixedSize(60, 28)
        self.table.setColumnCount(imagesInLine)
        for i in range(5):
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
        self.searchButton.clicked.connect(self.findImage)
        self.turnSearchModeButton.clicked.connect(self.turnSearchMode)
        self.searchResultList.itemClicked.connect(lambda: self.callImageEditing())

        self.displayImages()

    def findImage(self):
        """Поиск изображений по имени или тегу"""
        self.searchResultList.clear()
        print(self.searchLine.text())
        search_query = self.searchLine.text().lower()

        search_result = []
        if search_query:
            for i in open('data.txt', encoding='utf-8').readlines():
                if self.isNameSearchMode:
                    name = getImageName(i).lower()
                    if search_query in name:
                        if search_query == name:
                            search_result.insert(0, getImageName(i))
                        search_result.append(getImageName(i))
                else:
                    for ind, tag in enumerate(map(lambda x: x.lower(), getImageTagsList(i))):
                        if search_query in tag:
                            if search_query == tag:
                                search_result.insert(0, tag)
                            else:
                                search_result.append(getImageTagsList(i)[ind])

        self.searchResultList.show()
        self.searchResultList.addItems(search_result)

    def turnSearchMode(self):
        """Переключение режима поиска изображения\n
                по имени <-> по тегу"""
        if self.isNameSearchMode:
            self.turnSearchModeButton.setText('тегу')
        else:
            self.turnSearchModeButton.setText('имени')
        self.isNameSearchMode = not self.isNameSearchMode

    def displayImages(self):
        """Отображение сохраненных изображений"""

        # def columnsCount():
        #     return min(len(lines), 4)

        lines = open('data.txt', encoding='utf-8').readlines()

        columnsCount = min(len(lines), imagesInLine)
        self.table.setColumnCount(imagesInLine)
        # columnsCount = columnsCount()
        rowsCount = len(lines) // imagesInLine if (len(lines) % imagesInLine == 0) else len(lines) // imagesInLine + 1
        self.table = QTableWidget(rowsCount, columnsCount)
        for row in range(rowsCount):
            for column in range(columnsCount):
                # lines_index = min(row * min(len(lines), 4) + column, len(lines) - 1)
                lines_index = row * min(len(lines), imagesInLine) + column
                if lines_index > min(row * min(len(lines), imagesInLine) + column, len(lines) - 1):
                    break
                # if row > self.table.rowCount():
                #     self.table.setRowCount(self.table.rowCount() + 1)
                image_button = QPushButton()
                image_button.setFixedSize(250, 200)


                # print(row, column, self.imageButtonsDict[image_button])
                image_button.setIcon(QIcon(resizeImage(getImagePath(lines[lines_index]), 250, 200)))
                image_button.setIconSize(QSize(250, 200))
                image_button.clicked.connect(self.callImageEditing)

                self.table.setCellWidget(row, column, image_button)
                self.imageButtonsDict.setdefault(image_button, [lines[lines_index], lines_index])
                # image_button.clicked.connect(lambda: self.callImageEditing(lines[lines_index], lines_index))
                # if self.table.cellWidget(row, column) == None:
                #     self.table.setCellWidget(row, column, image_button)
                print(self.table.cellWidget(row, column))


        for i in range(self.table.rowCount()):
            self.table.setRowHeight(i, 200)
        self.table.setColumnCount(5)
        self.table.setFixedSize(columnsCount * 250 + 2, rowsCount * 200)
        # print(*self.imageButtonsDict.items(), sep='\n')


    def callImageEditing(self):
        sender = QApplication.instance().sender()
        # print(self.imageButtonsDict[sender])
        global editingWindow
        editingWindow = ImageEditing(*self.imageButtonsDict[sender])
        editingWindow.show()

    def turnMode(self):
        """Сворачивание/разворачивание меню"""
        self.turnModeButton.setText('□' if self.isExpandedMode else '—')
        for i in (self.searchLine, self.addTagButton,
                  self.addImageButton, self.searchButton,
                  self.systemText, self.turnSearchModeButton):
            i.hide() if self.isExpandedMode else i.show()
        self.isExpandedMode = not self.isExpandedMode

    def addNewTag(self):
        """Добавление нового тега"""
        newTag, okPressed = QInputDialog.getText(self, 'Новый тег', 'Введите новый тег')
        if okPressed:
            print(newTag, file=open('tags.txt', mode='a+t', encoding='utf-8'))

    def addNewImage(self):
        """Вызов редактирования нового изборажения"""
        # filePath = QFileDialog.getOpenFileName(self, 'Выбор изображения', '',
        #                                        'Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
        filePath = QFileDialog.getOpenFileName(self, 'Выбор изображения', '*.png;;*.jpg')[0]
        if filePath:
            line = f'{filePath}:Введите имя:'
            global editingWindow
            editingWindow = ImageEditing(line)
            editingWindow.show()

    # def mouseMoveEvent(self, e: QMouseEvent):
    #     # self.statusBar().showMessage(f'{e.x()}, {e.y()}')
    #     self.searchResultList.hide()


class ImageEditing(QWidget):
    """Окно редактирования изображений"""

    def __init__(self, dataline, index=None):
        super(ImageEditing, self).__init__()
        self.setWindowTitle('Редактор параметров изображения')
        self.indexInFile = index
        self.tags = getImageTagsList(dataline)

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
        self.enterNameLine = QLineEdit(getImageName(self.dataLine))
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

        self.verticalLayout.insertWidget(5, self.searchResultList)
        self.verticalLayout.addItem(self.spacer)
        self.verticalLayout.addWidget(self.saveImageButton)

        self.enterNameLayout.addWidget(self.enterNameLayoutText)
        self.enterNameLayout.addWidget(self.enterNameLine)

        self.searchTagLayout.addWidget(self.searchTagLayoutText)
        self.searchTagLayout.addWidget(self.searchTagLine)

        self.setLayout(self.mainLayout)
        self.selectedImage.setPixmap(resizeImage(getImagePath(self.dataLine), 600, 400))

        self.searchTagLine.textChanged.connect(self.searchTag)
        self.addTagButton.clicked.connect(self.AddTagToImage)
        self.searchResultList.itemClicked.connect(self.ChooseTag)
        self.saveImageButton.clicked.connect(self.saveImage)
        self.enterNameLine.textChanged.connect(self.clearNameLine)

        self.searchResultList.hide()

    def clearNameLine(self):
        if self.enterNameLine.text().startswith('Введите'):
            self.enterNameLine.clear()

    def saveImage(self):
        """Сохранение изображения"""
        self.tags = map(lambda x: x.rstrip("\n"), (i for i in self.tags if i))
        lines = open('data.txt', encoding='utf-8').readlines()
        # print('lines:', *lines, end='end')
        if self.indexInFile:
            lines[self.indexInFile] = f'{getImagePath(self.dataLine)}:' \
                                      f'{self.enterNameLine.text()}:' \
                                      f'{";".join(self.tags)}'
        else:
            lines.append(f'{getImagePath(self.dataLine).strip()}:{self.enterNameLine.text()}:{";".join(self.tags)}')
        print(*map(lambda x: x.lstrip(), lines), file=open('data.txt', encoding='utf-8', mode='w'))
        # print('Image saved')
        ImageManager.displayImages(ex)
        self.close()

    def searchTag(self):
        """Поиск тега"""
        self.searchResultList.clear()
        self.searchResultList.show()
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
        """Присвоение тега изображению"""
        tag = self.searchTagLine.text()
        if tag in map(lambda x: x.lower(), open('tags.txt', encoding='utf-8').readlines()):
            self.tags.append(tag.rstrip('\n'))
            self.searchTagLine.clear()
            self.searchResultList.clear()
            self.tagsLabel.setText('\n'.join(self.tags))
            self.searchResultList.hide()


def resizeImage(path: str, newWidth: int, newHeight: int):
    return QPixmap(path).scaled(newWidth, newHeight)


def getImageName(line: str):
    return line.split(':')[-2]


def getImagePath(line: str):
    return ':'.join(line.split(':')[0:2]).lstrip()


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
