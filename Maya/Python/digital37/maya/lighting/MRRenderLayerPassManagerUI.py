# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRRenderLayerPassManager.ui'
#
# Created: Sat Jan 21 14:10:54 2012
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
        root.resize(1314, 707)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        root.setFont(font)
        root.setWindowTitle(QtGui.QApplication.translate("root", "Mental Ray Render Layer Manager V1.0 (37digital)", None, QtGui.QApplication.UnicodeUTF8))
        root.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(root)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_MenuBar = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_MenuBar.setMargin(0)
        self.horizontalLayout_MenuBar.setObjectName(_fromUtf8("horizontalLayout_MenuBar"))
        self.pushButton_refresh = QtGui.QPushButton(self.widget)
        self.pushButton_refresh.setText(QtGui.QApplication.translate("root", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refresh.setObjectName(_fromUtf8("pushButton_refresh"))
        self.horizontalLayout_MenuBar.addWidget(self.pushButton_refresh)
        self.layoutWidget_3 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_10.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_createMaterials_04 = QtGui.QHBoxLayout()
        self.horizontalLayout_createMaterials_04.setObjectName(_fromUtf8("horizontalLayout_createMaterials_04"))
        self.checkBox_layerOverride_materiral = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_layerOverride_materiral.setEnabled(True)
        self.checkBox_layerOverride_materiral.setText(QtGui.QApplication.translate("root", "Layer Override", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_layerOverride_materiral.setChecked(True)
        self.checkBox_layerOverride_materiral.setObjectName(_fromUtf8("checkBox_layerOverride_materiral"))
        self.horizontalLayout_createMaterials_04.addWidget(self.checkBox_layerOverride_materiral)
        self.pushButton_CM_useBackground = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_useBackground.setText(QtGui.QApplication.translate("root", "Use Background", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_useBackground.setObjectName(_fromUtf8("pushButton_CM_useBackground"))
        self.horizontalLayout_createMaterials_04.addWidget(self.pushButton_CM_useBackground)
        self.pushButton_CM_zDepth = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_zDepth.setText(QtGui.QApplication.translate("root", "Z Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_zDepth.setObjectName(_fromUtf8("pushButton_CM_zDepth"))
        self.horizontalLayout_createMaterials_04.addWidget(self.pushButton_CM_zDepth)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_createMaterials_04)
        self.horizontalLayout_createMaterials_03 = QtGui.QHBoxLayout()
        self.horizontalLayout_createMaterials_03.setObjectName(_fromUtf8("horizontalLayout_createMaterials_03"))
        self.pushButton_CM_red = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_red.setText(QtGui.QApplication.translate("root", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_red.setObjectName(_fromUtf8("pushButton_CM_red"))
        self.horizontalLayout_createMaterials_03.addWidget(self.pushButton_CM_red)
        self.pushButton_CM_green = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_green.setText(QtGui.QApplication.translate("root", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_green.setObjectName(_fromUtf8("pushButton_CM_green"))
        self.horizontalLayout_createMaterials_03.addWidget(self.pushButton_CM_green)
        self.pushButton_CM_blue = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_blue.setText(QtGui.QApplication.translate("root", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_blue.setObjectName(_fromUtf8("pushButton_CM_blue"))
        self.horizontalLayout_createMaterials_03.addWidget(self.pushButton_CM_blue)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_createMaterials_03)
        self.horizontalLayout_createMaterials_02 = QtGui.QHBoxLayout()
        self.horizontalLayout_createMaterials_02.setObjectName(_fromUtf8("horizontalLayout_createMaterials_02"))
        self.pushButton_CM_black = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_black.setText(QtGui.QApplication.translate("root", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_black.setObjectName(_fromUtf8("pushButton_CM_black"))
        self.horizontalLayout_createMaterials_02.addWidget(self.pushButton_CM_black)
        self.pushButton_CM_blackNoAlpha = QtGui.QPushButton(self.layoutWidget_3)
        self.pushButton_CM_blackNoAlpha.setText(QtGui.QApplication.translate("root", "Black No Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CM_blackNoAlpha.setObjectName(_fromUtf8("pushButton_CM_blackNoAlpha"))
        self.horizontalLayout_createMaterials_02.addWidget(self.pushButton_CM_blackNoAlpha)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_createMaterials_02)
        self.layoutWidget_4 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_11.setMargin(0)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.pushButton_RS_apply = QtGui.QPushButton(self.layoutWidget_4)
        self.pushButton_RS_apply.setText(QtGui.QApplication.translate("root", "Apply Render Status", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RS_apply.setObjectName(_fromUtf8("pushButton_RS_apply"))
        self.horizontalLayout_11.addWidget(self.pushButton_RS_apply)
        self.checkBox_layerOverride_status = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_layerOverride_status.setEnabled(True)
        self.checkBox_layerOverride_status.setText(QtGui.QApplication.translate("root", "Layer Override", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_layerOverride_status.setChecked(True)
        self.checkBox_layerOverride_status.setObjectName(_fromUtf8("checkBox_layerOverride_status"))
        self.horizontalLayout_11.addWidget(self.checkBox_layerOverride_status)
        self.checkBox_castsShadows = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_castsShadows.setEnabled(True)
        self.checkBox_castsShadows.setText(QtGui.QApplication.translate("root", "Casts Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_castsShadows.setChecked(True)
        self.checkBox_castsShadows.setObjectName(_fromUtf8("checkBox_castsShadows"))
        self.horizontalLayout_11.addWidget(self.checkBox_castsShadows)
        self.checkBox_receiveShadows = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_receiveShadows.setText(QtGui.QApplication.translate("root", "Receive Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_receiveShadows.setChecked(True)
        self.checkBox_receiveShadows.setObjectName(_fromUtf8("checkBox_receiveShadows"))
        self.horizontalLayout_11.addWidget(self.checkBox_receiveShadows)
        self.checkBox_motionBlur = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_motionBlur.setText(QtGui.QApplication.translate("root", "Motion Blur", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_motionBlur.setChecked(True)
        self.checkBox_motionBlur.setObjectName(_fromUtf8("checkBox_motionBlur"))
        self.horizontalLayout_11.addWidget(self.checkBox_motionBlur)
        self.checkBox_primaryVisibility = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_primaryVisibility.setText(QtGui.QApplication.translate("root", "Primary Visibility", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_primaryVisibility.setChecked(True)
        self.checkBox_primaryVisibility.setObjectName(_fromUtf8("checkBox_primaryVisibility"))
        self.horizontalLayout_11.addWidget(self.checkBox_primaryVisibility)
        self.checkBox_smoothShading = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_smoothShading.setText(QtGui.QApplication.translate("root", "Smooth Shading", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_smoothShading.setChecked(True)
        self.checkBox_smoothShading.setObjectName(_fromUtf8("checkBox_smoothShading"))
        self.horizontalLayout_11.addWidget(self.checkBox_smoothShading)
        self.checkBox_visibleInReflections = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_visibleInReflections.setText(QtGui.QApplication.translate("root", "Visible In Reflections", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_visibleInReflections.setChecked(True)
        self.checkBox_visibleInReflections.setObjectName(_fromUtf8("checkBox_visibleInReflections"))
        self.horizontalLayout_11.addWidget(self.checkBox_visibleInReflections)
        self.checkBox_visibleInRefractions = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_visibleInRefractions.setText(QtGui.QApplication.translate("root", "Visible In Refractions", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_visibleInRefractions.setChecked(True)
        self.checkBox_visibleInRefractions.setObjectName(_fromUtf8("checkBox_visibleInRefractions"))
        self.horizontalLayout_11.addWidget(self.checkBox_visibleInRefractions)
        self.checkBox_doubleSided = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_doubleSided.setText(QtGui.QApplication.translate("root", "Double Sided", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_doubleSided.setChecked(True)
        self.checkBox_doubleSided.setTristate(False)
        self.checkBox_doubleSided.setObjectName(_fromUtf8("checkBox_doubleSided"))
        self.horizontalLayout_11.addWidget(self.checkBox_doubleSided)
        self.checkBox_opposite = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_opposite.setEnabled(False)
        self.checkBox_opposite.setText(QtGui.QApplication.translate("root", "Opposite", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_opposite.setChecked(False)
        self.checkBox_opposite.setObjectName(_fromUtf8("checkBox_opposite"))
        self.horizontalLayout_11.addWidget(self.checkBox_opposite)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_L = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_L.setMargin(0)
        self.verticalLayout_L.setObjectName(_fromUtf8("verticalLayout_L"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.comboBox_L = QtGui.QComboBox(self.widget1)
        self.comboBox_L.setObjectName(_fromUtf8("comboBox_L"))
        self.verticalLayout_10.addWidget(self.comboBox_L)
        self.verticalLayout_L.addLayout(self.verticalLayout_10)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.stackedWidget = QtGui.QStackedWidget(self.widget1)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_SL = QtGui.QWidget()
        self.page_SL.setObjectName(_fromUtf8("page_SL"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.page_SL)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.listWidget_SL = QtGui.QListWidget(self.page_SL)
        self.listWidget_SL.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_SL.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_SL.setObjectName(_fromUtf8("listWidget_SL"))
        self.verticalLayout_9.addWidget(self.listWidget_SL)
        self.pushButton_SL_add = QtGui.QPushButton(self.page_SL)
        self.pushButton_SL_add.setText(QtGui.QApplication.translate("root", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SL_add.setObjectName(_fromUtf8("pushButton_SL_add"))
        self.verticalLayout_9.addWidget(self.pushButton_SL_add)
        self.pushButton_SL_remove = QtGui.QPushButton(self.page_SL)
        self.pushButton_SL_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SL_remove.setObjectName(_fromUtf8("pushButton_SL_remove"))
        self.verticalLayout_9.addWidget(self.pushButton_SL_remove)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.stackedWidget.addWidget(self.page_SL)
        self.page_CL = QtGui.QWidget()
        self.page_CL.setObjectName(_fromUtf8("page_CL"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.page_CL)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.listWidget_CL = QtGui.QListWidget(self.page_CL)
        self.listWidget_CL.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_CL.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_CL.setObjectName(_fromUtf8("listWidget_CL"))
        self.verticalLayout_11.addWidget(self.listWidget_CL)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_layerName = QtGui.QLabel(self.page_CL)
        self.label_layerName.setText(QtGui.QApplication.translate("root", "Layer Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_layerName.setObjectName(_fromUtf8("label_layerName"))
        self.horizontalLayout_4.addWidget(self.label_layerName)
        self.lineEdit_layerName = QtGui.QLineEdit(self.page_CL)
        self.lineEdit_layerName.setObjectName(_fromUtf8("lineEdit_layerName"))
        self.horizontalLayout_4.addWidget(self.lineEdit_layerName)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.comboBox_CL = QtGui.QComboBox(self.page_CL)
        self.comboBox_CL.setObjectName(_fromUtf8("comboBox_CL"))
        self.verticalLayout_11.addWidget(self.comboBox_CL)
        self.pushButton_CL_add = QtGui.QPushButton(self.page_CL)
        self.pushButton_CL_add.setText(QtGui.QApplication.translate("root", "                      Add                     ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CL_add.setObjectName(_fromUtf8("pushButton_CL_add"))
        self.verticalLayout_11.addWidget(self.pushButton_CL_add)
        self.pushButton_CL_remove = QtGui.QPushButton(self.page_CL)
        self.pushButton_CL_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CL_remove.setObjectName(_fromUtf8("pushButton_CL_remove"))
        self.verticalLayout_11.addWidget(self.pushButton_CL_remove)
        self.pushButton_CL_apply = QtGui.QPushButton(self.page_CL)
        self.pushButton_CL_apply.setText(QtGui.QApplication.translate("root", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CL_apply.setObjectName(_fromUtf8("pushButton_CL_apply"))
        self.verticalLayout_11.addWidget(self.pushButton_CL_apply)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.stackedWidget.addWidget(self.page_CL)
        self.verticalLayout_7.addWidget(self.stackedWidget)
        self.verticalLayout_L.addLayout(self.verticalLayout_7)
        self.widget2 = QtGui.QWidget(self.splitter)
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_AO = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_AO.setMargin(0)
        self.verticalLayout_AO.setObjectName(_fromUtf8("verticalLayout_AO"))
        self.label_OBJ = QtGui.QLabel(self.widget2)
        self.label_OBJ.setText(QtGui.QApplication.translate("root", "Associated Objects:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_OBJ.setObjectName(_fromUtf8("label_OBJ"))
        self.verticalLayout_AO.addWidget(self.label_OBJ)
        self.listWidget_AO = QtGui.QListWidget(self.widget2)
        self.listWidget_AO.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_AO.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_AO.setObjectName(_fromUtf8("listWidget_AO"))
        self.verticalLayout_AO.addWidget(self.listWidget_AO)
        self.pushButton_AO_add = QtGui.QPushButton(self.widget2)
        self.pushButton_AO_add.setText(QtGui.QApplication.translate("root", "                      Add                     ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AO_add.setObjectName(_fromUtf8("pushButton_AO_add"))
        self.verticalLayout_AO.addWidget(self.pushButton_AO_add)
        self.pushButton_AO_remove = QtGui.QPushButton(self.widget2)
        self.pushButton_AO_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AO_remove.setObjectName(_fromUtf8("pushButton_AO_remove"))
        self.verticalLayout_AO.addWidget(self.pushButton_AO_remove)
        self.widget3 = QtGui.QWidget(self.splitter)
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.verticalLayout_O = QtGui.QVBoxLayout(self.widget3)
        self.verticalLayout_O.setMargin(0)
        self.verticalLayout_O.setObjectName(_fromUtf8("verticalLayout_O"))
        self.label_Outline = QtGui.QLabel(self.widget3)
        self.label_Outline.setText(QtGui.QApplication.translate("root", "Overrides:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Outline.setObjectName(_fromUtf8("label_Outline"))
        self.verticalLayout_O.addWidget(self.label_Outline)
        self.listWidget_O = QtGui.QListWidget(self.widget3)
        self.listWidget_O.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_O.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_O.setObjectName(_fromUtf8("listWidget_O"))
        self.verticalLayout_O.addWidget(self.listWidget_O)
        self.pushButton_O_remove = QtGui.QPushButton(self.widget3)
        self.pushButton_O_remove.setText(QtGui.QApplication.translate("root", "                Remove                ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_O_remove.setObjectName(_fromUtf8("pushButton_O_remove"))
        self.verticalLayout_O.addWidget(self.pushButton_O_remove)
        self.widget4 = QtGui.QWidget(self.splitter)
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.verticalLayout_P = QtGui.QVBoxLayout(self.widget4)
        self.verticalLayout_P.setMargin(0)
        self.verticalLayout_P.setObjectName(_fromUtf8("verticalLayout_P"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_SP = QtGui.QLabel(self.widget4)
        self.label_SP.setText(QtGui.QApplication.translate("root", "Scene Passes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_SP.setObjectName(_fromUtf8("label_SP"))
        self.verticalLayout.addWidget(self.label_SP)
        self.listWidget_SP = QtGui.QListWidget(self.widget4)
        self.listWidget_SP.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_SP.setDragEnabled(True)
        self.listWidget_SP.setDragDropOverwriteMode(False)
        self.listWidget_SP.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_SP.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_SP.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_SP.setObjectName(_fromUtf8("listWidget_SP"))
        self.verticalLayout.addWidget(self.listWidget_SP)
        self.pushButton_SP_remove = QtGui.QPushButton(self.widget4)
        self.pushButton_SP_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SP_remove.setObjectName(_fromUtf8("pushButton_SP_remove"))
        self.verticalLayout.addWidget(self.pushButton_SP_remove)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_AVP = QtGui.QLabel(self.widget4)
        self.label_AVP.setText(QtGui.QApplication.translate("root", "Available Passes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_AVP.setObjectName(_fromUtf8("label_AVP"))
        self.verticalLayout_2.addWidget(self.label_AVP)
        self.listWidget_AVP = QtGui.QListWidget(self.widget4)
        self.listWidget_AVP.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_AVP.setDragEnabled(True)
        self.listWidget_AVP.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_AVP.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_AVP.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_AVP.setObjectName(_fromUtf8("listWidget_AVP"))
        self.verticalLayout_2.addWidget(self.listWidget_AVP)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_P.addLayout(self.horizontalLayout_2)
        self.verticalLayout_AP = QtGui.QVBoxLayout()
        self.verticalLayout_AP.setObjectName(_fromUtf8("verticalLayout_AP"))
        self.label_AP = QtGui.QLabel(self.widget4)
        self.label_AP.setText(QtGui.QApplication.translate("root", "Associated Passes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_AP.setObjectName(_fromUtf8("label_AP"))
        self.verticalLayout_AP.addWidget(self.label_AP)
        self.listWidget_ASP = QtGui.QListWidget(self.widget4)
        self.listWidget_ASP.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_ASP.setDragEnabled(True)
        self.listWidget_ASP.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_ASP.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_ASP.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_ASP.setObjectName(_fromUtf8("listWidget_ASP"))
        self.verticalLayout_AP.addWidget(self.listWidget_ASP)
        self.pushButton_ASP_remove = QtGui.QPushButton(self.widget4)
        self.pushButton_ASP_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ASP_remove.setObjectName(_fromUtf8("pushButton_ASP_remove"))
        self.verticalLayout_AP.addWidget(self.pushButton_ASP_remove)
        self.verticalLayout_P.addLayout(self.verticalLayout_AP)
        self.widget5 = QtGui.QWidget(self.splitter)
        self.widget5.setObjectName(_fromUtf8("widget5"))
        self.verticalLayout_M = QtGui.QVBoxLayout(self.widget5)
        self.verticalLayout_M.setMargin(0)
        self.verticalLayout_M.setObjectName(_fromUtf8("verticalLayout_M"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_SCM = QtGui.QVBoxLayout()
        self.verticalLayout_SCM.setObjectName(_fromUtf8("verticalLayout_SCM"))
        self.label_CM_2 = QtGui.QLabel(self.widget5)
        self.label_CM_2.setText(QtGui.QApplication.translate("root", "Scene Contr. Maps:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CM_2.setObjectName(_fromUtf8("label_CM_2"))
        self.verticalLayout_SCM.addWidget(self.label_CM_2)
        self.listWidget_SCM = QtGui.QListWidget(self.widget5)
        self.listWidget_SCM.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_SCM.setDragEnabled(True)
        self.listWidget_SCM.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_SCM.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_SCM.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_SCM.setObjectName(_fromUtf8("listWidget_SCM"))
        self.verticalLayout_SCM.addWidget(self.listWidget_SCM)
        self.pushButton_SCM_add = QtGui.QPushButton(self.widget5)
        self.pushButton_SCM_add.setText(QtGui.QApplication.translate("root", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SCM_add.setObjectName(_fromUtf8("pushButton_SCM_add"))
        self.verticalLayout_SCM.addWidget(self.pushButton_SCM_add)
        self.pushButton_SCM_remove = QtGui.QPushButton(self.widget5)
        self.pushButton_SCM_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SCM_remove.setObjectName(_fromUtf8("pushButton_SCM_remove"))
        self.verticalLayout_SCM.addWidget(self.pushButton_SCM_remove)
        self.horizontalLayout_5.addLayout(self.verticalLayout_SCM)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_CM = QtGui.QLabel(self.widget5)
        self.label_CM.setText(QtGui.QApplication.translate("root", "Associated Contr. Maps:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CM.setObjectName(_fromUtf8("label_CM"))
        self.verticalLayout_4.addWidget(self.label_CM)
        self.listWidget_ACM = QtGui.QListWidget(self.widget5)
        self.listWidget_ACM.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_ACM.setDragEnabled(True)
        self.listWidget_ACM.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_ACM.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_ACM.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_ACM.setObjectName(_fromUtf8("listWidget_ACM"))
        self.verticalLayout_4.addWidget(self.listWidget_ACM)
        self.pushButton_ACM_add = QtGui.QPushButton(self.widget5)
        self.pushButton_ACM_add.setText(QtGui.QApplication.translate("root", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ACM_add.setObjectName(_fromUtf8("pushButton_ACM_add"))
        self.verticalLayout_4.addWidget(self.pushButton_ACM_add)
        self.pushButton_ACM_remove = QtGui.QPushButton(self.widget5)
        self.pushButton_ACM_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ACM_remove.setObjectName(_fromUtf8("pushButton_ACM_remove"))
        self.verticalLayout_4.addWidget(self.pushButton_ACM_remove)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_M.addLayout(self.horizontalLayout_5)
        self.verticalLayout_AOCM = QtGui.QVBoxLayout()
        self.verticalLayout_AOCM.setObjectName(_fromUtf8("verticalLayout_AOCM"))
        self.label_CM_3 = QtGui.QLabel(self.widget5)
        self.label_CM_3.setText(QtGui.QApplication.translate("root", "Associated Objects:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CM_3.setObjectName(_fromUtf8("label_CM_3"))
        self.verticalLayout_AOCM.addWidget(self.label_CM_3)
        self.listWidget_AOCM = QtGui.QListWidget(self.widget5)
        self.listWidget_AOCM.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.listWidget_AOCM.setDragEnabled(True)
        self.listWidget_AOCM.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget_AOCM.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_AOCM.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_AOCM.setObjectName(_fromUtf8("listWidget_AOCM"))
        self.verticalLayout_AOCM.addWidget(self.listWidget_AOCM)
        self.pushButton_AOCM_add = QtGui.QPushButton(self.widget5)
        self.pushButton_AOCM_add.setText(QtGui.QApplication.translate("root", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AOCM_add.setObjectName(_fromUtf8("pushButton_AOCM_add"))
        self.verticalLayout_AOCM.addWidget(self.pushButton_AOCM_add)
        self.pushButton_AOCM_remove = QtGui.QPushButton(self.widget5)
        self.pushButton_AOCM_remove.setText(QtGui.QApplication.translate("root", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AOCM_remove.setObjectName(_fromUtf8("pushButton_AOCM_remove"))
        self.verticalLayout_AOCM.addWidget(self.pushButton_AOCM_remove)
        self.verticalLayout_M.addLayout(self.verticalLayout_AOCM)
        self.verticalLayout_3.addWidget(self.splitter_2)
        root.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(root)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        root.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(root)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1314, 18))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFIle = QtGui.QMenu(self.menuBar)
        self.menuFIle.setTitle(QtGui.QApplication.translate("root", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        root.setMenuBar(self.menuBar)
        self.actionImport_Layers = QtGui.QAction(root)
        self.actionImport_Layers.setText(QtGui.QApplication.translate("root", "Import Layers ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Layers.setObjectName(_fromUtf8("actionImport_Layers"))
        self.actionExport_Layers = QtGui.QAction(root)
        self.actionExport_Layers.setText(QtGui.QApplication.translate("root", "Export Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Layers.setObjectName(_fromUtf8("actionExport_Layers"))
        self.menuFIle.addAction(self.actionImport_Layers)
        self.menuFIle.addAction(self.actionExport_Layers)
        self.menuBar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(root)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        pass

