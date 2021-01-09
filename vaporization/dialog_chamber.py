# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\khony\AppData\Local\Programs\Python\OOP_diploma\project\vaporization\dialog_chamber.ui'
#
# Created: Sat Jan 09 13:38:16 2021
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 180)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.ok_button = QtGui.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(10, 140, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.h_label = QtGui.QLabel(Dialog)
        self.h_label.setGeometry(QtCore.QRect(100, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.h_label.setFont(font)
        self.h_label.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.h_label.setAlignment(QtCore.Qt.AlignCenter)
        self.h_label.setObjectName("h_label")
        self.distance = QtGui.QDoubleSpinBox(Dialog)
        self.distance.setGeometry(QtCore.QRect(10, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.distance.setFont(font)
        self.distance.setMaximum(20.0)
        self.distance.setSingleStep(0.1)
        self.distance.setObjectName("distance")
        self.weight = QtGui.QDoubleSpinBox(Dialog)
        self.weight.setGeometry(QtCore.QRect(10, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.weight.setFont(font)
        self.weight.setDecimals(3)
        self.weight.setMaximum(9.999)
        self.weight.setSingleStep(0.001)
        self.weight.setObjectName("weight")
        self.m_label = QtGui.QLabel(Dialog)
        self.m_label.setGeometry(QtCore.QRect(100, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.m_label.setFont(font)
        self.m_label.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.m_label.setAlignment(QtCore.Qt.AlignCenter)
        self.m_label.setObjectName("m_label")
        self.radius = QtGui.QDoubleSpinBox(Dialog)
        self.radius.setGeometry(QtCore.QRect(10, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.radius.setFont(font)
        self.radius.setMaximum(10.0)
        self.radius.setSingleStep(0.1)
        self.radius.setObjectName("radius")
        self.r_label = QtGui.QLabel(Dialog)
        self.r_label.setGeometry(QtCore.QRect(100, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.r_label.setFont(font)
        self.r_label.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.r_label.setAlignment(QtCore.Qt.AlignCenter)
        self.r_label.setObjectName("r_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Cu", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Al", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Ti", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.h_label.setText(QtGui.QApplication.translate("Dialog", "h, cm", None, QtGui.QApplication.UnicodeUTF8))
        self.m_label.setText(QtGui.QApplication.translate("Dialog", "m, g", None, QtGui.QApplication.UnicodeUTF8))
        self.r_label.setText(QtGui.QApplication.translate("Dialog", "r, cm", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

