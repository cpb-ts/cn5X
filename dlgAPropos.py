# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgAPropos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgApropos(object):
    def setupUi(self, dlgApropos):
        dlgApropos.setObjectName("dlgApropos")
        dlgApropos.setWindowModality(QtCore.Qt.ApplicationModal)
        dlgApropos.resize(768, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/cn5X/images/XYZAB.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        dlgApropos.setWindowIcon(icon)
        dlgApropos.setSizeGripEnabled(False)
        dlgApropos.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(dlgApropos)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(dlgApropos)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(178, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cn5X/images/XYZAB.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setText("<h1>cn5X++</h1>")
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lblVersion = QtWidgets.QLabel(self.tab)
        self.lblVersion.setObjectName("lblVersion")
        self.verticalLayout_3.addWidget(self.lblVersion)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setText("Copyright (C) Gauthier Brière - 2018-2022")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.frame1 = QtWidgets.QFrame(self.tab)
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 5))
        self.frame1.setLineWidth(3)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setMinimumSize(QtCore.QSize(300, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setText(
            "This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n"
            "This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n"
            "You should have received a copy of the GNU General Public License along with this program.\n"
            "If not, see <http://www.gnu.org/licenses/>."
        )
        self.label_4.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.qptLicence = QtWidgets.QPlainTextEdit(self.tab_2)
        self.qptLicence.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.qptLicence.setReadOnly(True)
        self.qptLicence.setPlainText("")
        self.qptLicence.setObjectName("qptLicence")
        self.horizontalLayout_4.addWidget(self.qptLicence)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem6)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgApropos)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(dlgApropos)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(dlgApropos.accept)
        self.buttonBox.rejected.connect(dlgApropos.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgApropos)

    def retranslateUi(self, dlgApropos):
        _translate = QtCore.QCoreApplication.translate
        dlgApropos.setWindowTitle(_translate("dlgApropos", "About cn5X++"))
        self.lblVersion.setText(_translate("dlgApropos", "Version 0.0"))
        self.label_3.setText(
            _translate(
                "dlgApropos",
                "CN5X++ is a 5/6 axis control panel application for Grbl-controlled digital machines.\n"
                "This application is intended to implement all the features of the grbl-Mega-5X firmware.",
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("dlgApropos", "Information")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("dlgApropos", "License")
        )


import cn5X_rc
