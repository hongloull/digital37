# -*- coding: utf-8 -*-
#Description:
# -*- coding: utf-8 -*- 
#Author:honglou(hongloull@gmail.com)
#Create:2011.12.06
#Update: 2012.02.01
#How to use : 
import logging
import traceback
import itertools
import os
import sip
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
import maya.OpenMayaUI

# Make RenderLayerPassUI by: pyuic4 RenderLayerPassManager.ui>RLPUI.py
import digital37.maya.lighting.RenderLayerPassManagerUI as RLPUI
# reload only for tests
reload(RLPUI)

import digital37.maya.lighting.RenderLayerPass as RLP
# reload only for tests
reload(RLP)
 
import digital37.qt.Dialog as Dialog
reload(Dialog)

class StartRenderLayerPassManager(QtGui.QMainWindow,RLPUI.Ui_root):
    def __init__(self, parent=None, debug=True):
        
        self.DEBUG = debug
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.RLP = RLP.RenderLayerPass(self.DEBUG)
        
        # init model
        self.MODEL = 'C'
        
        # Init widget
        self.init_combobox_L()
        self.init_combobox_CL()
        self.init_lineEdit_layerName()
        
        self.lineEdit_layerName.textChanged.connect( self.set_lineEdit_layerName )
        self.comboBox_L.currentIndexChanged.connect( self.switchStackedWidget )
        self.comboBox_CL.currentIndexChanged.connect( self.setCreationLayerPreset )
         
        #self.ui.listWidget_L.itemSelectionChanged.connect( self.updateAll )
        self.listWidget_SL.itemSelectionChanged.connect( self.updateLayerSettings_manager )
        self.listWidget_CL.itemSelectionChanged.connect( self.updateLayerSettings_creation )
        
        # for rename layer
        self.listWidget_SL.itemDoubleClicked.connect( self.getActiveLayer )
        self.listWidget_CL.itemDoubleClicked.connect( self.get_layer_name_before_rename )
        
        self.listWidget_SL.itemChanged.connect( self.renameLayer_SL )
        self.listWidget_CL.itemChanged.connect( self.renameLayer_CL )
        
        self.listWidget_SP.itemChanged.connect( self.updateScenePasses )
        self.listWidget_ASP.itemChanged.connect( self.updateAssociatedPasses )
        
        self.checkBox_doubleSided.clicked.connect( self.updateCheckBox_opposite )
        
        self.listWidget_AO.itemSelectionChanged.connect( self.select_obj_from_list )
        
        self.listWidget_SP.dragMoveEvent = self.dragMoveEvent_SP
        self.listWidget_ASP.dragMoveEvent = self.dragMoveEvent_ASP
        self.listWidget_AVP.dragMoveEvent = self.dragMoveEvent_AVP
        
        # init lists
        self.updateAll()
        
        self.addMenu()
        
        # pop menu
        self.createPopupMenu()
        
    def create_dialog(self,title,labelText):
        # Must use self for display
        self.Dialog = QtGui.QDialog()
        self.Dialog.ui = Dialog.Ui_Dialog()
        self.Dialog.ui.setupUi(self.Dialog)
        self.Dialog.setWindowTitle(title)
        self.Dialog.ui.label.setText(labelText)
        self.Dialog.show()
        
    def file_dialog(self):
        text = None
        self.RLP.create_user_settings_dir()
        fd = QtGui.QFileDialog(self,'',RLP.RenderLayerPass.USER_DIR,'')
        filename = fd.getOpenFileName()
        if os.path.isfile(filename):
            text = open(filename).read()
        return text
                    
    def create_create_layer_preset_dialog(self,title,labelText):
        self.create_dialog(title, labelText)
        QtCore.QObject.connect(self.Dialog.ui.buttonBox, \
                               QtCore.SIGNAL(_fromUtf8("accepted()")),\
                               self.create_preset_from_layer)
        
    def create_apply_layer_preset_dialog(self,title,labelText):
        # get layers selected
        self.getSelectedLayers()
        if self.RLP.LAYERS_CREATION_SELECTED :
            text = self.file_dialog()
            if text:
                if self.DEBUG:
                    logging.debug('get from file:')
                    print text
                # convert xml to dictionary
                self.apply_preset_to_layer(text)
            else:
                self.RLP.warning('can not read from selected file.')
        else:
            self.RLP.warning('select some layers first.')
                
    def addMenu(self):
        # refresh menu
        self.action_refresh = QtGui.QAction(QtGui.QIcon('icons/web.png'), 'Refresh', self)
        self.action_refresh.setShortcut('F5')
        self.action_refresh.setStatusTip('refresh application')
        self.connect(self.action_refresh, QtCore.SIGNAL('triggered()'), self.updateAll)
        
        menubar = self.menuBar()
        edit_menu = menubar.addMenu('&Edit')
        edit_menu.addAction(self.action_refresh)
        
    def switchStackedWidget(self):
        # Get combobox selected index
        self.stackedWidget.setCurrentIndex( self.comboBox_L.currentIndex() )
        if self.comboBox_L.currentIndex() == 0 :
            self.MODEL = 'M'
        else:
            self.MODEL = 'C'
        self.updateAll()
            
    def setCreationLayerPreset(self):
        # Get combobox selected index
        layerPreset = str( self.comboBox_CL.currentText() )
        # Get selected layers
        self.getSelectedLayers()
        self.RLP.set_creation_layers_attr('PRESET', layerPreset,'Update')
        
    def updateLayerPresetCombobox(self):
        self.getSelectedLayers()
        # Only one layer selected, preset will update
        if self.MODEL == 'C' and len(self.RLP.LAYERS_CREATION_SELECTED) == 1 :
            # Get layer preset attr
            preset = self.RLP.get_creation_layer_attr(self.RLP.LAYER_CREATION_ACTIVE, 'PRESET')
            # Set preset
            logging.debug('prest:%s',preset)
            if preset and preset != str( self.comboBox_CL.currentText() ) :
                i = self.comboBox_CL.findText( QtCore.QString(preset), QtCore.Qt.MatchFixedString)
                self.comboBox_CL.setCurrentIndex(i)
        
    def updateCheckBox_opposite(self):
        if self.checkBox_doubleSided.isChecked() :
            self.checkBox_opposite.setEnabled(False)
        else :
            self.checkBox_opposite.setEnabled(True)
        
    def createPopupMenu(self):
        self.listWidget_CL.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_CL.customContextMenuRequested.connect(self.showPopupMenu)
        
        self.contextMenu = QtGui.QMenu(self)  
        self.actionA = self.contextMenu.addAction(u'Add')  
        self.actionB = self.contextMenu.addAction(u'Remove')  
        self.actionA.triggered.connect(self.actionHandler_add)  
        self.actionB.triggered.connect(self.actionHandler_remove)
        
        self.contextMenu.addSeparator()
        
        self.presetMenu = QtGui.QMenu('Layer Preset',self)
        self.contextMenu.addMenu(self.presetMenu)
        
        self.action_create = self.presetMenu.addAction(u'Create')
        self.action_create.triggered.connect(self.show_create_preset_from_layer_dialog)
        self.action_create = self.presetMenu.addAction(u'Apply')
        self.action_create.triggered.connect(self.show_apply_preset_to_layer_dialog)
                
    def showPopupMenu(self, point):
        self.contextMenu.exec_(self.listWidget_CL.mapToGlobal(point)) 

    def actionHandler_add(self):  
        # function for menu
        logging.debug('action handler_add')
        self.on_pushButton_CL_add_pressed()
              
    def actionHandler_remove(self):  
        # function for menu
        logging.debug('action handler_remove')
        self.on_pushButton_CL_remove_pressed()
        
    def show_create_preset_from_layer_dialog(self):
        logging.debug('create_preset_from_layer')
        # Get layer
        self.getActiveLayer()
        if self.RLP.LAYER_CREATION_ACTIVE :
            # show dialog
            self.create_create_layer_preset_dialog('Create Layer Prest','Preset Name:')
        
    def show_apply_preset_to_layer_dialog(self):
        logging.debug('create_preset_from_layer')
        # Get layer
        self.getActiveLayer()
        if self.RLP.LAYER_CREATION_ACTIVE :
            # show dialog
            self.create_apply_layer_preset_dialog('Create Layer Prest','Preset Name:')
                                
    def create_preset_from_layer(self):
        presetName = str(self.Dialog.ui.lineEdit.text())
        self.RLP.save_creation_layer_preset(presetName,self.RLP.LAYER_CREATION_ACTIVE)
                                
    def apply_preset_to_layers(self,text):
        self.RLP.apply_preset_to_creation_layers(text)
                    
    # listWidget_SP can only accept listWidget_AVP's drag and drop
    def dragMoveEvent_SP(self,e):
        logging.debug('custom dragMoveEvent')
        if e.source() == self.listWidget_AVP :
            e.accept()
            # Add passes to scenes
            #self.updateScenePasses()
        else :
            e.ignore()
        
    # listWidget_SP can only accept listWidget_SP's drag and drop
    # set drop action to copy
    def dragMoveEvent_ASP(self,e):
        logging.debug('custom dragMoveEvent')
        if e.source() == self.listWidget_SP :
            #self.listWidget_SP.setDefaultDropAction(QtCore.Qt.CopyAction)
            e.accept()
            e.setDropAction(QtCore.Qt.CopyAction)
            # add custom cmd to add passes to selected layers
            #self.addAssociatedPasses2Layers()
        else :
            e.ignore()
        
    # listWidget_AVP can only accept listWidget_SP's drag and drop
    def dragMoveEvent_AVP(self,e):
        logging.debug('custom dragMoveEvent')
        if e.source() == self.listWidget_SP :
            e.accept()
        else :
            e.ignore()            

    def init_combobox_L(self):
        self.comboBox_L.addItems( self.RLP.MODEL )
        self.comboBox_L.setCurrentIndex(1)

    def init_combobox_CL(self):
        self.comboBox_CL.addItems( self.RLP.LAYER_PRESET )

    def init_lineEdit_layerName(self):
        self.lineEdit_layerName.setText( self.RLP.LAYER_NAME_DEFAULT )

    def set_lineEdit_layerName(self):
        if not self.lineEdit_layerName.text() :
            self.init_lineEdit_layerName()
                                
    def insertListWidgetItem(self,listWidget,inputList):
        # Clear listWidget first
        #listWidget.clear()
        self.appendListWidgetItem(listWidget, inputList)

    def appendListWidgetItem(self,listWidget,inputList):
        returnItem = None
        # Get listWidget items first
        widgetListItems = self.getAllItemsInListWidget(listWidget)
        if self.DEBUG:
            print 'inputList',
            print inputList
        if inputList :
            widgetItem = None
            for i,name in itertools.izip( itertools.count(1), (x for x in inputList if x not in widgetListItems) ) :
                widgetItem = QtGui.QListWidgetItem(name)
                listWidget.insertItem( i, widgetItem )
                if listWidget == self.listWidget_SL or listWidget == self.listWidget_CL:
                    widgetItem.setFlags(widgetItem.flags() | QtCore.Qt.ItemIsEditable)
            if widgetItem :
                returnItem = widgetItem
        return returnItem
    
    def delSelItemsInListWidget(self,listWidget):
        items = listWidget.selectedItems()
        if items:
            for item in items :
                row = listWidget.row( item ) 
                try:
                    listWidget.takeItem( row )
                except:
                    logging.warning('delSelItemInListWidget error')
                     
    def select_obj_from_list(self):
        sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_AO)
        if sels_set_listWidget:
            # Remove objs to layer
            self.RLP.select_obj( sels_set_listWidget )
           
    def listWidget_CL_remove(self):
        listItems = self.listWidget_CL.selectedItems()
        if listItems:
            for l in listItems :
                i = self.listWidget_CL.row(l)
                try:
                    self.listWidget_CL.takeItem(i)
                except:
                    traceback.print_exc()
                    logging.warning('can not remove itemWidget')
             
    def get_widgetItem_text(self,item):
        return str(item.text())
    
    def get_selected_widgetItem_text(self,listWidget):
        nodes_set = set()
        for i in itertools.imap( lambda x:str(x.text()), listWidget.selectedItems() ) :
            nodes_set.add(i)
