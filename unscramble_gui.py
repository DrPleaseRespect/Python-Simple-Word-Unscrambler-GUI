import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window_ui_v2 import Ui_MainWindow
import logging

Dictionary = 'huge_dict.txt'
Icon = 'icon.ico'
VERSION = "1.1.0"

class Unscrambler(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)
    progressmax = QtCore.pyqtSignal(int)
    senditem = QtCore.pyqtSignal(str)
    Queuetext = QtCore.pyqtSignal(str)
    cleartext = QtCore.pyqtSignal()
    def unscramble(self, words, scrambled):
        self.cleartext.emit()
        input_total = len(scrambled)
        progressmax_int = len(words) * len(scrambled)
        self.progressmax.emit(progressmax_int)
        logging.info(F"Progress Maximum Set")
        iteration = 0
        progress = 0
        for individual_scrambled in scrambled:
            logging.info(F"Progress Defined to 0")
            iteration += 1
            logging.info(F"Iteration Value: {iteration}")
            self.Queuetext.emit(F"{iteration}/{input_total}")
            self.senditem.emit(F"------")
            logging.debug(F"Queuetext and senditem emitters has been emitted")
            for i in words:
                progress += 1
                
                if len(i) != len(individual_scrambled):
                    continue
                listword = list(i)
                scrambled_backup = individual_scrambled
                list_scrambled = list(scrambled_backup)
                self.progress.emit(progress + 1)
                for letter in listword:
                    if letter in list_scrambled:
                        list_scrambled.remove(letter)
                    if len(list_scrambled) <= 0:
                        self.senditem.emit(str(i))
            
        
        self.progress.emit(progressmax_int)
        self.finished.emit()



            

        
        


   

class About(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 273)
        Dialog.setMinimumSize(QtCore.QSize(483, 273))
        Dialog.setMaximumSize(QtCore.QSize(483, 273))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Page"))
        self.label.setText(_translate("Dialog", "Programmer:"))
        self.label_2.setText(_translate("Dialog", "Julian Nayr (DrPleaseRespect)"))
        self.label_5.setText(_translate("Dialog", "Tools Used:"))
        self.label_6.setText(_translate("Dialog", "Visual Studio Code"))
        self.label_9.setText(_translate("Dialog", "Python"))
        self.label_7.setText(_translate("Dialog", "PyQt5"))
        self.label_8.setText(_translate("Dialog", "Qt Designer"))
        self.label_3.setText(_translate("Dialog", "Wordlist Used:"))
        self.label_4.setText(_translate("Dialog", "SCOWL: http://wordlist.aspell.net/"))
        self.label_10.setText(_translate("Dialog", "Version:"))
        self.label_11.setText(_translate("Dialog", VERSION))

        
class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.show()
        self.toolBar.actionTriggered['QAction*'].connect(self.ShowAboutDialog)
        self.UnscrambledButton.clicked.connect(self.unscramble)
        self.Input.textChanged.connect(self.InputChanged)
        self.Input.returnPressed.connect(self.returnpressed)
        self.setWindowIcon(QtGui.QIcon(Icon))

    def returnpressed(self):
        if self.Input.text() == "":
            pass
        else:
            self.unscramble()
    
    def InputChanged(self):
        if self.Input.text() == "":
            self.UnscrambledButton.setEnabled(False)
        else:
            self.UnscrambledButton.setEnabled(True)

    def ShowAboutDialog(QAction):
        dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        dialog.setWindowIcon(QtGui.QIcon(Icon))
        about_ui = About()
        about_ui.setupUi(dialog)
        dialog.exec()

    def unscramble(self):
        self.UnscrambledButton.setEnabled(False)
        self.Input.setEnabled(False)
        scrambled = self.Input.text().lower().split()
        words = load_words()
        self.thread = QtCore.QThread()
        self.unscrambler = Unscrambler()
        self.unscrambler.moveToThread(self.thread)
        self.thread.started.connect(lambda:self.unscrambler.unscramble(words,scrambled))
        self.unscrambler.finished.connect(self.thread.quit)
        self.unscrambler.finished.connect(self.unscrambler.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.unscrambler.progress.connect(self.setprogress)
        self.unscrambler.progressmax.connect(self.setmaxprogress)
        self.unscrambler.senditem.connect(self.senditem)
        self.unscrambler.Queuetext.connect(self.setqueue)
        self.unscrambler.finished.connect(self.unscramblefinished)
        self.unscrambler.cleartext.connect(self.cleartext)
        self.thread.start()




    def old_unscramble(self):
        self.resultslist.clear()
        self.UnscrambledButton.setEnabled(False)
        self.Input.setEnabled(False)
        scrambled = self.Input.text().lower().split()
        matched = []
        iteration = 0
        words = load_words()
        self.Lines.setText("0/0")
        input_total = len(scrambled)
        self.progressBar.setMaximum(len(words))
        for individiual_scrambled in scrambled:
            progress = 0
            iteration += 1
            self.Lines.setText(F"{iteration}/{input_total}")
            if iteration > 1:
                self.resultslist.addItem(F"------")
            for i in words:
                progress += 1
                if len(i) != len(individiual_scrambled):
                    continue
                self.progressBar.setValue(progress)
                listword = list(i)
                scrambled_backup = individiual_scrambled
                list_scrambled = list(scrambled_backup)

                
                for letter in listword:
                    if letter in list_scrambled:
                        list_scrambled.remove(letter)
                    if len(list_scrambled) <= 0:
                        self.resultslist.addItem(str(i))
        #self.progressBar.setValue(100)
        #self.resultslist.addItems(matched)
        self.UnscrambledButton.setEnabled(True)
        self.Input.setEnabled(True)
        self.Input.clear()
        self.Lines.setText("0/0")

    def setmaxprogress(self, max):
        self.progressBar.setMaximum(max)

    def setprogress(self, progress):
        self.progressBar.setValue(progress)

    def senditem(self, item):
        self.resultslist.addItem(str(item))
        self.repaint()

    def setqueue(self, queue):
        self.Lines.setText(queue)

    def unscramblefinished(self):
        self.UnscrambledButton.setEnabled(True)
        self.Input.setEnabled(True)
        self.Input.clear()
        self.progressBar.setValue(0)

    def cleartext(self):
        self.resultslist.clear()


def load_words():
    with open(Dictionary) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

load_words()
app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
app.exec()