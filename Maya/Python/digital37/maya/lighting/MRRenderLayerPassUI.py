# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRRenderLayerPass.ui'
#
# Created: Mon Jan 09 20:18:03 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName(_fromUtf8("root"))
        root.resize(363, 441)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        root.setFont(font)
        root.setWindowTitle(QtGui.QApplication.translate("root", "Mental Ray Render Layer Tool V1.0 (37digital)", None, QtGui.QApplication.UnicodeUTF8))
        root.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(root)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Tab_layer = QtGui.QWidget()
        self.Tab_layer.setObjectName(_fromUtf8("Tab_layer"))
        self.layoutWidget = QtGui.QWidget(self.Tab_layer)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget_layer = QtGui.QTabWidget(self.Tab_layer)
        self.tabWidget_layer.setGeometry(QtCore.QRect(10, 0, 321, 361))
        self.tabWidget_layer.setObjectName(_fromUtf8("tabWidget_layer"))
        self.tab_color = QtGui.QWidget()
        self.tab_color.setObjectName(_fromUtf8("tab_color"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_color)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 12, 311, 310))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_assignedPasses = QtGui.QLabel(self.layoutWidget1)
        self.label_assignedPasses.setText(QtGui.QApplication.translate("root", "Assigned Passes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_assignedPasses.setObjectName(_fromUtf8("label_assignedPasses"))
        self.verticalLayout_5.addWidget(self.label_assignedPasses)
        self.listWidget_assignedPasses = QtGui.QListWidget(self.layoutWidget1)
        self.listWidget_assignedPasses.setProperty("showDropIndicator", False)
        self.listWidget_assignedPasses.setDragEnabled(True)
        self.listWidget_assignedPasses.setDragDropOverwriteMode(False)
        self.listWidget_assignedPasses.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_assignedPasses.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_assignedPasses.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_assignedPasses.setObjectName(_fromUtf8("listWidget_assignedPasses"))
        self.verticalLayout_5.addWidget(self.listWidget_assignedPasses)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_availablePasses = QtGui.QLabel(self.layoutWidget1)
        self.label_availablePasses.setText(QtGui.QApplication.translate("root", "Available Passes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_availablePasses.setObjectName(_fromUtf8("label_availablePasses"))
        self.verticalLayout_6.addWidget(self.label_availablePasses)
        self.listWidget_availablePasses = QtGui.QListWidget(self.layoutWidget1)
        self.listWidget_availablePasses.setProperty("showDropIndicator", False)
        self.listWidget_availablePasses.setDragEnabled(True)
        self.listWidget_availablePasses.setDragDropOverwriteMode(False)
        self.listWidget_availablePasses.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_availablePasses.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_availablePasses.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_availablePasses.setObjectName(_fromUtf8("listWidget_availablePasses"))
        self.verticalLayout_6.addWidget(self.listWidget_availablePasses)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_color_passFrefix = QtGui.QLabel(self.layoutWidget1)
        self.label_color_passFrefix.setText(QtGui.QApplication.translate("root", "Pass Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color_passFrefix.setObjectName(_fromUtf8("label_color_passFrefix"))
        self.horizontalLayout.addWidget(self.label_color_passFrefix)
        self.lineEdit_color_passPrefix = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_color_passPrefix.setObjectName(_fromUtf8("lineEdit_color_passPrefix"))
        self.horizontalLayout.addWidget(self.lineEdit_color_passPrefix)
        self.label_color_passSuffix = QtGui.QLabel(self.layoutWidget1)
        self.label_color_passSuffix.setText(QtGui.QApplication.translate("root", "Pass Suffix:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color_passSuffix.setObjectName(_fromUtf8("label_color_passSuffix"))
        self.horizontalLayout.addWidget(self.label_color_passSuffix)
        self.lineEdit_color_passSuffix = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_color_passSuffix.setObjectName(_fromUtf8("lineEdit_color_passSuffix"))
        self.horizontalLayout.addWidget(self.lineEdit_color_passSuffix)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_layerName = QtGui.QLabel(self.layoutWidget1)
        self.label_layerName.setText(QtGui.QApplication.translate("root", "Layer Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_layerName.setObjectName(_fromUtf8("label_layerName"))
        self.horizontalLayout_4.addWidget(self.label_layerName)
        self.lineEdit_color_layerName = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_color_layerName.setObjectName(_fromUtf8("lineEdit_color_layerName"))
        self.horizontalLayout_4.addWidget(self.lineEdit_color_layerName)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.pushButton_color_apply = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_color_apply.setText(QtGui.QApplication.translate("root", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_color_apply.setObjectName(_fromUtf8("pushButton_color_apply"))
        self.verticalLayout_7.addWidget(self.pushButton_color_apply)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.tabWidget_layer.addTab(self.tab_color, _fromUtf8(""))
        self.tab_aO = QtGui.QWidget()
        self.tab_aO.setObjectName(_fromUtf8("tab_aO"))
        self.layoutWidget_4 = QtGui.QWidget(self.tab_aO)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 110, 309, 85))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_color_passFrefix_2 = QtGui.QLabel(self.layoutWidget_4)
        self.label_color_passFrefix_2.setText(QtGui.QApplication.translate("root", "Pass Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color_passFrefix_2.setObjectName(_fromUtf8("label_color_passFrefix_2"))
        self.horizontalLayout_6.addWidget(self.label_color_passFrefix_2)
        self.lineEdit_ao_passPrefix = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_ao_passPrefix.setObjectName(_fromUtf8("lineEdit_ao_passPrefix"))
        self.horizontalLayout_6.addWidget(self.lineEdit_ao_passPrefix)
        self.label_color_passSuffix_2 = QtGui.QLabel(self.layoutWidget_4)
        self.label_color_passSuffix_2.setText(QtGui.QApplication.translate("root", "Pass Suffix:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color_passSuffix_2.setObjectName(_fromUtf8("label_color_passSuffix_2"))
        self.horizontalLayout_6.addWidget(self.label_color_passSuffix_2)
        self.lineEdit_ao_passSuffix = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_ao_passSuffix.setObjectName(_fromUtf8("lineEdit_ao_passSuffix"))
        self.horizontalLayout_6.addWidget(self.lineEdit_ao_passSuffix)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_layerName_2 = QtGui.QLabel(self.layoutWidget_4)
        self.label_layerName_2.setText(QtGui.QApplication.translate("root", "Layer Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_layerName_2.setObjectName(_fromUtf8("label_layerName_2"))
        self.horizontalLayout_7.addWidget(self.label_layerName_2)
        self.lineEdit_ao_layerName = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEdit_ao_layerName.setObjectName(_fromUtf8("lineEdit_ao_layerName"))
        self.horizontalLayout_7.addWidget(self.lineEdit_ao_layerName)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.pushButton_ao_apply = QtGui.QPushButton(self.layoutWidget_4)
        self.pushButton_ao_apply.setText(QtGui.QApplication.translate("root", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ao_apply.setObjectName(_fromUtf8("pushButton_ao_apply"))
        self.verticalLayout_11.addWidget(self.pushButton_ao_apply)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_aO)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 311, 101))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("root", "Create AO Layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget2 = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 260, 74))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.radioButton_ao = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_ao.setText(QtGui.QApplication.translate("root", "AO ( Render Layer by Material )", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_ao.setChecked(True)
        self.radioButton_ao.setObjectName(_fromUtf8("radioButton_ao"))
        self.verticalLayout_8.addWidget(self.radioButton_ao)
        self.radioButton_ao_transparency = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_ao_transparency.setText(QtGui.QApplication.translate("root", "AO Transpancy ( Render Layer by Material )", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_ao_transparency.setObjectName(_fromUtf8("radioButton_ao_transparency"))
        self.verticalLayout_8.addWidget(self.radioButton_ao_transparency)
        self.checkBox_addAoPass = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox_addAoPass.setText(QtGui.QApplication.translate("root", "Add AO Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_addAoPass.setObjectName(_fromUtf8("checkBox_addAoPass"))
        self.verticalLayout_8.addWidget(self.checkBox_addAoPass)
        self.tabWidget_layer.addTab(self.tab_aO, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget_5 = QtGui.QWidget(self.tab)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 240, 309, 85))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_color_passFrefix_3 = QtGui.QLabel(self.layoutWidget_5)
        self.label_color_passFrefix_3.setText(QtGui.QApplication.translate("root", "Pass Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color_passFrefix_3.setObjectName(_fromUtf8("label_color_passFrefix_3"))
        self.horizontalLayout_8.addWidget(self.label_color_passFrefix_3)
        self.lineEdit_ao_passPrefix_2 = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_ao_passPrefix_2.setObjectName(_fromUtf8("lineEdit_ao_passPrefix_2"))
        self.horizontalLayout_8.addWidget(self.lineEdit_ao_passPrefix_2)
        self.label_color_passSuffix_3 = QtGui.QLabel(self.layoutWidget_5)
        self.label_color_passSuffix_3.setText(QtGui.QApplication.translate("root", "Pass Suffix:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_color_passSuffix_3.setObjectName(_fromUtf8("label_color_passSuffix_3"))
        self.horizontalLayout_8.addWidget(self.label_color_passSuffix_3)
        self.lineEdit_ao_passSuffix_2 = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_ao_passSuffix_2.setObjectName(_fromUtf8("lineEdit_ao_passSuffix_2"))
        self.horizontalLayout_8.addWidget(self.lineEdit_ao_passSuffix_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_layerName_3 = QtGui.QLabel(self.layoutWidget_5)
        self.label_layerName_3.setText(QtGui.QApplication.translate("root", "Layer Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_layerName_3.setObjectName(_fromUtf8("label_layerName_3"))
        self.horizontalLayout_9.addWidget(self.label_layerName_3)
        self.lineEdit_ao_layerName_2 = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_ao_layerName_2.setObjectName(_fromUtf8("lineEdit_ao_layerName_2"))
        self.horizontalLayout_9.addWidget(self.lineEdit_ao_layerName_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.pushButton_ao_apply_2 = QtGui.QPushButton(self.layoutWidget_5)
        self.pushButton_ao_apply_2.setText(QtGui.QApplication.translate("root", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ao_apply_2.setObjectName(_fromUtf8("pushButton_ao_apply_2"))
        self.verticalLayout_12.addWidget(self.pushButton_ao_apply_2)
        self.tabWidget_layer.addTab(self.tab, _fromUtf8(""))
        self.tabWidget.addTab(self.Tab_layer, _fromUtf8(""))
        self.Tab_material = QtGui.QWidget()
        self.Tab_material.setObjectName(_fromUtf8("Tab_material"))
        self.groupBox_2 = QtGui.QGroupBox(self.Tab_material)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 311, 141))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("root", "Create Materials:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 291, 95))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_createMaterials_02 = QtGui.QHBoxLayout()
        self.horizontalLayout_createMaterials_02.setObjectName(_fromUtf8("horizontalLayout_createMaterials_02"))
        self.pushButton_CM_black = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_black.setText(QtGui.QApplication.translate("root", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_black.setObjectName(_fromUtf8("pushButton_CM_black"))
        self.horizontalLayout_createMaterials_02.addWidget(self.pushButton_CM_black)
        self.pushButton_CM_blackNoAlpha = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_blackNoAlpha.setText(QtGui.QApplication.translate("root", "Black No Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_blackNoAlpha.setObjectName(_fromUtf8("pushButton_CM_blackNoAlpha"))
        self.horizontalLayout_createMaterials_02.addWidget(self.pushButton_CM_blackNoAlpha)
        self.verticalLayout.addLayout(self.horizontalLayout_createMaterials_02)
        self.horizontalLayout_createMaterials_03 = QtGui.QHBoxLayout()
        self.horizontalLayout_createMaterials_03.setObjectName(_fromUtf8("horizontalLayout_createMaterials_03"))
        self.pushButton_CM_red = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_red.setText(QtGui.QApplication.translate("root", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_red.setObjectName(_fromUtf8("pushButton_CM_red"))
        self.horizontalLayout_createMaterials_03.addWidget(self.pushButton_CM_red)
        self.pushButton_CM_green = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_green.setText(QtGui.QApplication.translate("root", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_green.setObjectName(_fromUtf8("pushButton_CM_green"))
        self.horizontalLayout_createMaterials_03.addWidget(self.pushButton_CM_green)
        self.pushButton_CM_blue = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_blue.setText(QtGui.QApplication.translate("root", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_blue.setObjectName(_fromUtf8("pushButton_CM_blue"))
        self.horizontalLayout_createMaterials_03.addWidget(self.pushButton_CM_blue)
        self.verticalLayout.addLayout(self.horizontalLayout_createMaterials_03)
        self.horizontalLayout_createMaterials_04 = QtGui.QHBoxLayout()
        self.horizontalLayout_createMaterials_04.setObjectName(_fromUtf8("horizontalLayout_createMaterials_04"))
        self.pushButton_CM_useBackground = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_useBackground.setText(QtGui.QApplication.translate("root", "Use Background", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_useBackground.setObjectName(_fromUtf8("pushButton_CM_useBackground"))
        self.horizontalLayout_createMaterials_04.addWidget(self.pushButton_CM_useBackground)
        self.pushButton_CM_zDepth = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_CM_zDepth.setText(QtGui.QApplication.translate("root", "Z Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_zDepth.setObjectName(_fromUtf8("pushButton_CM_zDepth"))
        self.horizontalLayout_createMaterials_04.addWidget(self.pushButton_CM_zDepth)
        self.verticalLayout.addLayout(self.horizontalLayout_createMaterials_04)
        self.groupBox = QtGui.QGroupBox(self.Tab_material)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 311, 211))
        self.groupBox.setTitle(QtGui.QApplication.translate("root", "Render Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_renderStatus_02 = QtGui.QHBoxLayout()
        self.horizontalLayout_renderStatus_02.setObjectName(_fromUtf8("horizontalLayout_renderStatus_02"))
        self.checkBox_castsShadows = QtGui.QCheckBox(self.groupBox)
        self.checkBox_castsShadows.setEnabled(True)
        self.checkBox_castsShadows.setText(QtGui.QApplication.translate("root", "Casts Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_castsShadows.setChecked(True)
        self.checkBox_castsShadows.setObjectName(_fromUtf8("checkBox_castsShadows"))
        self.horizontalLayout_renderStatus_02.addWidget(self.checkBox_castsShadows)
        self.checkBox_receiveShadows = QtGui.QCheckBox(self.groupBox)
        self.checkBox_receiveShadows.setText(QtGui.QApplication.translate("root", "Receive Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_receiveShadows.setChecked(True)
        self.checkBox_receiveShadows.setObjectName(_fromUtf8("checkBox_receiveShadows"))
        self.horizontalLayout_renderStatus_02.addWidget(self.checkBox_receiveShadows)
        self.verticalLayout_2.addLayout(self.horizontalLayout_renderStatus_02)
        self.horizontalLayout_renderStatus_03 = QtGui.QHBoxLayout()
        self.horizontalLayout_renderStatus_03.setObjectName(_fromUtf8("horizontalLayout_renderStatus_03"))
        self.checkBox_motionBlur = QtGui.QCheckBox(self.groupBox)
        self.checkBox_motionBlur.setText(QtGui.QApplication.translate("root", "Motion Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_motionBlur.setChecked(True)
        self.checkBox_motionBlur.setObjectName(_fromUtf8("checkBox_motionBlur"))
        self.horizontalLayout_renderStatus_03.addWidget(self.checkBox_motionBlur)
        self.checkBox_primaryVisibility = QtGui.QCheckBox(self.groupBox)
        self.checkBox_primaryVisibility.setText(QtGui.QApplication.translate("root", "Primary Visibility", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_primaryVisibility.setChecked(True)
        self.checkBox_primaryVisibility.setObjectName(_fromUtf8("checkBox_primaryVisibility"))
        self.horizontalLayout_renderStatus_03.addWidget(self.checkBox_primaryVisibility)
        self.verticalLayout_2.addLayout(self.horizontalLayout_renderStatus_03)
        self.horizontalLayout_renderStatus_04 = QtGui.QHBoxLayout()
        self.horizontalLayout_renderStatus_04.setObjectName(_fromUtf8("horizontalLayout_renderStatus_04"))
        self.checkBox_smoothShading = QtGui.QCheckBox(self.groupBox)
        self.checkBox_smoothShading.setText(QtGui.QApplication.translate("root", "Smooth Shading", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_smoothShading.setChecked(True)
        self.checkBox_smoothShading.setObjectName(_fromUtf8("checkBox_smoothShading"))
        self.horizontalLayout_renderStatus_04.addWidget(self.checkBox_smoothShading)
        self.checkBox_visibleInReflections = QtGui.QCheckBox(self.groupBox)
        self.checkBox_visibleInReflections.setText(QtGui.QApplication.translate("root", "Visible In Reflections", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_visibleInReflections.setChecked(True)
        self.checkBox_visibleInReflections.setObjectName(_fromUtf8("checkBox_visibleInReflections"))
        self.horizontalLayout_renderStatus_04.addWidget(self.checkBox_visibleInReflections)
        self.verticalLayout_2.addLayout(self.horizontalLayout_renderStatus_04)
        self.horizontalLayout_renderStatus_05 = QtGui.QHBoxLayout()
        self.horizontalLayout_renderStatus_05.setObjectName(_fromUtf8("horizontalLayout_renderStatus_05"))
        self.checkBox_visibleInRefractions = QtGui.QCheckBox(self.groupBox)
        self.checkBox_visibleInRefractions.setText(QtGui.QApplication.translate("root", "Visible In Refractions", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_visibleInRefractions.setChecked(True)
        self.checkBox_visibleInRefractions.setObjectName(_fromUtf8("checkBox_visibleInRefractions"))
        self.horizontalLayout_renderStatus_05.addWidget(self.checkBox_visibleInRefractions)
        self.checkBox_doubleSided = QtGui.QCheckBox(self.groupBox)
        self.checkBox_doubleSided.setText(QtGui.QApplication.translate("root", "Double Sided", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_doubleSided.setChecked(True)
        self.checkBox_doubleSided.setTristate(False)
        self.checkBox_doubleSided.setObjectName(_fromUtf8("checkBox_doubleSided"))
        self.horizontalLayout_renderStatus_05.addWidget(self.checkBox_doubleSided)
        self.verticalLayout_2.addLayout(self.horizontalLayout_renderStatus_05)
        self.checkBox_opposite = QtGui.QCheckBox(self.groupBox)
        self.checkBox_opposite.setEnabled(False)
        self.checkBox_opposite.setText(QtGui.QApplication.translate("root", "Opposite", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_opposite.setChecked(False)
        self.checkBox_opposite.setObjectName(_fromUtf8("checkBox_opposite"))
        self.verticalLayout_2.addWidget(self.checkBox_opposite)
        self.pushButton_RS_apply = QtGui.QPushButton(self.groupBox)
        self.pushButton_RS_apply.setText(QtGui.QApplication.translate("root", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RS_apply.setObjectName(_fromUtf8("pushButton_RS_apply"))
        self.verticalLayout_2.addWidget(self.pushButton_RS_apply)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.Tab_material, _fromUtf8(""))
        self.tab_help = QtGui.QWidget()
        self.tab_help.setObjectName(_fromUtf8("tab_help"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_help)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 311, 171))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("root", "Create Render Layers:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget_3 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 30, 291, 126))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_createRenderLayers_02 = QtGui.QHBoxLayout()
        self.horizontalLayout_createRenderLayers_02.setObjectName(_fromUtf8("horizontalLayout_createRenderLayers_02"))
        self.pushButton_CRL_color = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CRL_color.setText(QtGui.QApplication.translate("root", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CRL_color.setObjectName(_fromUtf8("pushButton_CRL_color"))
        self.horizontalLayout_createRenderLayers_02.addWidget(self.pushButton_CRL_color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_createRenderLayers_02)
        self.pushButton_CRL_aO = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CRL_aO.setText(QtGui.QApplication.translate("root", "AO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CRL_aO.setObjectName(_fromUtf8("pushButton_CRL_aO"))
        self.verticalLayout_3.addWidget(self.pushButton_CRL_aO)
        self.horizontalLayout_createRenderLayers_03 = QtGui.QHBoxLayout()
        self.horizontalLayout_createRenderLayers_03.setObjectName(_fromUtf8("horizontalLayout_createRenderLayers_03"))
        self.pushButton_CRL_keyLight = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CRL_keyLight.setText(QtGui.QApplication.translate("root", "Key Light", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CRL_keyLight.setObjectName(_fromUtf8("pushButton_CRL_keyLight"))
        self.horizontalLayout_createRenderLayers_03.addWidget(self.pushButton_CRL_keyLight)
        self.pushButton_CRL_fillLight = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CRL_fillLight.setText(QtGui.QApplication.translate("root", "Fill Light", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CRL_fillLight.setObjectName(_fromUtf8("pushButton_CRL_fillLight"))
        self.horizontalLayout_createRenderLayers_03.addWidget(self.pushButton_CRL_fillLight)
        self.pushButton_CRL_backLight = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CRL_backLight.setText(QtGui.QApplication.translate("root", "Back Light", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CRL_backLight.setObjectName(_fromUtf8("pushButton_CRL_backLight"))
        self.horizontalLayout_createRenderLayers_03.addWidget(self.pushButton_CRL_backLight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_createRenderLayers_03)
        self.horizontalLayout_createRenderLayers_04 = QtGui.QHBoxLayout()
        self.horizontalLayout_createRenderLayers_04.setObjectName(_fromUtf8("horizontalLayout_createRenderLayers_04"))
        self.pushButton_CRL_shadow = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CRL_shadow.setText(QtGui.QApplication.translate("root", "Shadow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CRL_shadow.setObjectName(_fromUtf8("pushButton_CRL_shadow"))
        self.horizontalLayout_createRenderLayers_04.addWidget(self.pushButton_CRL_shadow)
        self.verticalLayout_3.addLayout(self.horizontalLayout_createRenderLayers_04)
        self.tabWidget.addTab(self.tab_help, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget)
        root.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(root)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_layer.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        self.listWidget_assignedPasses.setSortingEnabled(True)
        self.listWidget_availablePasses.setSortingEnabled(True)
        self.tabWidget_layer.setTabText(self.tabWidget_layer.indexOf(self.tab_color), QtGui.QApplication.translate("root", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_layer.setTabText(self.tabWidget_layer.indexOf(self.tab_aO), QtGui.QApplication.translate("root", "AO", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_layer.setTabText(self.tabWidget_layer.indexOf(self.tab), QtGui.QApplication.translate("root", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_layer), QtGui.QApplication.translate("root", "Render Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_material), QtGui.QApplication.translate("root", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_help), QtGui.QApplication.translate("root", "Help", None, QtGui.QApplication.UnicodeUTF8))