#        items = listWidget.selectedItems()
#        if items:
#            for item in items :
#                # Get item's text
#                nodes_set.add( str(item.text()) )
        return nodes_set
        
    def removeListWidgetItem(self,listWidget,inputStringList):
        # Clear listWidget first
        if inputStringList :
            for k in inputStringList :
                items = listWidget.findItems(k,QtCore.Qt.MatchFixedString)
                # Items maybe None
                if items:
                    i = listWidget.row(items[0])
                    try:
                        listWidget.takeItem(i)
                    except:
                        traceback.print_exc()
                        logging.warning('can not remove itemWidget')                    
                        
    def getAllItemsInListWidget(self,listWidget):
        items_dict = {}
        for i in xrange(listWidget.count()):
            item = listWidget.item(i)
            items_dict[str(item.text())] = item
        return items_dict
                
    def getTextListsFromListWidget(self,listWidget):
        texts_list = []
        for i in xrange(listWidget.count()):
            item = listWidget.item(i)
            txt =  str(item.text())
            if txt != '':
                texts_list.append(txt) 
        return texts_list
        
    def getItemsInListWidget(self,listWidget,item_text):
        items_dict = {}
        items = listWidget.findItems(item_text,QtCore.Qt.MatchFixedString)
        if items :
            items_dict[ str( items[0].text() ) ] = items[0]
        return items_dict
                        
    def getMemberInListByName(self,inputList,inputStr):
        matchMember = None
        #logging.debug( 'inputStr:',str(inputStr) )
        for l in inputList:
            if inputStr == l.keys() :
                matchMember = l
        return matchMember

    def flattenItemsInListWidget(self,listWidget):
        text_list = set( self.getTextListsFromListWidget(listWidget) )
        if self.DEBUG:
            print 'text_list:',text_list
        listWidget.clear()
        self.insertListWidgetItem(listWidget, list(text_list))
                         
    def updateLayerList(self):
        # Get layers first
        self.RLP.getLayers()
        # Get render inputDict
        self.insertListWidgetItem(self.listWidget_SL, self.RLP.LAYERS)
        
    def updateAssociatedObjectList(self):
        logging.debug('updateAssociatedObjectList')
        self.listWidget_AO.clear()
        self.getActiveLayer()
        obj_names_list = None
        if self.MODEL == 'M' :
            if self.RLP.LAYER_MANAGER_ACTIVE :
                obj_names_list = self.RLP.getObjInLayer( self.RLP.LAYER_MANAGER_ACTIVE )
                self.insertListWidgetItem(self.listWidget_AO, obj_names_list)
        else:
            if self.RLP.LAYER_CREATION_ACTIVE :
                if self.DEBUG:
                    print 'self.RLP.LAYER_CREATION_ACTIVE:',
                    print self.RLP.LAYER_CREATION_ACTIVE
                obj_names_list = self.RLP.get_creation_layer_attr( self.RLP.LAYER_CREATION_ACTIVE,'AO' )
                if self.DEBUG:
                    print 'obj_names_list:',
                    print obj_names_list
                self.insertListWidgetItem(self.listWidget_AO, obj_names_list)
        
    def updateAssociatedLightList(self):
        logging.debug('updateAssociatedObjectList')
        self.listWidget_AL.clear()
        self.getActiveLayer()
        obj_names_list = None
        if self.MODEL == 'M' :
            if self.RLP.LAYER_MANAGER_ACTIVE :
                light_names_set = self.RLP.get_light_in_layer( self.RLP.LAYER_MANAGER_ACTIVE )
                self.insertListWidgetItem(self.listWidget_AL, light_names_set)      
        else:
            if self.RLP.LAYER_CREATION_ACTIVE :
                if self.DEBUG:
                    print 'self.RLP.LAYER_CREATION_ACTIVE:',
                    print self.RLP.LAYER_CREATION_ACTIVE
                light_names_list = self.RLP.get_creation_layer_attr( self.RLP.LAYER_CREATION_ACTIVE,'AL' )
                if self.DEBUG:
                    print 'obj_names_list:',
                    print obj_names_list
                self.insertListWidgetItem(self.listWidget_AL, light_names_list)
                
    def updateOverridesList(self):
        logging.debug('updateOverridesList')
        self.listWidget_O.clear()
        self.getActiveLayer()
        if self.MODEL == 'M' :
            if self.RLP.LAYER_MANAGER_ACTIVE :
                objs = self.RLP.getOverridesInLayer( self.RLP.LAYER_MANAGER_ACTIVE )
                self.insertListWidgetItem(self.listWidget_O, objs)
        else:
            pass
    
    def updateAssociatedPassList(self):
        logging.debug('updateAssociatedPassList')
        self.listWidget_ASP.clear()
        # Get active layer first
        self.getActiveLayer()
        if self.MODEL == 'M' :
            if self.RLP.LAYER_MANAGER_ACTIVE :
                passes_list = self.RLP.getPassByLayer(self.RLP.LAYER_MANAGER_ACTIVE)
                self.insertListWidgetItem(self.listWidget_ASP, passes_list)
        else:
            if self.RLP.LAYER_CREATION_ACTIVE :
                passes_list = self.RLP.get_creation_layer_attr( self.RLP.LAYER_CREATION_ACTIVE,'AP' )
                self.insertListWidgetItem(self.listWidget_ASP, passes_list)
                        
    def updateAssociatedPasses(self):
        logging.debug('updateAssociatedPasses')
        # Get selected layers
        self.getSelectedLayers()
        # remove same items
        # TODO: must be modify later
        #self.flattenItemsInListWidget(self.listWidget_ASP)
        # Get all widgetItems in listWidget_SP
        listWidgetItems_names_list = self.getTextListsFromListWidget(self.listWidget_ASP)
        if self.MODEL == 'M' :
            # Only update if some layers selected
            if self.RLP.LAYERS_MANAGER_SELECTED and listWidgetItems_names_list :
                self.RLP.updateAssociatedPasses( listWidgetItems_names_list,self.MODEL )
        else:
            if self.RLP.LAYERS_CREATION_SELECTED and listWidgetItems_names_list :
                self.RLP.updateAssociatedPasses( listWidgetItems_names_list,self.MODEL )
                
    def updateScenePassList(self):
        logging.debug('updateScenePassList')
        self.RLP.getScenePasses()
        if self.RLP.PASSES_SCENE :
            self.insertListWidgetItem(self.listWidget_SP, self.RLP.PASSES_SCENE)

    def updateAvailablePassList(self):
        logging.debug('updateAvailablePassList')
        # Get active layer first
        self.RLP.getAvailablePasses()
        if self.RLP.PASSES_AVAILABLE :
            self.insertListWidgetItem(self.listWidget_AVP, self.RLP.PASSES_AVAILABLE)  
        
    def updateAll(self):
        # Update all layers to list
        self.updateLayerList()
        layer_current = None
        # First check if some layers in list have been selected
        self.getActiveLayer()
        if not self.RLP.LAYER_MANAGER_ACTIVE :
            # Then check if some layers in scene has been selected
            layer_current = self.RLP.get_layer_current()
            if layer_current : 
                # Set layer active
                self.set_layer_manager_active(layer_current)
        self.updateLayerSettings_manager()     
                    
    def updateLayerSettings_manager(self):
        self.getSelectedLayers()
        self.updateAssociatedObjectList()
        self.updateAssociatedLightList()
        self.updateAssociatedPassList()
        self.updateScenePassList()
        self.updateAvailablePassList()
        self.updateOverridesList()      
                    
    def updateLayerSettings_creation(self):
        self.updateLayerPresetCombobox()
        self.updateAssociatedObjectList()
        self.updateAssociatedLightList()
        self.updateAssociatedPassList()
        self.updateScenePassList()
        self.updateAvailablePassList()
        self.updateOverridesList()   
                                        
    def getSelectedLayers(self):
        if self.MODEL == 'M' :
            del self.RLP.LAYERS_MANAGER_SELECTED[:]
            #self.RLP.LAYERS_MANAGER_SELECTED = 
            for selItem in self.listWidget_SL.selectedItems() :
                # use str() to convert qstring to string
                layerName = str( selItem.text() )
                self.RLP.LAYERS_MANAGER_SELECTED.append( layerName )
        else :
            del self.RLP.LAYERS_CREATION_SELECTED[:]
            #self.RLP.LAYERS_CREATION_SELECTED = 
            for selItem in self.listWidget_CL.selectedItems() :
                # use str() to convert qstring to string
                layerName = str( selItem.text() )
                self.RLP.LAYERS_CREATION_SELECTED.append( layerName )
        self.RLP.getActiveLayer()
        
    def get_layer_name_before_rename(self):
        self.RLP.LAYER_MANAGER_ACTIVE = None
        self.RLP.LAYER_CREATION_ACTIVE = None
        logging.debug('get active layer')
        if self.MODEL == 'M' :
            layerName = ''
            #currentItem = self.ui.listWidget_L.currentItem()
            currentItems = self.listWidget_SL.selectedItems()
            if not currentItems:
                logging.debug('no active layer')
            else:
                try:
                    currentItem = currentItems[-1]
                except :
                    logging.debug('can not get active layer')
                    traceback.print_exc()
                else :
                    try:
                        layerName = str( currentItem.text() )
                    except:
                        logging.debug('can not find text()')
                        traceback.print_exc()
                    else:
                        logging.debug('currentItem: %s' ,layerName )
                        self.RLP.LAYER_MANAGER_ACTIVE = layerName
        else :
            layerName = ''
            #currentItem = self.ui.listWidget_L.currentItem()
            currentItems = self.listWidget_CL.selectedItems()
            if not currentItems:
                logging.debug('no active layer')
            else:
                try:
                    currentItem = currentItems[-1]
                except :
                    logging.debug('can not get active layer')
                    traceback.print_exc()
                else :
                    try:
                        layerName = str( currentItem.text() )
                    except:
                        logging.debug('can not find text()')
                        traceback.print_exc()
                    else:
                        #logging.debug('currentItem: ' + layerName )
                        self.RLP.LAYER_CREATION_ACTIVE = layerName
                        self.RLP.LAYER_BEFORE_RENAME = self.RLP.LAYER_CREATION_ACTIVE
                        logging.debug('LAYER_BEFORE_RENAME: %s' ,self.RLP.LAYER_BEFORE_RENAME )
                                
    def getActiveLayer(self):
        self.RLP.LAYER_MANAGER_ACTIVE = None
        self.RLP.LAYER_CREATION_ACTIVE = None
        logging.debug('get active layer')
        if self.MODEL == 'M' :
            layerName = ''
            #currentItem = self.ui.listWidget_L.currentItem()
            currentItems = self.listWidget_SL.selectedItems()
            if not currentItems:
                logging.debug('no active layer')
            else:
                try:
                    currentItem = currentItems[-1]
                except :
                    logging.debug('can not get active layer')
                    traceback.print_exc()
                else :
                    try:
                        layerName = str( currentItem.text() )
                    except:
                        logging.debug('can not find text()')
                        traceback.print_exc()
                    else:
                        logging.debug('currentItem: %s',layerName )
                        self.RLP.LAYER_MANAGER_ACTIVE = layerName
        else :
            layerName = ''
            #currentItem = self.ui.listWidget_L.currentItem()
            currentItems = self.listWidget_CL.selectedItems()
            if not currentItems:
                logging.debug('no active layer')
            else:
                try:
                    currentItem = currentItems[-1]
                except :
                    logging.debug('can not get active layer')
                    traceback.print_exc()
                else :
                    try:
                        layerName = str( currentItem.text() )
                    except:
                        logging.debug('can not find text()')
                        traceback.print_exc()
                    else:
                        logging.debug('currentItem: %s' ,layerName )
                        self.RLP.LAYER_CREATION_ACTIVE = layerName
                        logging.debug('LAYER_CREATION_ACTIVE: %s' ,self.RLP.LAYER_CREATION_ACTIVE )
            return layerName
                        
    def set_layer_manager_active(self,layer_current):
        # clear selection in listWidget_L
        self.listWidget_SL.clearSelection()
        # get widgetitem
        listItems = self.getItemsInListWidget(self.listWidget_SL, layer_current.longName())
        if listItems :
            self.listWidget_SL.setCurrentItem( listItems.values()[0] )
            logging.debug('set_layer_manager_active:')
    
    def renameLayer_SL(self):
        logging.debug('rename layer_SL')
        # Get selected listWidgetItem
        # Important: no need for self.getActiveLayer
        # Because item double clicked connected self.getActiveLayer
        if self.RLP.LAYER_MANAGER_ACTIVE :
            item = self.listWidget_SL.currentItem()
            txt = str( item.text() )
            if txt :
                #logging.debug('layer text:',str(txt))
                try :
                    self.RLP.rename( self.RLP.LAYER_MANAGER_ACTIVE, txt )
                except :
                    traceback.print_exc()
    
    def renameLayer_CL(self):
        logging.debug('rename layer_CL')
        # Get selected listWidgetItem
        # Important: no need for self.getActiveLayer
        # Because item double clicked connected self.getActiveLayer
        newName = self.getActiveLayer()
        logging.debug('newName:%s',newName)
        if newName :
            if newName != self.RLP.LAYER_BEFORE_RENAME :
                #logging.debug('layer text:',str(txt))
                try :
                    self.RLP.rename_creation_layer(newName)
                except :
                    traceback.print_exc()

    def updateScenePasses(self):
        logging.debug('updateScenePasses')
        listWidgetItems = self.getAllItemsInListWidget(self.listWidget_SP)
        if self.DEBUG:
            print listWidgetItems.keys()
        if listWidgetItems :
            self.RLP.updateScenePasses( listWidgetItems.keys() )
                    
    def addAssociatedPasses2Layers(self):
        pass_names_list = []
        # Get selected widgetItems in listWidget_SP
        self.getSelectedLayers()
        listWidgetItems = self.listWidget_SP.selectedItems()
        for listWidgetItem in listWidgetItems :
            pass_names_list.append( str( listWidgetItem.text() ) )
        if self.RLP.LAYERS_MANAGER_SELECTED and pass_names_list :
            for layer in self.RLP.LAYERS_MANAGER_SELECTED :
                self.RLP.add_pass_to_layer(layer,pass_names_list)
        
    def on_pushButton_SL_add_pressed(self):
        newLayer = self.RLP.createNewLayer()
        # Add newlayer to listwidget
        self.appendListWidgetItem(self.listWidget_SL, {newLayer.longName():newLayer})
        
        # select newlayer in listwidget_L
        self.set_layer_manager_active(newLayer)
        # update other lists
        self.updateLayerSettings_manager()     
                            
    def on_pushButton_SL_remove_pressed(self):
        sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_SL)
        if logging.DEBUG :
            print 'sels_set_listWidget:',
            print sels_set_listWidget
        if sels_set_listWidget:
            self.removeListWidgetItem(self.listWidget_SL, sels_set_listWidget)
            # Remove pass to layer
            self.RLP.removeLayer( sels_set_listWidget )
            
    def on_pushButton_CL_add_pressed(self):
        # Important: Clear list selection
        self.listWidget_CL.clearSelection()
        
        # Get layer name
        # Get layer name
        layerName = str( self.lineEdit_layerName.text() )
        layerPrefix = self.lineEdit_layerPrefix.text()
        if layerPrefix:
            layerName = str(layerPrefix) + '_' + layerName
        layerSuffix = self.lineEdit_layerSuffix.text()
        if layerSuffix:
            layerName += '_' + str(layerSuffix)        
        layerNameExt = layerName
        # Check layer name is existes or not
        layerNameLists = self.getTextListsFromListWidget( self.listWidget_CL )
        if layerNameExt in layerNameLists :
            i = 1
            while True:
                layerNameExt = layerName + str(i)
                if layerNameExt in layerNameLists :
                    i += 1
                else :
                    break
        # Get layer preset
        layerPreset = str(self.comboBox_CL.currentText())
        
        # Add newlayer to listwidget
        currentItem = self.appendListWidgetItem(self.listWidget_CL, {layerNameExt:None})
        # Select listWidgetItem
        if currentItem :
            self.listWidget_CL.clearSelection()
            self.listWidget_CL.setCurrentItem( currentItem )
        # update LAYER_CREATION
        self.RLP.init_creation_layer_attr(layerNameExt)
        self.RLP.set_creation_layer_attr(layerNameExt,'PRESET', layerPreset,'Update')
                
    def on_pushButton_CL_remove_pressed(self):
        # Get sel layer
        self.getSelectedLayers()
        
        if self.RLP.LAYERS_CREATION_SELECTED :
            # Delete list widget items
            self.delSelItemsInListWidget(self.listWidget_CL)
            # Update creation layers
            self.RLP.remove_layers_from_creation_layers()
            
    def on_pushButton_CL_apply_pressed(self):
        # Create creation layers
        self.RLP.create_creation_layers()
        # Clear layer list widget
        self.listWidget_CL.clear()
                
    def on_pushButton_refresh_pressed(self):
        # Get selection layer first
        #self.getActiveLayer()
        self.updateAll()
        # Reselect active layer
        #self.set_layer_manager_active( self.RLP.LAYER_MANAGER_ACTIVE )

    def on_pushButton_AO_add_pressed(self):
        self.getSelectedLayers()
        # Get selection obj
        sels_set = self.RLP.get_selection_names()
        if sels_set :
            if self.MODEL == 'M' :
                if self.RLP.LAYERS_MANAGER_SELECTED :
                    # Get current obj in list
                    obj_names_set = self.RLP.get_obj_in_layer( self.RLP.LAYER_MANAGER_ACTIVE )
                    if obj_names_set:
                        sels_set = sels_set - obj_names_set
                    self.appendListWidgetItem(self.listWidget_AO, sels_set)
                    # Add objs to layer
                    self.RLP.add_obj_to_layers( self.RLP.LAYERS_MANAGER_SELECTED, sels_set )
            else:
                if self.RLP.LAYERS_CREATION_SELECTED :
                    self.appendListWidgetItem(self.listWidget_AO, sels_set)
                    if self.DEBUG:
                        print 'sels_set:',
                        print sels_set
                    self.RLP.set_creation_layers_attr( 'AO', sels_set, 'Add' )

    def on_pushButton_AL_add_pressed(self):
        self.getSelectedLayers()
        # Get selection obj
        sels_set = self.RLP.getLightInSelection()
        if sels_set :
            if self.MODEL == 'M' :
                if self.RLP.LAYERS_MANAGER_SELECTED :
                    # Get current obj in list
                    obj_names_set = self.RLP.get_light_in_layer( self.RLP.LAYER_MANAGER_ACTIVE )
                    if obj_names_set :
                        sels_set = sels_set - obj_names_set
                    self.appendListWidgetItem(self.listWidget_AL, sels_set)
                    # Add objs to layer
                    self.RLP.add_obj_to_layers( self.RLP.LAYERS_MANAGER_SELECTED, sels_set )
            else:
                if self.RLP.LAYERS_CREATION_SELECTED :
                    self.appendListWidgetItem(self.listWidget_AL, sels_set)
                    if self.DEBUG:
                        print 'sels_set:',
                        print sels_set
                    self.RLP.set_creation_layers_attr( 'AL', sels_set, 'Add' )
                    
    def on_pushButton_O_remove_pressed(self):
        # Get layer active
        self.getSelectedLayers()
        
        # For user select some widgetItems in listWidget
        sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_O)     

        if self.MODEL == 'M' :
            if self.RLP.LAYERS_MANAGER_SELECTED and sels_set_listWidget:
                self.removeListWidgetItem(self.listWidget_O, sels_set_listWidget)
                # Remove objs to layer
                self.RLP.remove_overrides_from_layers( self.RLP.LAYERS_MANAGER_SELECTED, sels_set_listWidget )
        else:
            if self.RLP.LAYERS_CREATION_SELECTED and sels_set_listWidget:
                self.removeListWidgetItem(self.listWidget_O, sels_set_listWidget)
                # Remove passes from creation layer
                self.RLP.set_creation_layers_attr('O', sels_set_listWidget, 'Remove')
            
    def on_pushButton_AO_remove_pressed(self):
        self.getSelectedLayers()
        # Get selection obj:For user select some objs in model view
        sels_set = self.RLP.get_selection_names()
        
        if self.MODEL == 'M' :
            if self.RLP.LAYERS_MANAGER_SELECTED:
                # For user select some widgetItems in listWidget
                sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_AO)
                if sels_set_listWidget:
                    # add model sel and widget sel
                    sels_set = sels_set | sels_set_listWidget
                if sels_set:
                    logging.debug('sels_set:')
                    self.RLP.log_list( sels_set )
                    self.removeListWidgetItem(self.listWidget_AO, sels_set)
                    # Remove objs to layer
                    self.RLP.remove_obj_from_layers( self.RLP.LAYERS_MANAGER_SELECTED, sels_set )
        else:
            if self.RLP.LAYERS_CREATION_SELECTED:
                # For user select some widgetItems in listWidget
                sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_AO)
                if sels_set_listWidget:
                    # add model sel and widget sel
                    sels_set = sels_set | sels_set_listWidget
                if sels_set:
                    logging.debug('sels_set:')
                    self.RLP.log_list( sels_set )
                    self.removeListWidgetItem(self.listWidget_AO, sels_set)
                    # Remove objs from creation layer
                    self.RLP.set_creation_layers_attr('AO', sels_set, 'Remove')
                                
    def on_pushButton_AL_remove_pressed(self):
        self.getSelectedLayers()
        # Get selection obj:For user select some objs in model view
        sels_set = self.RLP.getLightInSelection()
        
        if self.MODEL == 'M' :
            if self.RLP.LAYERS_MANAGER_SELECTED:
                # For user select some widgetItems in listWidget
                sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_AL)
                if sels_set_listWidget:
                    # add model sel and widget sel
                    sels_set = sels_set | sels_set_listWidget
                if sels_set:
                    logging.debug('sels_set:')
                    self.RLP.log_list( sels_set )
                    self.removeListWidgetItem(self.listWidget_AL, sels_set)
                    # Remove objs to layer
                    self.RLP.remove_obj_from_layers( self.RLP.LAYERS_MANAGER_SELECTED, sels_set )
        else:
            if self.RLP.LAYERS_CREATION_SELECTED:
                # For user select some widgetItems in listWidget
                sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_AL)
                if sels_set_listWidget:
                    # add model sel and widget sel
                    sels_set = sels_set | sels_set_listWidget
                if sels_set:
                    logging.debug('sels_set:')
                    self.RLP.log_list( sels_set )
                    self.removeListWidgetItem(self.listWidget_AL, sels_set)
                    # Remove objs from creation layer
                    self.RLP.set_creation_layers_attr('AL', sels_set, 'Remove')
    
    def on_pushButton_ASP_remove_pressed(self):
        # Get layer active
        self.getSelectedLayers()
        
        # For user select some widgetItems in listWidget
        sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_ASP)     

        if self.MODEL == 'M' :
            if self.RLP.LAYERS_MANAGER_SELECTED and sels_set_listWidget:
                self.removeListWidgetItem(self.listWidget_ASP, sels_set_listWidget)
                # Remove pass to layer
                #self.RLP.removePass2Layer( self.RLP.LAYER_MANAGER_ACTIVE, sels_set_listWidget )
                self.RLP.remove_pass_from_layers( self.RLP.LAYERS_MANAGER_SELECTED, sels_set_listWidget )
        else:
            if self.RLP.LAYERS_CREATION_SELECTED and sels_set_listWidget:
                self.removeListWidgetItem(self.listWidget_ASP, sels_set_listWidget)
                # Remove passes from creation layer
                self.RLP.set_creation_layers_attr('AP', sels_set_listWidget, 'Remove')
                    
    def on_pushButton_SP_remove_pressed(self):
        sels_set_listWidget = self.get_selected_widgetItem_text(self.listWidget_SP)
        if sels_set_listWidget :
            self.removeListWidgetItem(self.listWidget_SP, sels_set_listWidget)
            # Remove passes
            self.RLP.removeScenePasses( sels_set_listWidget )
                                                                                
    def on_pushButton_RS_apply_pressed(self):
        layerOverride = self.checkBox_layerOverride_status.isChecked()
        renderStatus = {'castsShadows':[self.checkBox_castsShadows,True],\
                        'receiveShadows':[self.checkBox_receiveShadows,True],\
                        'motionBlur':[self.checkBox_motionBlur,True],\
                        'primaryVisibility':[self.checkBox_primaryVisibility,True],\
                        'smoothShading':[self.checkBox_smoothShading,True],\
                        'visibleInReflections':[self.checkBox_visibleInReflections,True],\
                        'visibleInRefractions':[self.checkBox_visibleInRefractions,True],\
                        'doubleSided':[self.checkBox_doubleSided,True],\
                        'opposite':[self.checkBox_opposite,True]
                        }
        for v in renderStatus.itervalues() :
            v[1] = v[0].isChecked()
        self.RLP.setRenderStatus( renderStatus, layerOverride )

    def on_pushButton_CM_black_pressed(self):
        self.RLP.create_surface_shader( [0,0,0],[1,1,1],'BLACK_MATTE',\
                                      self.checkBox_layerOverride_materiral.isChecked() )
        
    def on_pushButton_CM_blackNoAlpha_pressed(self):
        self.RLP.create_surface_shader( [0,0,0],[0,0,0],'BLACK_NO_ALPHA_MATTE',\
                                      self.checkBox_layerOverride_materiral.isChecked() )        
                                        
    def on_pushButton_CM_red_pressed(self):
        self.RLP.create_surface_shader( [1,0,0],[1,1,1],'RED_MATTE',\
                                      self.checkBox_layerOverride_materiral.isChecked() )                                          
        
    def on_pushButton_CM_green_pressed(self):
        self.RLP.create_surface_shader( [0,1,0],[1,1,1],'GREEN_MATTE',\
                                      self.checkBox_layerOverride_materiral.isChecked() )
          
    def on_pushButton_CM_blue_pressed(self):
        self.RLP.create_surface_shader( [0,0,1],[1,1,1],'BLUE_MATTE',\
                                      self.checkBox_layerOverride_materiral.isChecked() )  
                                                
    def on_pushButton_CM_useBackground_pressed(self):
        #self.RLP.createShadowShader('userBackGround',None,1)
        self.RLP.create_shadow_shader('SHADOW_MATTE',\
                                      self.checkBox_layerOverride_materiral.isChecked())
                                        
    def on_pushButton_CM_zDepth_pressed(self):
        self.RLP.createZDepthShader('Z_Depth_MAT')

def setLog(logLevel):
    LOG_LEVELS = {'debug': logging.DEBUG, 'info':logging.INFO, \
              'warning': logging.WARNING, 'error': logging.ERROR,\
              'critical': logging.CRITICAL}
    LOG_LEVEL = LOG_LEVELS.get(logLevel)
    logging.basicConfig(level=LOG_LEVEL)
                                    
def getMayaWindow():
    ptr = maya.OpenMayaUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

def main(logLevel='warning',debug=True):
    setLog(logLevel)
    global RenderLayerPassManager_app
    global RenderLayerPassManager_myapp
    RenderLayerPassManager_app = QtGui.qApp
    RenderLayerPassManager_myapp = StartRenderLayerPassManager(getMayaWindow(),debug)
    RenderLayerPassManager_myapp.show()

if __name__ == "__main__":
    main()